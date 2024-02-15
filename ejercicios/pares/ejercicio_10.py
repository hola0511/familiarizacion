numero = int(input("escriba aqui su numero:"))

def factorial(numero):
    if numero == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado


print("El factorial de", numero, "es:", factorial(numero))
