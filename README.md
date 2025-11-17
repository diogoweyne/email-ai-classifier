# 📩 Classificador Inteligente de E-mails — IA + Python + Flask

Este projeto consiste em uma aplicação web capaz de **classificar e-mails automaticamente** em duas categorias:

- **Produtivo** — quando o e-mail requer ação, resposta, atualização ou suporte
- **Improdutivo** — quando o e-mail não exige ação imediata, como mensagens de cortesia ou felicitações

Além da classificação, o sistema **gera uma resposta automática profissional** baseada no conteúdo do e-mail, utilizando Inteligência Artificial.

---

## 🚀 Tecnologias Utilizadas

- **Python 3**
- **Flask** *(Backend Web)*
- **OpenAI API** *(Classificação + Respostas automatizadas)*
- **PyPDF2** *(Leitura de arquivos PDF)*
- **HTML + Bootstrap** *(Interface Web)*

---

## 🧠 Como Funciona

1. O usuário envia um arquivo `.txt` ou `.pdf` **ou** cola o texto do e-mail
2. O backend limpa e pré-processa o texto
3. O sistema envia o texto para a **IA da OpenAI**
4. A IA devolve um **JSON com categoria e resposta sugerida**
5. A interface exibe o resultado em tempo real

---

## 🖥️ Rodando Localmente

### Pré-requisitos:
- Python 3 instalado
- Chave da API da OpenAI
- Virtualenv (opcional, mas recomendado)

### Passos:

```bash
# 1. Clone o repositório
git clone https://github.com/<seu-usuario>/<seu-repo>.git

# 2. Acesse a pasta do projeto
cd email-ai-classifier

# 3. Crie um ambiente virtual
python -m venv .venv

# 4. Ative o ambiente virtual
# Windows
.\.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

# 5. Instale as dependências
pip install -r req
