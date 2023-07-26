"""
Iterando strings com while

"""

nome = 'carlos'

index = 0
new_name = ''
while index < len(nome):
    letra = nome[index]
    new_name += letra + '*'
    index +=1

print(new_name)