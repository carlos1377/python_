# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class Pessoa:
    ano = 2023  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('hey')

    @classmethod
    def criar_50_anos(cls, nome):  # cls é a própria classe
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):  # cls é a própria
        return cls('Anônima', idade)


print(Pessoa.ano)
p1 = Pessoa('carlos', 19)
print(p1.nome)
Pessoa.metodo_de_classe()
p2 = Pessoa.criar_50_anos('eduard')
print(p2.idade, p2.nome)
p3 = Pessoa.criar_sem_nome(18)
print(p3.nome, p3.idade)
