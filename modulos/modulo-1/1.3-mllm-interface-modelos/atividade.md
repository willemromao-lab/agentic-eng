# Atividade (Multimodal Large Language Models)

1. Configure um ambiente com UV conforme ensinado anteriormente [aqui](/modulos/modulo-1/1.1-arquitetura-gpt/configuracao-ambiente-experimentos.md).
2. Instale as bibliotecas:
    - openai
    - python-dotenv
2. Crie um arquivo `.env` dentro desse ambiente e defina uma variável chamada `AZURE_OPENAI_API_KEY`. Em seguida, cole a chave de API fornecida.
3. Em um jupyter notebook carregue a variável de ambiente. Use o SDK da OpenAI conforme o [exemplo fornecido](/modulos/modulo-1/1.3-mllm-interface-modelos/integracao-azure.ipynb) e faça uma chamada ao modelo passando uma URL de uma imagem de sua escolha e solicitando uma descrição da imagem.