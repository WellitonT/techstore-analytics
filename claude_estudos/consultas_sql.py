import sqlite3

conexao = sqlite3.connect("techstore.db")
cursor = conexao.cursor()

cursor.execute("""
        SELECT * FROM produtos
            WHERE valor > 500
            ORDER BY valor DESC
""")

for linha in cursor.fetchall():
    print(linha)

conexao.close()