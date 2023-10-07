# try, except, else e finally
try:
    print('arquivo aberto')
    8/0
except ZeroDivisionError as error:
    print('dividiu por zero')
    print(f'{error.__class__.__name__=}, {error}')
else:
    print('não deu erro')
finally:
    print('fechar arquivo')

# raise - lançdando exceções(erros)


def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero')
    return True


def deve_ser_int_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'{n} deve ser int ou float. '
            f'"{tipo_n.__name__}" enviado'
        )


def divide(n, d):  # a função não deve tratar as exceções, pois o papel dela é apenas receber dois numeros e dividi-los
    deve_ser_int_float(n)
    deve_ser_int_float(d)
    nao_aceito_zero(d)
    return n / d


print(divide(8, '0'))
