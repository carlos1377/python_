# Exercício - sistema de perguntas e respostas
import sys

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


def question(num_quest):
    correct = 0

    for j in range(num_quest + 1):

        for chave in perguntas[j]:

            if chave == 'Opções':
                print(chave + ':')

                for i, ops in enumerate(perguntas[j]['Opções']):
                    print(f'{i}) {ops}')
                answer = int(input('Escolha uma opção: '))

                try:
                    if perguntas[j]['Opções'][answer] == perguntas[j]['Resposta']:
                        print('Resposta correta \n')
                        correct += 1
                    else:
                        print('Resposta errada.')
                except ValueError:
                    print('Você não digitou um número.')
                    sys.exit()
                except IndexError:
                    print('Você não digitou uma opção válida.')
                    sys.exit()
                break

            print(chave + ':', perguntas[j][chave], '\n')
    print(f'Você acertou {correct} questões de {num_quest+1} \n')


question(num_quest=2)

# print(perguntas[0]['Pergunta'])
