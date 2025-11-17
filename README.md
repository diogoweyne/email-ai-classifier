# 📩🧠 Classificador Inteligente de E-mails com IA  
Aplicação Web criada com Python + Flask + OpenAI, capaz de analisar o conteúdo de um e-mail, 
classificá-lo como **Produtivo** ou **Improdutivo**, e ainda sugerir **uma resposta automática profissional**.

O objetivo é reduzir tempo operacional, evitar triagens manuais e ajudar equipes com grande volume de mensagens diárias.

---

## 🚀 Funcionalidades

✔ Upload de arquivos `.txt` ou `.pdf`  
✔ Entrada de texto manual  
✔ Pré-processamento simples (NLP) para limpeza de dados  
✔ Classificação automática via Inteligência Artificial  
✔ Geração de resposta automática pronta para uso  
✔ Interface simples e intuitiva  
✔ Compatível com deploy na nuvem (Render)

---

## 🛠 Tecnologias Utilizadas

| Componente | Tecnologia |
|------------|------------|
| Linguagem | Python |
| Framework Web | Flask |
| IA | OpenAI API |
| Leitura de PDF | PyPDF2 |
| UI / Frontend | HTML + Bootstrap |
| Deploy sugerido | Render |

---

## 📁 Estrutura do Projeto

```
📦 email-ai-classifier
├── app.py
├── requirements.txt
├── .env                 # NÃO deve ser enviado ao GitHub
├── Procfile             # Usado apenas para deploy (Render)
└── templates
    └── index.html
```

---

## ⚙️ Pré-requisitos

Antes de rodar o projeto, você precisa ter instalado:

- [Python 3+]
- Pip (instalado junto ao Python)
- Uma **API Key válida da OpenAI**  
  🔑 → https://platform.openai.com/account/api-keys

Caso ainda não tenha chave, crie uma gratuita com limite de uso iniciais.

---

## 📌 1. Clonar o Repositório

Abra o terminal e execute:

```bash
git clone https://github.com/diogoweyne/email-ai-classifier
cd email-ai-classifier
```

---

## 🔧 2. Criar um Ambiente Virtual (recomendado)

```bash
python -m venv .venv
```

### Ativando o ambiente virtual

**Windows PowerShell**
```bash
.\.venv\Scripts\Activate.ps1
```

**Linux / Mac**
```bash
source .venv/bin/activate
```

---

## 📦 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

---

## 🔐 4. Criar o arquivo `.env` com sua API Key

Atenção: **esse arquivo não vai para o GitHub por segurança**.

Crie o arquivo `.env` na raiz do projeto e adicione:

```env
OPENAI_API_KEY=sua-chave-aqui

```

## ▶️ 5. Executar o projeto localmente

No terminal ainda dentro da pasta do projeto:

```bash
python app.py
```

Se funcionar corretamente, aparecerá:

```
 * Running on http://127.0.0.1:5000
```

Agora abra no navegador:

👉 http://127.0.0.1:5000/

---

## 🧪 6. Testes sugeridos

### Teste Produtivo
```
Olá, podem me informar o status da minha solicitação de ressarcimento?
```

### Teste Improdutivo
```
Passando aqui apenas para desejar um ótimo final de semana!
```

### Teste via Upload PDF/TXT
Envie um documento curto com texto simples.

---

## 🌐 Deploy (opcional) — Render

1. Subir o projeto para GitHub  
2. Criar arquivo `Procfile` com:  
```
web: gunicorn app:app
```
3. Acessar https://render.com  
4. Criar Web Service usando seu repositório  
5. Adicionar variável de ambiente:  
```
OPENAI_API_KEY = sua-chave
```
