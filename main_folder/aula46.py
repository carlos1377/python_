import os

SECRET = 'juliano'

letras_acertadas = ''
word_sct = '*' * len(SECRET)
num_tent = 0

while True:

    letra = input(str('Digite uma letra: '))
    num_tent += 1
    if len(letra) > 1:
        print('Você digitou mais de uma letra.')
        continue

    if letra in SECRET:
        letras_acertadas += letra

    real_word = ''
    for letter in SECRET:
        if letter in letras_acertadas:
            real_word += letter
        else:
            real_word += '*'

    print('Palavra formada:', real_word)

    if real_word == SECRET:
        os.system('cls')
        print('Você acertou.')
        print('A palavra era:', SECRET)
        print(num_tent, 'Tentativas')
        letras_acertadas = ''
        num_tent = 0
