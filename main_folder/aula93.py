# Yield from

def gen1():
    yield 1
    yield 2
    yield 3


def gen2(gen=None):
    if gen is not None:
        yield from gen
    yield 4
    yield 5
    yield 6
    yield 7


g = gen2(gen1())
for numero in g:
    print(numero)
