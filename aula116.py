import os
# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

path = 'C:\\rep\\python_\\'
path += 'aula116.txt'

# arquivo = open(path, 'w')

# arquivo.close()
# with open(path, 'w+') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#     )
#     arquivo.seek(0, 0)
#     print(arquivo.read())
#     print('lendo')
#     arquivo.seek(0, 0)
#     print(arquivo.readline().strip())
#     print(arquivo.readline().strip())

#     for linha in arquivo.readlines():
#         print(linha.strip())

# with open(path, 'r') as arquivo:
#     print(arquivo.read())


with open(path, 'w', encoding='utf8') as arquivo:
    arquivo.write('Atenção')

os.remove(path)
# os.rename(path, 'aula116-2.txt')
