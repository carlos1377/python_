# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
from itertools import zip_longest
lista_a = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_b = ['BA', 'SP', 'MG', 'RJ']


def zipper(lista1, lista2):
    intervalo_maximo = min(len(lista1), len(lista2))
    return [
        (lista1[i], lista2[i]) for i in range(intervalo_maximo)
    ]


print(zipper(lista_a, lista_b))  # na mão mesmo

print(list(zip(lista_a, lista_b)))  # itera sobre a menor

# itera sobre a maior lista
print(list(zip_longest(lista_a, lista_b, fillvalue='Sem cidade')))
