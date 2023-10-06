"""
args - Argumentos não nomeados
* - *args (empacotamento de desempacotamento)
"""

x, y, *resto = 1, 2, 3, 4
print(x, y, resto)


# def soma(x, y):
#     return x + y


def soma2(*args):
    total = 0
    for numero in args:
        total += numero
    return total


some = soma2(1, 2, 3, 4, 5, 6)
print(some)

some121 = soma2(5, 9, 8, 44)
print(some121)


numeros = 1, 5, 9, 70, 584445

print(sum(numeros))
print(soma2(*numeros))  # desempacotamento de argumentos
