"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

while True:
    try:
        nint = int(input('Digite um número inteiro: '))
        if nint % 2 == 0:
            print('Você digitou um número par.')
        else:
            print('Você digitou um número ímpar.')
        break
    except:
        print('Digite um número inteiro válido!')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
while True:
    try:
        hint = int(input('Digite a Hora atual: '))
        if hint in range(0, 12):
            print('Bom dia')
        elif hint in range(12, 18):
            print('Boa tarde')
        elif hint in range(18, 24):
            print('Boa noite')
        break
    except:
        print('Digite apenas um horário válido!')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

sname = str(input('Digite seu nome: '))
tamanho_nome = len(sname)

if tamanho_nome <= 4 and tamanho_nome > 0:
    print('Seu nome é curto')
elif tamanho_nome in range(5, 7):
    print('Seu nome é normal')
elif tamanho_nome > 6:
    print('Seu nome é muito grande')
else:
    print('Digite um nome valido')
