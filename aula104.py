# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores s'ao Syntax Sugar(Açucar Sintático)
def criar_funcao(func):
    def interna(*args, **kwargs):
        print('decorando')
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        return resultado
    return interna


@criar_funcao  # decora a função abaixo fazendo a closure automaticamente
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


invert = inverte_string('123')


print(invert)
