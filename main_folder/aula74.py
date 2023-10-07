"""
Closure e funções que retornam outras funções
"""


def criar_saudacao(saudacao):

    def saudar(nome):

        return f'{saudacao}, {nome}'
    return saudar


falar_bomdia = criar_saudacao('Bom dia')

falar_boanoite = criar_saudacao('Boa Noite')


print(falar_bomdia('eduardo'))


print(falar_boanoite('carlos'))

for nome in ['Maria', 'Carlos', 'Eduarda']:
    print(falar_bomdia(nome))
