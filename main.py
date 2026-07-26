import sqlite3
from src.database import criar_tabela, migrar_catalogo_json_para_sql, atualizar_valor_sql, remover_produto_sql

conexao = sqlite3.connect("data/techstore.db")
criar_tabela(conexao)
migrar_catalogo_json_para_sql("data/catalogo.json", conexao)
conexao.close()