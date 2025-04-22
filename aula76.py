

def criador_multiplicador(multiplicador):
    def multiplicar(numero):
        return multiplicador * numero
    return multiplicar

duplicar=criador_multiplicador(3)

print(duplicar(3))
