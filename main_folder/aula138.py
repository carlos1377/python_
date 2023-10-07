# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class Pessoa:
    cpf = '000054524965'

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print('cls pessoa')
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa):
    def falar_nome_classe(self):
        print('cls cliente')
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Aluno(Pessoa):
    cpf = '050448216541 aluno'


c1 = Cliente('carlos', 'orso')
a1 = Aluno('eduardo', 'orso')
c1.falar_nome_classe()
a1.falar_nome_classe()
print(c1.cpf)
print(a1.cpf)
