# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def multiplicacao(multiplo):
    def multiplicador(numero):
        return numero * multiplo
    return multiplicador


duplicar = multiplicacao(2)
triplicar = multiplicacao(3)
quadruplicar = multiplicacao(4)

print(duplicar(10))
print(triplicar(5))
print(quadruplicar(4))
