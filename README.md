# TechStore Analytics

Sistema de gestão de catálogo de produtos e pedidos para um e-commerce fictício, construído como projeto de estudo e portfólio em Engenharia de Dados, com foco em fundamentos sólidos de Python orientado a objetos e boas práticas de engenharia de software.

## Sobre o projeto

Este projeto nasceu como terreno de prática para consolidar Programação Orientada a Objetos aplicada a um domínio real (e-commerce), evoluindo de exercícios isolados para uma arquitetura de software completa: herança e polimorfismo, encapsulamento, métodos mágicos, abstração e inversão de dependência, exceções customizadas, e testes automatizados.

Cada decisão de design documentada abaixo foi tomada de forma deliberada, com trade-offs avaliados — não copiada de tutorial.

## Funcionalidades

- Cadastro de produtos físicos e digitais, com cálculo de imposto e frete específicos por tipo
- Aplicação de descontos com validação
- Persistência em múltiplos formatos (JSON e CSV), intercambiáveis sem alterar o código consumidor
- Hierarquia de exceções customizadas para erros de negócio
- Testes automatizados cobrindo os principais fluxos

## Arquitetura

```
techstore-analytics/
├── src/
│   ├── __init__.py
│   ├── models.py              # Produto, ProdutoFisico, ProdutoDigital, Pedido
│   ├── storage_interface.py   # Contrato abstrato (ABC) para persistência
│   ├── json_storage.py        # Implementação concreta: JSON
│   ├── csv_storage.py         # Implementação concreta: CSV
│   ├── database.py
│   ├── exceptions.py          # Hierarquia de exceções customizadas
│   └── logger.py
├── data/                      # Dados gerados em execução (ignorados no git)
├── tests/
│   └── test_models.py
├── main.py
├── requirements.txt
├── pytest.ini
└── .gitignore
```

## Decisões de design

**Herança e polimorfismo.** `Produto` é a classe base, com `ProdutoFisico` e `ProdutoDigital` sobrescrevendo apenas o que realmente difere entre os dois tipos (`calcular_frete`, alíquota de imposto). Métodos que não fazem sentido para um dos tipos (frete para produto digital) não foram forçados na classe mãe com valores fictícios — em vez disso, `Produto` fornece uma implementação padrão neutra, evitando violar o Princípio de Substituição de Liskov.

**Encapsulamento.** O atributo `valor` é protegido por `@property`/`@setter`, validando a entrada na origem — inclusive na criação do objeto — em vez de espalhar validação redundante por cada método que usa o valor.

**Abstração e inversão de dependência.** `StorageInterface`, uma classe abstrata (`ABC`), define o contrato que `JsonStorage` e `CsvStorage` implementam. O código que consome o storage não precisa saber qual implementação está por trás — trocar de JSON para um banco de dados real, no futuro, não exige alterar quem usa o storage.

**Exceções customizadas.** Erros de negócio (`ValorInvalidoError`, `PercentualInvalidoError`) herdam de uma base comum (`TechstoreError`), permitindo capturar seletivamente um tipo específico ou qualquer erro de negócio do projeto de forma genérica, sem mascarar bugs reais de programação.

## Como rodar o projeto

```bash
# Clonar o repositório
git clone https://github.com/WellitonT/techstore-analytics.git
cd techstore-analytics

# Criar e ativar o ambiente virtual (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

# Instalar dependências
pip install -r requirements.txt

# Rodar o projeto
python main.py
```

## Rodando os testes

```bash
pytest tests/ -v
```

## Stack

- Python 3.13
- Biblioteca padrão (`dataclasses`, `datetime`, `uuid`, `json`, `csv`, `sqlite3`, `abc`) para toda a lógica de domínio
- `pytest` para testes automatizados

## Status

Fundamentos de Programação Orientada a Objetos completos: herança, polimorfismo, encapsulamento, métodos mágicos, abstração, exceções customizadas. Próximas adições previstas: expansão da cobertura de testes automatizados para os módulos de storage.

## Autor

Welliton — projeto desenvolvido como parte de uma trilha autodidata em Engenharia de Dados, com trajetória planejada até Machine Learning e AI Engineering.