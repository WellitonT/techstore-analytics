import sqlite3
from src.json_storage import carregar_catalogo


# ============================================================
# Configuração inicial do banco
# ============================================================

def criar_tabela(conexao):
    """Cria as tabelas produtos e pedidos, se ainda não existirem."""
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            valor REAL NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pedidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto_id INTEGER NOT NULL,
            quantidade INTEGER NOT NULL,
            FOREIGN KEY (produto_id) REFERENCES produtos(id)
        )
    """)
    conexao.commit()


def adicionar_coluna_categoria(conexao):
    """Adiciona a coluna 'categoria' à tabela produtos, se ainda não existir."""
    cursor = conexao.cursor()
    try:
        cursor.execute("ALTER TABLE produtos ADD COLUMN categoria TEXT")
        conexao.commit()
    except sqlite3.OperationalError:
        pass  # coluna já existe, ignora


# ============================================================
# CRUD de produtos
# ============================================================

def migrar_catalogo_json_para_sql(caminho_json, conexao):
    """Migra produtos de um catálogo JSON para o banco SQL, sem duplicar
    produtos que já foram migrados anteriormente (operação idempotente)."""
    produtos = carregar_catalogo(caminho_json)
    cursor = conexao.cursor()
    for produto in produtos:
        cursor.execute("SELECT id FROM produtos WHERE nome = ?", (produto.nome,))
        if cursor.fetchone() is None:
            cursor.execute(
                "INSERT INTO produtos (nome, valor) VALUES (?, ?)",
                (produto.nome, produto.valor)
            )
    conexao.commit()
    print("Migração concluída")


def atualizar_valor_sql(conexao, nome_produto, novo_valor):
    """Atualiza o valor de um produto pelo nome. Imprime quantas linhas
    foram afetadas (0 indica que o produto não foi encontrado)."""
    cursor = conexao.cursor()
    cursor.execute("""
        UPDATE produtos SET valor = ? WHERE nome = ?
    """, (novo_valor, nome_produto))
    conexao.commit()
    print(f"Linhas afetadas: {cursor.rowcount}")


def remover_produto_sql(conexao, nome_produto):
    """Remove um produto pelo nome. Imprime quantas linhas foram removidas
    (0 indica que o produto não foi encontrado)."""
    cursor = conexao.cursor()
    cursor.execute("""
        DELETE FROM produtos WHERE nome = ?
    """, (nome_produto,))
    conexao.commit()
    print(f"Linhas removidas: {cursor.rowcount}")


# ============================================================
# Categorias e relatórios agregados
# ============================================================

def popular_categorias(conexao, categorias: dict):
    """Atualiza a categoria de cada produto com base em um dicionário
    {nome_do_produto: categoria}."""
    cursor = conexao.cursor()
    for nome, categoria in categorias.items():
        cursor.execute(
            "UPDATE produtos SET categoria = ? WHERE nome = ?",
            (categoria, nome)
        )
    conexao.commit()


def estatisticas_por_categoria(conexao):
    """Retorna, por categoria: quantidade de produtos, soma dos valores
    e o maior valor."""
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT categoria, COUNT(*), SUM(valor), MAX(valor)
        FROM produtos
        GROUP BY categoria
    """)
    return cursor.fetchall()

def categorias_com_multiplos_produtos(conexao):
    """Retorna categorias que possuem mais de um produto cadastrado,
    usando CTE para agregar antes de filtrar."""
    cursor = conexao.cursor()
    cursor.execute("""
        WITH contagem_por_categoria AS (
            SELECT categoria, COUNT(*) AS quantidade
            FROM produtos
            GROUP BY categoria
        )
        SELECT categoria, quantidade FROM contagem_por_categoria
        WHERE quantidade > 1
    """)
    return cursor.fetchall()

def produto_mais_caro(conexao):
    """Retorna (nome, valor) do produto com maior valor no catálogo,
    usando subquery para calcular o máximo dinamicamente."""
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT nome, valor FROM produtos
        WHERE valor = (SELECT MAX(valor) FROM produtos)
    """)
    return cursor.fetchone()

# ============================================================
# Pedidos
# ============================================================

def inserir_pedido(conexao, produto_id: int, quantidade: int):
    """Registra um novo pedido, referenciando um produto existente pelo id."""
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO pedidos (produto_id, quantidade) VALUES (?, ?)",
        (produto_id, quantidade)
    )
    conexao.commit()


def relatorio_pedidos(conexao):
    """Retorna todos os pedidos com os dados do produto associado
    (nome, valor unitário) e o valor total de cada pedido."""
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT pedidos.id, produtos.nome, produtos.valor, pedidos.quantidade,
               produtos.valor * pedidos.quantidade AS valor_total
        FROM pedidos
        JOIN produtos ON pedidos.produto_id = produtos.id
    """)
    return cursor.fetchall()