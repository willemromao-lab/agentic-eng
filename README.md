# Engenharia de LLMs e Sistemas Agentic

[![Licença: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.pt-br)



### Módulo 1 - Large Language Models (LLMs)

- <details>
  <summary><strong>1.1 - Arquitetura Generative Pre-trained Transformer (GPT)</strong></summary>

  - Embeddings e Tokenização  
  - Positional Encoding  
  - Dropout  
  - Blocos Transformer  

  **Referências**
  - *Alammar, Cap. 1-3*
  - *Huyen, Cap. 1-2*

  </details>

- <details>
  <summary><strong>1.2 - Post-Training e Eficiência</strong></summary>

  - Fine-Tuning (LoRA, QLoRA, SFT, RLHF e DPO)
  - Quantização
  - Small Language Models (SLMs)

  **Referências**
  - *Alammar, Cap. 7 (p. 200-201), 11-12*
  - *Huyen, Cap. 7, 9*
  - *Albada, Cap. 7 (p. 146-162)*

  </details>

- <details>
  <summary><strong>1.3 - Multimodal Large Language Models (MLLM) e Interface de Modelos</strong></summary>

  - CLIP/BLIP-2
  - Integração via API (OpenAI/Gemini)

  **Referências**
  - *Alammar, Cap. 9*
  - *Albada, Cap. 1 (p. 5)*

  </details>


### Módulo 2 - Sistemas Agentic

- <details>
  <summary><strong>2.1 - Teoria de Agentes</strong></summary>

  - Prompt Engineering
  - ReAct e Chain-of-Thought (CoT)
  - Reflexion e Planejamento
  - Agents Protocol (A2A, ACP, MCP)
  - LLM Routing e Fallbacks
  - Guardrails e Proteção contra Prompt Injection
  - Human-in-the-loop (HITL)

  **Referências**
  - *Allamar, Cap. 6, 7 (p. 218-224)*
  - *Huyen, Cap. 5, 6 (p. 275-304)*
  - *Albada Cap. 1-8, 11 (p. 251-253), 12*

  </details>

- <details>
  <summary><strong>2.2 - Geração Aumentada via Recuperação (RAG)</strong></summary>

  - Bancos Vetoriais
  - Métricas de similaridade (Cosseno, Euclidiana)
  - Algoritmos de busca (IVF vs HNSW)
  - Busca Híbrida
  - Agentic RAG
  - Graph RAG

  **Referências**
  - *Alammar, Cap. 8*
  - *Huyen, Cap. 6 (p. 253-274)*
  - *Albada, Cap. 6*

  </details>


### Módulo 3 - LangChain, MCP e LangGraph

- <details>
  <summary><strong>3.1 - LangChain</strong></summary>

  - Chains
  - Memory (Short/Long term)
  - Tools
  - Implementações dos tópicos 2.1 e 2.2

  </details>

- <details>
  <summary><strong>3.2 - LangGraph</strong></summary>

  - Grafos de estado (State Schema)
  - Nodes
  - Reducers
  - Paralelização
  - Sub-grafos

  </details>

- <details>
  <summary><strong>3.3 - Model Context Protocol (MCP)</strong></summary>

  - Arquitetura
  - Protocolo
  - Primitives (Tools, Resources e Prompts)

  </details>

- <details>
  <summary><strong>3.4 - Projeto</strong></summary>

  - Definição do escopo, design da arquitetura do agente e seleção dos Foundation Models
  - Implementação de Tools, integração de bancos vetoriais e orquestração de memória

  **Referências**
  - *Allamar, Cap 7*
  - *Huyen, Cap 1 (p. 28-34), 10*
  - *Albada, Cap. 1, 4*

  </details>

### Módulo 4 - AgentOps e LangSmith

- <details>
  <summary><strong>4.1 - Deployment</strong></summary>

  - LangSmith Cloud
  - FastAPI, Postgres e Docker

  </details>

- <details>
  <summary><strong>4.2 - Avaliação</strong></summary>

  - Métricas (Perplexity, Rouge, BLEU)
  - Datasets e Experimentos
  - Gerenciamento de Prompts
  - LLM-as-judge
  - Comparação Pairwise
  - Testes A/B

  **Referências**
  - *Huyen, Cap. 3-4*
  - *Albada, Cap. 9 e 11*

  </details>

- <details>
  <summary><strong>4.3 - Observabilidade</strong></summary>

  - Tracing
  - Runs
  - Monitoramento de latência e custo
  - Queues e Annotations

  **Referências**
  - *Huyen, Cap. 10 (p. 465-491)*
  - *Albada, Cap. 10*

  </details>

- <details>
  <summary><strong>4.4 - Projeto</strong></summary>

  - Avaliação dos agentes e deploy

  </details>
