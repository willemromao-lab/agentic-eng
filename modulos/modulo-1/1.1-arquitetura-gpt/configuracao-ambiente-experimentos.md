# Tutorial de Configuração do Ambiente para Experimentos

Durante o curso é importante isolarmos ambientes para garantir que nossos experimentos não deem conflito com outros. Para resolver esse problema, usaremos o **Miniconda**, que é uma ferramenta para fazermos esse isolamento de ambientes.

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

## 🐍 Instalação do Miniconda

Para instalar o Miniconda, execute os seguintes comandos:

```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
```

Ative o Conda:

```bash
source ~/miniconda3/bin/activate
```

Inicialize o Conda para todos os shells:

```bash
conda init --all
```

Configure para não ativar o ambiente base automaticamente:

```bash
conda config --set auto_activate_base false
```

Verifique se o Conda foi instalado corretamente:

```bash
conda --version
```

✅ Se estiver OK, vai mostrar a versão do Conda instalada.

---

## 🔧 Criando um Ambiente

Criando um ambiente com uma versão específica do Python com pip e motor de execução do Python no Jupyter:

**Sintaxe:**
```bash
conda create --name <ENV_NAME> python=<PYTHON_VERSION> pip ipykernel
```

**Exemplo:**
```bash
conda create --name curso_llms_agentes python=3.12 pip ipykernel
```

---

## ✅ Ativando o Ambiente

**Sintaxe:**
```bash
conda activate <ENV_NAME>
```

**Exemplo:**
```bash
conda activate curso_llms_agentes
```

---

## 📦 Instalando Pacotes pip

**Instalando um pacote:**

Sintaxe:
```bash
pip install <PACKAGE>
```

Exemplo:
```bash
pip install langchain
```

**Instalando muitos pacotes:**

Sintaxe:
```bash
pip install <PACKAGE1> <PACKAGE2> <PACKAGE3>
```

Exemplo:
```bash
pip install langchain langgraph
```

---

## 📋 Comandos Úteis

| Comando | Descrição |
|---------|-----------|
| `conda deactivate` | Desativar o ambiente atual |
| `conda info --envs` | Listar todos os ambientes |
| `conda remove --name <ENV_NAME> --all` | Remover um ambiente |
| `pip list` | Listar pacotes instalados |