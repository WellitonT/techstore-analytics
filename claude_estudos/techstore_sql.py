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
        cursor.execute(
            "INSERT INTO produtos (nome, valor) VALUES (?, ?)", 
            (produto.nome, produto.valor)
        )
    conexao.commit()
    print(f"{len(produtos)} produtos migrados para o banco SQL")

conexao = sqlite3.connect("techstore.db")
criar_tabela(conexao)
migrar_catalogo_json_para_sql("catalogo.json", conexao)
conexao.close()       