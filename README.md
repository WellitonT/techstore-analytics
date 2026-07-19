# TechStore Analytics

Projeto de estudos aplicado, construído ao longo da minha trilha de carreira em tecnologia: **Data Engineering → Machine Learning → AI Engineering**.

## Sobre o projeto

O TechStore Analytics é um sistema fictício de gestão de catálogo de produtos de e-commerce, usado como projeto contínuo para aplicar, na prática, cada conceito estudado ao longo da trilha. Em vez de exercícios isolados e descartáveis, cada fase da minha jornada de aprendizado adiciona uma nova camada a este mesmo sistema — simulando como conhecimentos se acumulam em um projeto de engenharia real.

**Evolução do projeto até agora:**
- ✅ **Fase 0 — Fundamentos de Python:** classes (POO), tratamento de erros (`try/except`), persistência em arquivos JSON
- ✅ **Git/GitHub:** versionamento de todo o código
- 🔄 **Fase 1 — SQL e Bancos de Dados (em andamento):** migração do catálogo de JSON para SQLite, consultas com `SELECT`, `WHERE`, `ORDER BY`
- ⏳ **Próximas fases:** Big Data, Cloud, Machine Learning, Deep Learning, Engenharia de IA/LLMs, MLOps

## Tecnologias utilizadas

- **Python 3** — linguagem principal
- **SQLite** — banco de dados relacional (via módulo `sqlite3` da biblioteca padrão)
- **JSON** — persistência inicial de dados (Fase 0)
- **Git/GitHub** — controle de versão

## Estrutura do repositório

```
techstore-analytics/
├── claude_estudos/       # Implementação principal do TechStore
│   ├── techstore.py      # Classe Produto, CRUD em JSON
│   └── techstore_sql.py  # Migração e integração com SQLite
├── chat_estudos/         # Exercícios de fixação por tópico
│   ├── funcoes.py
│   ├── poo.py
│   ├── poo_carrinho_compras.py
│   └── try_except.py
└── README.md
```

## Principais conceitos aplicados

- Programação Orientada a Objetos (classes, encapsulamento, métodos)
- Tratamento de exceções e validação de dados de entrada
- Serialização/desserialização de dados (JSON)
- Modelagem de dados relacional (`CREATE TABLE`, tipos, `PRIMARY KEY`, `NOT NULL`)
- Consultas SQL (`SELECT`, `WHERE`, `ORDER BY`)
- Integração Python + SQL (`sqlite3`)
- Boas práticas de engenharia: DRY (não duplicar lógica entre arquivos), guard clauses, tratamento defensivo de erros

## Sobre mim

Estou em transição de carreira para a área de tecnologia, com o objetivo de atuar como Engenheiro de Dados, evoluindo posteriormente para Machine Learning e Engenharia de IA. Este repositório documenta essa jornada de forma contínua e prática.
