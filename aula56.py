import os

lista = []

while True:
    print('Selecione uma opção')
    operacao = input('[i]nserir [a]pagar [l]istar:')

    if operacao == 'i':
        os.system('cls')

        valor = input('Valor:')
        lista.append(valor)
    elif operacao == 'a':
        indice = input('Digite o indice a apagar: ')
        try:
            del lista[int(indice)]
        except IndexError:
            print('Não existe esse indíce na lista')
        except ValueError:
            print('Digite um índice válido')
        except Exception:
            print('Erro Desconhecido')
    elif operacao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada pra listar')

        for index, item in enumerate(lista):
            print(index, item)
    else:
        print('Esta não é uma operação válida')
