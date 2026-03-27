# Atividade de Projeto

Esta atividade marca o início da fase de design do seu sistema baseado em agentes. O objetivo é definir as bases estruturais e funcionais que servirão para a implementação técnica nos próximos módulos.

## 1. Definição do Escopo e Problema
- **Problema a ser resolvido**: Descreva o desafio real ou a necessidade que o agente irá endereçar.
- **Público-alvo**: Quem são os usuários finais do sistema e como eles interagem com ele?

## 2. Arquitetura do Sistema Agentic
- **Padrão de Agente**: O sistema será um agente único ou multiagente? Qual o padrão de orquestração (ex: ReAct, Plan-and-Execute, Self-Reflection)?
- **Foundation Models (LLMs)**: Qual modelo (GPT-4, Gemini 1.5 Pro, Claude 3.5 Sonnet) será o "motor" do raciocínio e por quê?

## 3. Ferramentas e Integrações (Tooling)
- **Capacidades**: O que o agente deve ser capaz de fazer autonomamente?
- **Tools**: Liste as ferramentas externas (APIs, Python Interpreter, busca na web) que o agente poderá invocar.
- **MCP (opcional)**: O sistema utilizará o Model Context Protocol para acessar recursos externos?

## 4. Estratégia de Memória e RAG
- **Memória de Curto Prazo**: Como o histórico da conversa será gerenciado (janela de contexto, resumo)?
- **Memória de Longo Prazo (Agentic RAG)**: O sistema precisará acessar uma base de conhecimento? Se sim, quais dados serão indexados?

## 5. Fluxo de Trabalho (Workflows)
- Descreva o passo a passo de uma interação típica (Happy Path).
- Como o sistema deve lidar com falhas, loops infinitos ou incertezas (Fallbacks e Guardrails)?

---
> 💡 **Dica**: Tente ser o mais específico possível nesta fase. Um design bem documentado agora reduz drasticamente a complexidade na hora de escrever o código.
