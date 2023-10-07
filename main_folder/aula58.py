"""

split e join com list e str

split - divide uma string em uma lista

join - une uma string


strip -  corta os espaços

lstrip - espaços da esquerda

rstrip - espaços da direita

"""


frase = '   Olha só que, coisa interessante    '

# divide a string a cada whitespace ou caractere sirecionado
lista_frases = frase.split(', ')


lista_frases_fixed = []


for i, frase in enumerate(lista_frases):

    lista_frases_fixed.append(lista_frases[i].strip())


print(lista_frases_fixed)


frases_unidas = ', '.join(lista_frases_fixed)
print(frases_unidas)
