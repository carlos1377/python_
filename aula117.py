import json

# pessoa = {
#     'nome': 'Luiz Otávio 2',
#     'sobrenome': 'Miranda',
#     'enderecos': [
#         {'rua': 'R1', 'numero': 32},
#         {'rua': 'R2', 'numero': 55},
#     ],
#     'altura': 1.8,
#     'numeros_preferidos': (2, 4, 6, 8, 10),
#     'dev': True,
#     'nada': None,
# }

# with open('aula117.json', 'w', encoding='utf8') as file:
#     json.dump(
#         pessoa,  # dado
#         file,  # arquivo
#         ensure_ascii=False,  # usar o formatador do seu pc, ou o utf8 se usar no with open
#         indent=2  # identar
#     )

with open('aula117.json', 'r', encoding='utf8') as file:
    pessoa = json.load(file)
    print(pessoa)
