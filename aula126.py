# __dict__ e vars para atributos de instância

class Pessoa:
    ano_atual = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


dados = {'nome': 'eduardo', 'idade': 18}
p2 = Pessoa(**dados)
p1 = Pessoa('carlos', 18)
p1.nome = 'eduardo'
print(p1.nome)
# p1.__dict__['outra'] = 'coisa'  # usando com __dict__ é editável CUIDAR
print(p1.__dict__)
print(vars(p1))
print(vars(p2))
