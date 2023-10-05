# Herança Múltipla - Python Orientado a Objetos
# Quer dizer que no Python, uma classe pode estender
# várias outras classes.
# Herança simples:
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Herança múltipla e mixins
# Log -> FileLog
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Cliente(Pessoa, FileLog)
#
# A, B, C, D
# D(B, C) - C(A) - B(A) - A
#
# método -> falar
#           A
#         /   \
#        B     C
#         \   /
#           D
#
# Python 3 usa C3 superclass linearization
# para gerar o mro.
# Você não precisa estudar isso (é complexo)
# https://en.wikipedia.org/wiki/C3_linearization
#
# Para saber a ordem de chamada dos métodos
# Use o método de classe Classe.mro()
# Ou o atributo __mro__ (Dunder - Double Underscore)

class A:
    def __init__(self, atributo):
        self.atributo = atributo


class B(A):
    def __init__(self, atributo, atributoB):
        super().__init__(atributo)
        self.atributoB = atributoB


class C(A):
    def __init__(self, atributo, atributoC):
        super().__init__(atributo)
        self.atributoC = atributoC


class D(B, C):
    def __init__(self, atributo, atributoB):
        super().__init__(atributo, atributoB)
