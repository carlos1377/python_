# classes decoradores (decorator classes


from typing import Any


class Multiplicar:
    # def __init__(self, func):
    #     self.func = func
    #     self._z = 10

    # def __call__(self, *args, **kwargs):
    #     resultado = self.func(*args, **kwargs)
    #     return resultado * self._z

    # uma das formas de fazer, com função interna a classe decoradora, passando o parametro quando for decorar

    def __init__(self, multiplicador):
        self._multiplicador = multiplicador

    def __call__(self, func):
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self._multiplicador
        return interna

# @Multiplicar


@Multiplicar(5)
def soma(x, y):
    return x + y


dois_plus_dois = soma(2, 2)
print(dois_plus_dois)
