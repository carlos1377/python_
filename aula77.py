# Manipulando chaves e valores em dicionários

pessoa = {
}

##

chave = 'nome_completo'

pessoa[chave] = 'carlos orso'
pessoa['sobrenome'] = 'eduardo'
# print(pessoa['nome1']) # keyerror
print(pessoa[chave])

del pessoa['sobrenome']

if pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa['sobrenome'])

print(pessoa)
