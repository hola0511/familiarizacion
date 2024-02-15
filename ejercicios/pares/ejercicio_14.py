numeros = [20, 40, 60, 80, 100]

def aritmetica(lista):
    if len(lista) == 0:
        return 0
    suma = sum(lista)
    media = suma / len(lista)
    return media


print("La media aritmética de la lista es:", aritmetica(numeros))
