# ordem dos decoradores
def param_decorador(nome):
    def decorador(func):
        print('decorador:', nome)

        def sua_nova_funcao(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {nome}'
            return final
        return sua_nova_funcao
    return decorador


@param_decorador(nome='5')
@param_decorador(nome='4')
@param_decorador(nome='3')
@param_decorador(nome='2')
@param_decorador(nome='1')
def soma(x, y):
    return x+y


dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)
