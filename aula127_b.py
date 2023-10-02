# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

from aula127_a import PATH_FILE, Pessoa

# minha tentativa abaixo comentado

# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

#     # def salvar_json(self, caminho):
#     #     with open(caminho, 'w', encoding='utf8') as file:
#     #         dados = json.dump(
#     #             self.__dict__,
#     #             file,
#     #             ensure_ascii=False,
#     #             indent=2,
#     #         )
#     #     return dados

#     def ler_json(self, caminho):
#         with open(caminho, 'r', encoding='utf8') as file:
#             dados = json.load(file)
#         self.__dict__ = dados


# p1 = Pessoa('eduardo', 9)
# p1.ler_json('aula127.json')
# print(vars(p1))

with open(PATH_FILE, 'r', encoding='utf8') as file:
    pessoas = json.load(file)
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])

print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
