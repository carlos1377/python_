"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40]
lista[2] = 300
# remove um indice da lista e ajusta os outros index (com listas grandes consome muito processamento)
del lista[2]
print(lista)
print(lista[2])

lista.append(50)  # adiciona um valor ao ultima item da lista
lista.pop()  # remove o ultimo item da lista
lista.append(60)
ultimo_valor = lista.pop()

print(lista, 'Removido =', ultimo_valor)
