# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

import copy

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'sobrenome': 'miranda2',
    'sobrenome': 'miranda3',
    #    'idade' : 18

}

pessoa.setdefault('idade', 0)

print(len(pessoa))

print(pessoa['sobrenome'])  # retorna a ultima atualização da chave

# print(list(pessoa.keys()))
# print(list(pessoa.values()))
print(list(pessoa.items()))

for chave, valor in pessoa.items():
    print(chave, valor)


pessoa.setdefault('idade', 0)

print(pessoa['idade'])

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2]
}

# d2 = d1 # aponta pra varivavel

d2 = d1.copy()  # tudo que for imutável será direcionado pro d2, listas e tuplas serão apenas apontados
# d2 = copy.deepcopy(d1) # faz um cópia total da variavel


d2['c1'] = 100
d2['l1'][1] = 9999

print(d1)
print(d2)


print(pessoa.get('nome', None))

# nome = pessoa.pop('nome')
# print(nome)
# print(pessoa)

ultima_chave = pessoa.popitem()
print(pessoa)

lista = [['nome', 'carlos'], ['idade', 18.5]]

pessoa.update({
    'nome': 'novo valor',
    'idade': 18,
})
print(pessoa)
pessoa.update(lista)  # com tuplas também funciona
print(pessoa)
