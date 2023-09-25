# dir, hasattr e getattr em Python
string = 'carlos'
metodo = 'upper'


if hasattr(string, metodo):  # testa de existe o metodo
    print('existe upper', string)
    print(getattr(string, metodo)())  # executa o metodo da variável
else:
    print('não existe o metodo')
