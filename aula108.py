from itertools import zip_longest


def somar_duas_listas(lista1, lista2):
    intervalo = min(len(lista1), len(lista2))
    return [
        (lista1[i] + lista2[i]) for i in range(intervalo)
    ]


l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [1, 2, 3, 4]

print(somar_duas_listas(l1, l2))

lista_soma = [
    x + y for x, y in zip(l1, l2)
]

print(lista_soma)

lista_soma_maior = [
    x + y for x, y in zip_longest(l1, l2, fillvalue=0)
]
print(lista_soma_maior)
