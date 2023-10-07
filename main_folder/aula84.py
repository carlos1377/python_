# empacotamento e desempacotamento de strings
a, b = 1, 2
a, b = b, a

# print(a, b)

pessoa = {
    'nome': 'carlos',
    'sobrenome': 'orso',
}

# (a1, a2), (b1, b2) = pessoa.items()

# print(a1, a2, b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

dados_pessos = {
    'idade': 18,
    'altura': 1.83,
}

pessoa_completa = {**pessoa, **dados_pessos}

print(pessoa_completa)


# args e kwargs
# args
# kwargs - keyword arguments (argumentos nomeados)

def mostra_kwargs(*args, **kwargs):
    print('não nomeados:', args)

    for chave, item in kwargs.items():
        print(chave, item)


mostra_kwargs(1212133, nome='Joana', qlq=13213)
mostra_kwargs(**pessoa_completa)
