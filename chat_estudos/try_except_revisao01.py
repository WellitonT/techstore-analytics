#Exercício 1: Crie uma função converter_para_int(texto) que tenta converter uma string pra número inteiro 
#usando int(texto). Se não for possível (ex: int("abc")), capture o erro ValueError e retorne "Valor inválido".

def converter_para_int(texto):
    try:
        texto = int(texto)
        return texto
    except ValueError:
        return f"{texto} Valor inválido"    

print(converter_para_int("abcd"))