#empacotamento 

dados= 1,2,3
print(dados)

# Define a função que recebe vários argumentos
def mostrar_numeros(*args):  # empacota os argumentos em uma tupla
    for numero in args:
        print(numero)

# Chama a função com vários valores
mostrar_numeros(1, 2, 3, 4)  # imprime cada número






#Desempacotamento

# Define uma função normal com 3 parâmetros
def somar(a, b, c):
    print(a + b + c)

# Cria uma lista com 3 valores
valores = [10, 20, 30]

# Chama a função desempacotando a lista
somar(*valores)  # equivalente a somar(10, 20, 30)


a,b,c=dados
print(a)
print(b)
print(c)