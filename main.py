# %%
import sqlite3
from src.database import criar_tabela, migrar_catalogo_json_para_sql, atualizar_valor_sql, remover_produto_sql, categorias_com_multiplos_produtos, ranking_produtos_por_categoria
# teste_csv.py, na RAIZ do projeto, não dentro de src/
from src.csv_storage import CsvStorage
from src.json_storage import JsonStorage

conexao = sqlite3.connect("data/techstore.db")
#resultado = ranking_produtos_por_categoria(conexao)
#print(resultado)

#conexao_produtos = carregar_catalogo("data/catalogo.json")
#salvar_catalogo_csv(conexao_produtos, "data/catalogo.csv")

#produtos_csv = carregar_catalogo_csv("data/catalogo.csv")
#for p in produtos_csv:
#    print(p.nome, p.valor)
atualizar_valor_sql(conexao, "Iphone 17 Pro Max", 15900.0)

conexao.close()