#Crie uma função contar_palavras(texto: str) -> int 
#que recebe uma string e retorna quantas palavras ela tem.
#Dica: strings têm um método .split() que quebra o texto em palavras

texto = "Eu quero muito me tornar um Engenheiro de Dados, e no futuro ser um Engenheiro de IA incrível, igualzinho o Tony Stark!"

def contar_palavras(texto:str) -> int:
    contagem_palavras_texto = texto.split()
    palavras_contadas = len(contagem_palavras_texto)
    return 
print(contar_palavras(texto))    
