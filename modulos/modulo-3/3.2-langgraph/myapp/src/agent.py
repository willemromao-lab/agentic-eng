from operator import add
from typing import Literal
import os

from typing_extensions import Annotated, NotRequired, TypedDict

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, AnyMessage
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
    

load_dotenv()


class SupportState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
    ticket: NotRequired[str]
    area: NotRequired[str]
    resposta: NotRequired[str]
    passos: NotRequired[Annotated[list[str], add]]


router_model = ChatOpenAI(
    model="gpt-5-mini",
    openai_api_key=os.environ["OPENAI_API_KEY"],
    openai_api_base=os.environ["BASE_URL"],
    temperature=0,
)


def classify_area(state: SupportState) -> dict:
    latest_human_ticket = None
    for msg in reversed(state.get("messages", [])):
        msg_type = getattr(msg, "type", None)
        if msg_type is None and isinstance(msg, dict):
            msg_type = msg.get("type") or msg.get("role")

        if msg_type in ("human", "user"):
            if isinstance(msg, dict):
                content = msg.get("content", "")
            else:
                content = getattr(msg, "content", "")

            if not isinstance(content, str):
                raise ValueError("Formato de entrada invalido: 'content' da mensagem deve ser string.")

            latest_human_ticket = content
            break

    ticket = latest_human_ticket or state.get("ticket", "")
    if not isinstance(ticket, str) or not ticket.strip():
        raise ValueError("Entrada invalida: informe 'ticket' (string) ou 'messages' com mensagem humana em texto.")

    prompt = (
        "Classifique o ticket em apenas uma categoria: 'financeiro' ou 'tecnico'. "
        "Responda com apenas uma palavra, sem explicacoes.\n\n"
        f"Ticket: {ticket}"
    )
    llm_out = router_model.invoke(prompt)
    guess = (llm_out.content or "").strip().lower()

    if "finance" in guess:
        area = "financeiro"
    elif "tecnico" in guess or "técnico" in guess:
        area = "tecnico"
    else:
        raise ValueError(f"Classificacao invalida do LLM: '{guess}'. Esperado 'financeiro' ou 'tecnico'.")

    return {"ticket": ticket, "area": area, "passos": [f"classify:{area}"]}


def route_area(state: SupportState) -> Literal["financeiro_flow", "tecnico_flow"]:
    return "financeiro_flow" if state["area"] == "financeiro" else "tecnico_flow"


def financeiro_reply(state: SupportState) -> dict:
    answer = "Encaminhado para Financeiro: vamos revisar fatura/pagamento e retornar protocolo."
    return {
        "resposta": answer,
        "messages": [AIMessage(content=answer)],
        "passos": ["financeiro_reply"],
    }


def tecnico_reply(state: SupportState) -> dict:
    answer = "Encaminhado para Suporte Tecnico: vamos diagnosticar falha de acesso/uso e orientar proximos passos."
    return {
        "resposta": answer,
        "messages": [AIMessage(content=answer)],
        "passos": ["tecnico_reply"],
    }


# Subgrafo financeiro
financeiro_builder = StateGraph(SupportState)
financeiro_builder.add_node("financeiro_reply", financeiro_reply)
financeiro_builder.add_edge(START, "financeiro_reply")
financeiro_builder.add_edge("financeiro_reply", END)
financeiro_flow = financeiro_builder.compile()


# Subgrafo técnico
tecnico_builder = StateGraph(SupportState)
tecnico_builder.add_node("tecnico_reply", tecnico_reply)
tecnico_builder.add_edge(START, "tecnico_reply")
tecnico_builder.add_edge("tecnico_reply", END)
tecnico_flow = tecnico_builder.compile()


# Grafo pai
parent_builder = StateGraph(SupportState)
parent_builder.add_node("classify_area", classify_area)
parent_builder.add_node("financeiro_flow", financeiro_flow)
parent_builder.add_node("tecnico_flow", tecnico_flow)
parent_builder.add_edge(START, "classify_area")
parent_builder.add_conditional_edges(
    "classify_area",
    route_area,
    ["financeiro_flow", "tecnico_flow"],
)
parent_builder.add_edge("financeiro_flow", END)
parent_builder.add_edge("tecnico_flow", END)

# Export que o langgraph.json referencia: ./src/agent.py:agent
agent = parent_builder.compile()