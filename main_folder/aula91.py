# generator expression, iterables e iterators em python
import sys

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__()  # tem __iter__ e __next__

generator = (n for n in range(1000000))
lista = [n for n in range(1000000)]

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))  # não guarda o iterável na memória

# print(next(generator))

for n in generator:
    print(n)

# generator não se pode acessar indíces (len, [0], etc.)
