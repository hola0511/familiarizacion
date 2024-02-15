import math

radio = eval(input("escriba el radio: "))

def calcular(radio):
    area = math.pi * radio**2
    return(area)


print(calcular(radio))
