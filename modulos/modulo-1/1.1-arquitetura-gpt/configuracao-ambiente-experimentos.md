# Tutorial de Configuração do Ambiente para Experimentos

Durante o curso é importante isolarmos ambientes para garantir que nossos experimentos não deem conflito com outros. Para resolver esse problema, usaremos o **uv**, que é uma ferramenta para fazermos esse isolamento de ambientes.

## ⚠️ Atenção - Sistema Operacional

A partir de agora, todos os projetos e tutoriais serão feitos em ambientes baseados em **Linux** (recomendo Ubuntu). 

Para quem usa Windows, uma alternativa mais rápida é usar o **WSL** (Windows Subsystem for Linux), ou fazer um dual boot no seu PC.

**Tutorial de instalação do WSL:**
https://youtu.be/oEdIf6mB_p4?si=WAFatjz7KjJ4TmwA

**Como conectar o VS Code no WSL:**
https://youtu.be/oZOO5ZQ9Zfg?si=HnyQK9JpAkXTAQfL

> **Importante:** A partir de agora, quem estiver usando Windows deve sempre usar o WSL para comandos de terminal.

## 📓 Extensão Jupyter Notebook

Também usaremos a extensão do **Jupyter Notebook** dentro do VS Code. O Jupyter Notebook é como se fosse um caderno que permite usar células de texto markdown e código, podemos executar código passo a passo, facilitando a aprendizagem.

**Link para instalação:**
https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter

---

## 🟪 Instalação e criação de ambientes com uv

Para instalar o uv, execute os seguintes comandos:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Dentro da pasta do seu projeto, execute:

```bash
uv init --bare
```

Instale o jupyter e o ipykernel (programa que roda o código Python por trás do Jupyter Notebook) dentro do ambiente

```bash
uv add jupyter ipykernel
```

Registre o ambiente Python gerenciado pelo uv como um kernel do Jupyter para você selecioná-lo nos notebooks:

```bash
uv run python -m ipykernel install --user --name meu-ambiente --display-name "meu ambiente"
```
---