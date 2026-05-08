"""
Servidor MCP completo demonstrando todos os componentes principais do protocolo:
- Tools: funções que o cliente pode executar
- Resources: fontes de dados estáticas e templated
- Prompts: modelos de mensagens pré-definidas
- Custom Routes: endpoints HTTP personalizados (não-MCP)

Executar: python server.py
Conectar: claude mcp add meu-server -- python server.py
"""

from mcp.server.fastmcp import FastMCP
from mcp.types import TextContent, PromptMessage
from pydantic import BaseModel
from starlette.responses import JSONResponse

# =============================================================================
# CRIAÇÃO DO SERVIDOR
# =============================================================================

mcp = FastMCP(
    name="Demo Server Completo",
    instructions="Servidor de exemplo demonstrando todos os componentes MCP",
)

# =============================================================================
# TOOLS - Funções executáveis pelo cliente
# =============================================================================

class CalculatorInput(BaseModel):
    """Schema de input para a calculadora (validação automática)."""
    a: float
    b: float
    operation: str  # +, -, *, /


@mcp.tool()
def get_weather(location: str) -> str:
    """
    Tool que retorna o clima de uma localização.

    O cliente MCP pode chamar esta tool passando 'location' como argumento.
    A description aqui é usada pelo cliente para entender o que a tool faz.

    Args:
        location: Nome da cidade/localização

    Returns:
        String com descrição do clima
    """
    return f"O clima em {location} é ensolarado com 25°C."


@mcp.tool()
def calculate(a: float, b: float, operation: str) -> dict:
    """
    Tool de calculadora com validação Pydantic.

    Args:
        a: Primeiro número
        b: Segundo número
        operation: Operação matemática (+, -, *, /)

    Returns:
        Dict com o resultado da operação
    """
    ops = {
        "+": a + b,
        "-": a - b,
        "*": a * b,
        "/": a / b if b != 0 else "Erro: divisão por zero"
    }
    result = ops.get(operation, "Operação inválida")
    return {"result": result}


# =============================================================================
# RESOURCES - Fontes de dados
# =============================================================================

@mcp.resource("data://status")
def get_server_status() -> str:
    """
    Resource estático retornando status do servidor.

    Resources são fontes de dados que o cliente MCP pode ler.
    Ao contrário de tools, resources são apenas leitura (read-only).

    URI: data://status
    O cliente chama ctx.read_resource("data://status") para acessar.

    Returns:
        String com status do servidor
    """
    return "Servidor MCP operando normalmente. Versão 1.0.0"


@mcp.resource("data://config/{section}")
def get_config(section: str) -> str:
    """
    Resource templated para buscar configurações.

    Templates usam {param} na URI. O FastMCP extrai automaticamente
    o parametro do URI e passa como argumento à função.

    URI: data://config/{section}
    Exemplo de uso: ctx.read_resource("data://config/database")

    Args:
        section: Seção da configuração desejada (database, api, cache)

    Returns:
        String JSON com configuração da seção
    """
    configs = {
        "database": '{"host": "localhost", "port": 5432, "name": "mydb"}',
        "api": '{"version": "v1", "timeout": 30}',
        "cache": '{"ttl": 3600, "max_size": 1000}',
    }
    return configs.get(section, f"Seção '{section}' não encontrada")


@mcp.resource("data://users/{user_id}")
def get_user(user_id: str) -> str:
    """
    Resource templated para buscar dados de usuário.

    URI: data://users/{user_id}
    Exemplo: ctx.read_resource("data://users/123")

    Args:
        user_id: ID do usuário

    Returns:
        String JSON com dados do usuário
    """
    return f'{{"id": "{user_id}", "name": "Usuário {user_id}", "active": true}}'


# =============================================================================
# PROMPTS - Modelos de mensagens pré-definidas
# =============================================================================

@mcp.prompt()
def analyze_data(table_name: str, analysis_type: str = "summary") -> list[dict]:
    """
    Prompt para análise de dados.

    Prompts são modelos de mensagens pré-configuradas que o cliente
    pode invocar. Útil para padronizar prompts comuns ou criar
    workflows de prompt complexos.

    Args:
        table_name: Nome da tabela a analisar
        analysis_type: Tipo de análise (summary, detailed, trend)

    Returns:
        Lista de mensagens (UserMessage ou AssistantMessage)
    """
    prompts = {
        "summary": f"Faça um resumo dos dados da tabela {table_name}.",
        "detailed": f"Faça uma análise detalhada da tabela {table_name}, incluindo estatísticas.",
        "trend": f"Analise as tendências na tabela {table_name}.",
    }
    return [
        PromptMessage(role="user", content=TextContent(type="text", text=prompts.get(analysis_type, prompts["summary"])))
    ]


@mcp.prompt()
def generate_report(topic: str, format: str = "markdown") -> list[dict]:
    """
    Prompt para geração de relatórios.

    Args:
        topic: Tópico do relatório
        format: Formato de saída (markdown, json, html)

    Returns:
        Lista de mensagens para o LLM gerar o relatório
    """
    return [
        PromptMessage(role="user", content=TextContent(type="text", text=f"Gere um relatório sobre: {topic}")),
        PromptMessage(role="assistant", content=TextContent(type="text", text=f"O relatório será gerado em formato {format}.")),
    ]


# =============================================================================
# CUSTOM ROUTES - Endpoints HTTP não-MCP
# =============================================================================

@mcp.custom_route("/health", methods=["GET"])
async def health_check(request) -> JSONResponse:
    """
    Endpoint customizado para health check.

    Custom routes permitem adicionar endpoints HTTP regulares
    ao servidor MCP. Não fazem parte do protocolo MCP - são
    endpoints REST comuns para monitoramento, logs, etc.

    O protocolo MCP continua funcionando normalmente em paralelo.

    Returns:
        JSONResponse com status de saúde do servidor
    """
    return JSONResponse({"status": "healthy", "service": "mcp-demo-server"})


# =============================================================================
# EXECUÇÃO DO SERVIDOR
# =============================================================================

if __name__ == "__main__":
    # stdio é o transport padrão para conectar com clientes MCP (Claude Code, etc)
    mcp.run("stdio")
