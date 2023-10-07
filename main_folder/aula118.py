# problema dos parametros mutaveis em functios python

# def add_clientes(nome, lista=[]):
#     lista.append(nome)
#     return lista

# nao colocar parametros mutaveis em valores padroes de uma funcao python,
def add_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


lista1 = []
cliente1 = add_clientes('carlos', lista1)
add_clientes('eduardo', cliente1)
print(cliente1)

cliente2 = add_clientes('maria')
add_clientes('pops', cliente2)
print(cliente2)

cliente3 = add_clientes('joao', lista1)
add_clientes('puuuuops', cliente3)
print(cliente3)
