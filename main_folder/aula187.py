# sys.argv - Executando arquivos com argumentos no sistema
# Fonte = Fira Code
import sys

argumentos = sys.argv
qtd_argumentos = len(argumentos)

print(qtd_argumentos)

if qtd_argumentos <= 1:
    print('você não passou argumentos')
else:
    print(f'você passou {qtd_argumentos}, sendo eles {argumentos[1:]}')
