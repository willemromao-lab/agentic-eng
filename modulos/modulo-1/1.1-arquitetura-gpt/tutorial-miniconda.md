# Tutorial de Instalação do Miniconda no Linux

## O que é o Conda?

O Conda é um gerenciador de pacotes e ambientes de código aberto. Ele permite instalar, executar e atualizar rapidamente pacotes e suas dependências, além de criar, salvar, carregar e alternar facilmente entre diferentes ambientes em seu computador local.

O **Miniconda** é uma versão minimalista do Anaconda que inclui apenas o conda, Python e um pequeno número de pacotes essenciais. É ideal para quem deseja uma instalação leve e quer instalar apenas os pacotes necessários.

Neste curso, utilizaremos o Miniconda para facilitar o isolamento de experimentos no Jupyter Notebook, permitindo criar ambientes independentes para cada projeto sem conflitos de dependências.

## 1. Download

Baixe a versão mais recente do Miniconda executando o comando apropriado para sua arquitetura:

**Linux x86:**
```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

### (Opcional) Verificar a integridade do instalador

A Anaconda recomenda verificar a integridade do instalador após o download. Consulte a documentação oficial para instruções detalhadas.

## 2. Instalação

Execute o instalador com o comando apropriado para sua arquitetura:

**Linux x86:**
```bash
bash Miniconda3-latest-Linux-x86_64.sh
```

Durante a instalação:

1. Pressione `Enter` para revisar o EULA (Contrato de Licença)
2. Digite `yes` para aceitar o EULA
3. Pressione `Enter` para aceitar o diretório padrão ou especifique outro caminho
4. Escolha uma opção de inicialização:
   - **Yes (Recomendado):** O conda modifica automaticamente sua configuração de shell
   - **No:** Você precisará inicializar o conda manualmente após a instalação

## 3. Ativar a instalação

Feche e reabra o terminal, ou execute:

```bash
source ~/.bashrc
```

Você deve ver `(base)` no prompt do terminal, indicando que está no ambiente base do conda.

## 4. Verificar a instalação

Teste sua instalação executando:

```bash
conda list
```

Ou verifique a versão instalada:

```bash
conda --version
```

Se a instalação foi bem-sucedida, você verá a lista de pacotes instalados ou o número da versão do conda.

## 5. Criar e ativar ambientes virtuais

Os ambientes virtuais permitem isolar projetos com diferentes dependências e versões de Python.

### Criar um novo ambiente

Para criar um ambiente com uma versão específica do Python:

```bash
conda create -n nome_do_ambiente python=3.10
```

Por exemplo, para criar um ambiente chamado "llm_project":

```bash
conda create -n llm_project python=3.10
```

### Ativar um ambiente

Para ativar o ambiente criado:

```bash
conda activate nome_do_ambiente
```

Exemplo:

```bash
conda activate llm_project
```

Após ativar, você verá `(llm_project)` no prompt do terminal em vez de `(base)`.

### Desativar um ambiente

Para retornar ao ambiente base:

```bash
conda deactivate
```

### Listar ambientes existentes

Para ver todos os ambientes criados:

```bash
conda env list
```

### Instalar pacotes em um ambiente

Com o ambiente ativado, instale pacotes usando:

```bash
conda install nome_do_pacote
```

Ou usando pip:

```bash
pip install nome_do_pacote
```

### Remover um ambiente

Para excluir um ambiente que não é mais necessário:

```bash
conda env remove -n nome_do_ambiente
```