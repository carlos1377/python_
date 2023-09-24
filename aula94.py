# Try, except, else e finally
a = 18
b = 0

try:
    # b[0]
    c = a / b
    print('ababa')
except ZeroDivisionError as e:
    print(e.__class__.__name__, '\n', e)
except NameError:
    print('algum valor nao esta definido')
except (TypeError, IndexError) as error:
    print(f'TypeError or IndexError \n msg = {error}')
    print(f'nome do erro = {error.__class__.__name__}')
except Exception:
    print('erro desconhecido')
