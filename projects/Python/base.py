# Vaticano - Enzo Schitini


print("-----------------------------------------------------")
print("Bem vindo :)")
p = 1
print("-----------------------------------------------------")

# Programas:

#############################################################
#############################################################

def programa1():
 def encontrar_numeros_repetidos(lista):
    contador = {}
    numeros_repetidos = []

    for numero in lista:
        if numero in contador:
            contador[numero] += 1
        else:
            contador[numero] = 1

    for numero, ocorrencias in contador.items():
        if ocorrencias > 1:
            numeros_repetidos.append(numero)

    return numeros_repetidos

 # Exemplo de uso
 lista = [1, 2, 3, 4, 5, 2, 3, 4, 7, 8, 9, 1, 2]
 numeros_repetidos = encontrar_numeros_repetidos(lista)
 print(numeros_repetidos)

# Funções:

#############################################################
#############################################################

if p == 1:
    programa1()
elif p == 2:
    print("Ok")
else:
    print("Erro!")