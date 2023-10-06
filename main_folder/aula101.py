def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def executa(funcao, x):  # Aplicado Closure na função de executar, pois a função soma e multiplica tem a mesma estrutura
    def interna(y):
        return funcao(x, y)
    return interna


duplica = executa(multiplica, 2)
soma_com_5 = executa(soma, 5)

print(duplica(10))
print(soma_com_5(10))
