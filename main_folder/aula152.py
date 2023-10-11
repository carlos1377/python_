# funções decoradoras e decoradores com classes
def meu_repr(self) -> str:
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr


def add_repr(cls):
    cls.__repr__ = meu_repr
    return cls


def meu_planeta(method):
    def internal(self, *args, **kwargs):
        resultado = method(self, *args, **kwargs)
        if 'Terra' in resultado:
            return 'Você está em casa'
        return resultado
    return internal
# class MyReprMixin:
#     def __repr__(self) -> str:
#         class_name = self.__class__.__name__
#         class_dict = self.__dict__
#         class_repr = f'{class_name}({class_dict})'
#         return class_repr


@add_repr
class Time:
    def __init__(self, nome):
        self.nome = nome


@add_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

    @meu_planeta
    def falar_nome(self):
        return f'O planeta é {self.nome}'


brasil = Time('Brasil')
portugal = Time('Portugal')
terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)
print(terra)
print(marte)

print(terra.falar_nome())
print(marte.falar_nome())
