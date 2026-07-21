import sqlite3
from techstore import Produto, carregar_catalogo

def criar_tabela(conexao):
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            valor REAL NOT NULL
        )
        """)
    conexao.commit()

def migrar_catalogo_json_para_sql(caminho_json, conexao):
    produtos = carregar_catalogo(caminho_json)
    cursor = conexao.cursor()

    for produto in produtos:
        cursor.execute("SELECT id FROM produtos WHERE nome = ?", (produto.nome,))
        ja_existe = cursor.fetchone()

        if ja_existe is None:
            cursor.execute(
                "INSERT INTO produtos (nome, valor) VALUES (?, ?)",
                (produto.nome, produto.valor)
            )

    conexao.commit()
    print(f"Migração concluída")

def atualizar_valor_sql(conexao, nome_produto, novo_valor):
    cursor = conexao.cursor()
    cursor.execute("""
        UPDATE produtos
        SET valor = ?
        WHERE nome = ?
    """, (novo_valor, nome_produto))
    conexao.commit()

def remover_produto_sql(conexao, nome_produto):
    cursor = conexao.cursor()
    cursor.execute("""
        DELETE FROM produtos
        WHERE nome = ?
    """, (nome_produto,))
    conexao.commit()
    print(f"Linhas removidas: {cursor.rowcount}")

conexao = sqlite3.connect("techstore.db")
criar_tabela(conexao)
migrar_catalogo_json_para_sql("catalogo.json", conexao)
atualizar_valor_sql(conexao, "Teclado Redragon", 199.0)
remover_produto_sql(conexao, "Monitor AOC")
conexao.close()      