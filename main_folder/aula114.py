# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm
import sys

sys.setrecursionlimit(1005)


def fatorial(num):
    if num <= 1:
        return 1
    return num * fatorial(num-1)


# print(fatorial(5))

def recursiva(inicio=0, fim=10):
    print(inicio, fim)
    if inicio >= fim:
        return fim
    inicio += 1
    return recursiva(inicio, fim)


print(recursiva(0, 1000))

print(fatorial(5))
