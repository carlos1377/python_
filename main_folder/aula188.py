# argparse.ArgumentParser para argumentos mais complexos
# Tutorial Oficial:
# https://docs.python.org/pt-br/3/howto/argparse.html
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-b', '--basic',
    help='mostra olá mundo na tela',
    # type=str, tipo do argumento
    metavar='STRING',
    # default='olá mundo', # valor padrão do argumento
    required=False,
    action='append',  # recebe o arguento mais de uma vez
    # nargs='+' # recebe mais de um valor no argumento
)

parser.add_argument(
    '-v', '--verbose',
    help='mostra logs',
    action="store_true"
)

args = parser.parse_args()


if args.basic is None:
    print('Voce não passou o valor de Basic')
    print(args.basic)
else:
    print('o valor de basic:', args.basic)


print(args.verbose)
