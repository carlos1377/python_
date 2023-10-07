"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

import re
import sys


# cpf = input('Digite seu CPF:')\
#     .replace('.', '') \
#     .replace(' ', '') \
#     .replace('-', '')

cpf = re.sub(
    r'[^0-9]',
    '',
    input('Digite seu CPF:')
)

try:
    first_char = cpf[0]
except IndexError:
    print('Digite um CPF válido.')
    sys.exit()
repeat_first_char = cpf == cpf[0] * len(cpf)

if repeat_first_char:
    print('Você enviou dados sequenciais.')
    sys.exit()

cpf_formatado_1 = cpf[:9]

multiplicacao_cpf = 0
i = 10

for number in cpf_formatado_1:
    multiplicacao_cpf += int(number) * i
    i -= 1

primeiro_digito = (multiplicacao_cpf * 10) % 11

primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0
print(f'O primeiro digito do seu CPF é {primeiro_digito}')

cpf_formatado_2 = cpf_formatado_1 + str(primeiro_digito)


multiplicacao_cpf = 0
i = 11

for number in cpf_formatado_2:
    multiplicacao_cpf += int(number) * i
    i -= 1

segundo_digito = (multiplicacao_cpf * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0
print(f'O segundo digito do seu CPF é {segundo_digito}')

novo_cpf = f'{cpf_formatado_2}{segundo_digito}'


if cpf == novo_cpf:
    print('CPF válido')
else:
    print('CPF inválido')
