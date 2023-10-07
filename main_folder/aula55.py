"""
enumerate  - enumera iteráveis (índices)
"""

lista = ['Maria', 'Helena', 'Carlos']
lista.append('João')

# lista_enumerada = enumerate(lista)

# o enumerate só pode ser consumido uma vez
for indice, nome in enumerate(lista):
    print(indice, nome)
