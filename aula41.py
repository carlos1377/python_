frase = 'O Python é uma linguagem de programação multiparadgima. Python foi criado por Guido van Rossum'


i = 0

apareceu_mais_vezes = 0
letras_que_apareceu_mais_vezes = ''

while i < len(frase):

    letra_atual = frase[i]

    if letra_atual == ' ':

        i += 1
        continue

    qtd_atual = frase.count(letra_atual)

    if apareceu_mais_vezes < qtd_atual:
        apareceu_mais_vezes = qtd_atual
        letras_que_apareceu_mais_vezes = letra_atual

    print(letra_atual, qtd_atual)

    i += 1

print(

    f'A letra que apareceu mais vezes foi o "{letras_que_apareceu_mais_vezes}" que apareceu {apareceu_mais_vezes}x')
