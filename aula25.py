"""
formatação de strings

s - strings
f - float
d - int
x ou X - Hexadecimal
.<número de dígitos>f (.2f)
(Caractere)(><^)(Quantidade)
> - esquerda
< - direita
^ - centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel:$>10}')
print(f'{11393.20740837:+,.1f}')
print(f'o hexadecimal de 1500 é {1500:08X}')
