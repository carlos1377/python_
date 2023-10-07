# decorados sao feitos para criar funções = fábrica de funções
def fact_decorators(a=None, b=None, c=None):
    # grande vantagem de ter uma fábrica de decoradores é ter acesso aos seus parametros (a, b , c) em todo escopo da função, como mostrando no aninhada()
    def fact_func(func):
        print('decoradora 1')

        def aninhada(*args, **kwargs):
            print('Parametros do decorador', a, b, c)
            print('aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fact_func


# quando o python decora a função, executa a funcao decoradora
@fact_decorators(1, 2, 4)
def soma(x, y):
    return x+y


multiplica = fact_decorators()(lambda x, y: x*y)
dez_vezes_cinco = multiplica(10, 5)
dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)
print(dez_vezes_cinco)
