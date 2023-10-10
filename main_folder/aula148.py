# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e
# retornar o novo objeto. Por isso, new recebe cls.
# __new__ ❗️DEVE retornar o novo objeto❗️
# __init__ é o método responsável por inicializar
# a instância. Por isso, init recebe self.
# __init__ ❗️NÃO DEVE retornar nada (None)❗️
# object é a super classe de uma classe
class A:
    def __new__(cls, *args, **kwargs):  # metodo que recebe a classe e cria a instancia
        print('antes da instancia estar criada')
        instance = super().__new__(cls)
        print('depois da instancia')
        return instance

    def __init__(self):
        print('sou o init')

    def __repr__(self):
        return 'A()'


a = A()
# a = object.__new__(A)
# a.__init__()
print(a)
