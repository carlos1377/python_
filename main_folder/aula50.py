"""
Cuidados com tipos mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

lista = ['Luiz', 'Maria']
lista2 = lista
# lista2 = lista.copy() copia o valor da lista, sem apontar pro valor da memória

lista[0] = 'João'

print(lista2)
