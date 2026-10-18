# TechStore Analytics

Projeto de fundamentos em Python, construído para praticar Programação Orientada a Objetos e engenharia de software em cima de um domínio concreto (uma loja de tecnologia), em vez de exercícios isolados. O projeto cresce a cada fase de estudo.

## O que o projeto demonstra

- **Modelagem com `dataclass`:** `datetime.date` e `uuid4` com `field(default_factory=...)`.
- **Herança e polimorfismo:** alíquota definida no nível da classe e sobrescrita nas subclasses, com cálculo de frete.
- **Encapsulamento:** validação via `@property` e `@setter`.
- **Métodos especiais (dunder):** objetos ordenáveis com `sorted()` sem precisar de `key=`.
- **Abstração e inversão de dependência:** `StorageInterface(ABC)` com implementações `JsonStorage` e `CsvStorage`, trocáveis sem mexer na regra de negócio.
- **Exceções customizadas:** hierarquia `TechstoreError` → `ValorInvalidoError` e `PercentualInvalidoError`.
- **Logging:** módulo próprio de log.
- **Testes:** `pytest`.

## Estrutura

```
techstore-analytics/
├── src/
│   ├── models.py          # Classes de domínio
│   ├── json_storage.py    # Persistência em JSON
│   ├── csv_storage.py     # Persistência em CSV
│   ├── database.py        # Persistência em banco de dados
│   └── logger.py          # Configuração de logging
├── data/
├── main.py
└── pytest.ini
```

## Como rodar

```powershell
git clone https://github.com/WellitonT/techstore-analytics.git
cd techstore-analytics

python -m venv venv
.\venv\Scripts\Activate.ps1

python main.py
```

## Testes

```powershell
python -m pytest
```

## Status

**Concluído:** modelagem orientada a objetos (herança, polimorfismo, encapsulamento, abstração), persistência em múltiplos formatos, hierarquia de exceções e logging.

**Papel no portfólio:** este é o projeto de fundamentos. A aplicação de engenharia de dados em pipeline está no [NBA Data Warehouse](https://github.com/WellitonT/nba-data-warehouse).

## Autor

Welliton ([LinkedIn](https://www.linkedin.com/in/welliton-tiene-336bb7207/)) · trilha autodidata em dados, rumo a MLOps.
