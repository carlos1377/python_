from functools import partial
from types import GeneratorType


# map - para mapear dados
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


def aumentar_percent(valor, percent):
    return round(valor * percent, 2)


aumentar_dez_percent = partial(  # faz uma closure
    aumentar_percent,
    percent=1.1
)

# novos_produtos = [
#     {**p, 'preco': aumentar_dez_percent(p['preco'])} for p in produtos
# ]


def muda_preco_produto(produto):
    return {
        **produto,
        'preco': aumentar_dez_percent(produto['preco'])
    }


novos_produtos = map(muda_preco_produto, produtos)
print_iter(novos_produtos)

novos_produtos = (x for x in produtos)
print_iter(novos_produtos)
print(isinstance(novos_produtos, GeneratorType))

novos_produtos = map(
    lambda x: x * 3,
    [1, 2, 3, 4]
)

print(list(novos_produtos))
