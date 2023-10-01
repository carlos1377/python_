# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('carlos', 'orso')
# p1.nome = 'carlos'
# p1.sobrenome = 'orso'

p2 = Pessoa('eduardo', 'ababa')
# p2.nome = 'eduardo'
# p2.sobrenome = 'ababa'

# print(isinstance(p1, Pessoa))

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)
