# csv.writer e csv.DictWriter para escrever em CSV
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula180.csv'

lista_clientes = [
    {'Nome': 'Carlos', 'Endereço': 'Av 1, 22'},
    {'Nome': 'Eduardo', 'Endereço': 'Rua 2, 1'},
    {'Nome': 'João', 'Endereço': 'Av B, 3A'},
]


with open(CAMINHO_CSV, 'w', encoding='utf8') as file:
    colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(file, fieldnames=colunas)
    escritor.writeheader()

    for cliente in lista_clientes:
        escritor.writerow(cliente)

# lista_clientes = [
#     ['Carlos', 'Av 1, 22'],
#     ['Eduardo', 'Rua 2, 1'],
#     ['João', 'Av B, 3A']
# ]


# with open(CAMINHO_CSV, 'w', encoding='utf8') as file:
#     # colunas = lista_clientes[0].keys()
#     colunas = ['Nome', 'Endereço']
#     escritor = csv.writer(file)
#     escritor.writerow(colunas)

#     for cliente in lista_clientes:
#         # escritor.writerow(cliente.values())
#         escritor.writerow(cliente)
