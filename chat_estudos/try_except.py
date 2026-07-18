def dividir_seguro(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        return "Erro: Divisão por zero"
print(dividir_seguro(10, 2))      