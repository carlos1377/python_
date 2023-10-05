# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

# class MinhaString(str):
#     def upper(self):
#         print('upper')
#         return super().upper()


# string = MinhaString('oi')
# print(string.upper())


class A:
    def __init__(self, atributo):
        self.atributo = atributo

    atributo_a = 'valor a'

    def metodo(self):
        print('A')


class B(A):
    atributo_b = 'valor b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        super().metodo()
        print('B')


class C(B):
    atributo_c = 'valor c'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def metodo(self):
        super().metodo()
        print('C')


c = C('teste', 'dasdasdas')

# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)

c.metodo()
print(c.atributo)
print(c.outra_coisa)
c.metodo()
