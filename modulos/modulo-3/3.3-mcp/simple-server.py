
from mcp.server.fastmcp import FastMCP
import uvicorn

mcp = FastMCP("Demo Server")

@mcp.tool()
def get_weather(location: str) -> str:
    """Retorna o clima para uma localização."""
    return f"O clima em {location} é ensolarado com 25°C."

@mcp.tool()
def calculate(a: float, b: float, operation: str) -> float:
    """Calculadora simples: +, -, *, /"""
    ops = {"+": a + b, "-": a - b, "*": a * b, "/": a / b if b != 0 else "Erro"}
    return ops.get(operation, "Operação inválida")

if __name__ == "__main__":
    uvicorn.run(mcp.streamable_http_app(), host="0.0.0.0", port=8000)
