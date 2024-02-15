numero = int(input("escriba aqui su numero:"))

def par_o_inpar(numero):
    if (numero%2==0):
        return "es par"
    else:
        return "es inpar"

print(par_o_inpar(numero))
