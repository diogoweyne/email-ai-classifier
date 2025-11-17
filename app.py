import os
import io
import json
import re

from flask import Flask, render_template, request
from dotenv import load_dotenv
from openai import OpenAI
import PyPDF2

# Carregar variáveis do .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

app = Flask(__name__)


def extract_text_from_file(file_storage):
    """Lê texto de .txt ou .pdf."""
    filename = file_storage.filename.lower()

    if filename.endswith(".txt"):
        content = file_storage.read().decode("utf-8", errors="ignore")
        return content

    if filename.endswith(".pdf"):
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(file_storage.read()))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
        return text

    return ""


def preprocess_text(text: str) -> str:
    """Limpeza simples do texto (pré-processamento NLP básico)."""
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9À-ÿ.,!?;:\s@]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def classify_and_respond(original_text: str):
    """Classifica e sugere resposta usando IA."""
    prompt = f"""
Você é um assistente de atendimento ao cliente de uma grande empresa do setor financeiro.

Classifique o email como:
- "Produtivo": quando o conteúdo pede ação, solicitação, dúvida ou status.
- "Improdutivo": quando o conteúdo é apenas social, felicitações, agradecimento, sem ação.

Depois gere uma resposta automática profissional e direta.

Responda **exclusivamente** no formato JSON abaixo:

{{
  "categoria": "Produtivo ou Improdutivo",
  "resposta": "texto sugerido"
}}

Texto do e-mail analisado:
\"\"\"{original_text}\"\"\"
"""

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Você é um assistente automatizado especializado em atendimento corporativo."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.1
    )

    content = completion.choices[0].message.content

    try:
        data = json.loads(content)
        categoria = data.get("categoria", "Não classificado")
        resposta = data.get("resposta", "Não foi possível gerar resposta automática.")
    except json.JSONDecodeError:
        categoria = "Não classificado"
        resposta = content

    return categoria, resposta


@app.route("/", methods=["GET", "POST"])
def index():
    email_text = ""
    categoria = None
    resposta_sugerida = None
    erro = None

    if request.method == "POST":
        uploaded_file = request.files.get("file")
        texto_digitado = request.form.get("email_textarea", "").strip()

        if uploaded_file and uploaded_file.filename != "":
            email_text = extract_text_from_file(uploaded_file)
        elif texto_digitado:
            email_text = texto_digitado
        else:
            erro = "Envie um arquivo (.txt ou .pdf) ou cole o texto do e-mail."
            return render_template("index.html", erro=erro)

        if not email_text.strip():
            erro = "Não foi possível identificar texto válido."
            return render_template("index.html", erro=erro)

        processed = preprocess_text(email_text)
        categoria, resposta_sugerida = classify_and_respond(processed)

    return render_template("index.html",
                           email_text=email_text,
                           categoria=categoria,
                           resposta_sugerida=resposta_sugerida,
                           erro=erro)


if __name__ == "__main__":
    app.run(debug=True)
