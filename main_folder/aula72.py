# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.


def multiplicacao(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


print(1*2*3*4*5*6*7*8*9)
print(multiplicacao(1, 2, 3, 4, 5, 6, 7, 8, 9))

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.


def par_impar(x=None):
    teste = int(x) % 2
    return f'{x} é par' if teste == 0 else f'{x} é ímpar'


print(par_impar(9005))
print(par_impar(900))
