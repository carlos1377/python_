SECRET = 'abelha'

letras_acertadas = ''
word_sct = '*' * len(SECRET)


while True:
    letra = input(str('Digite uma letra: '))

    if len(letra) > 1:
        print('Você digitou mais de uma letra.')
        continue

    if letra in SECRET:
        letras_acertadas += letra
    for letter in SECRET:
        if letter in letras_acertadas:
            print(letras_acertadas)
        else:
            print('*')
