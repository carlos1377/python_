# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import os
import json


def mostrar_todo(lista_todo):
    print()
    if not lista_todo:
        print('nada pra listar')
        print()
        return
    print('TAREFAS:')
    for tarefas in lista_todo:
        print('\t', tarefas)
    print()


def desfazer(lista_todo, todo_refaz):
    print()
    if not lista_todo:
        print('nenhuma tarefa pra desfazer')
        print()
        return
    tarefa = lista_todo.pop()
    todo_refaz.append(tarefa)
    print()


def refazer(lista_todo, todo_refaz):
    print()
    if not todo_refaz:
        print('nenhuma tarefa pra refazer')
        print()
        return
    tarefa = todo_refaz.pop()
    lista_todo.append(tarefa)
    print()


def adicionar(tarefa, lista_todo):
    print()
    if not tarefa.strip():
        print('voce nao escreveu nenhuma tarefa')
        print()
        return
    lista_todo.append(tarefa)


def ler_json(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as file:
            dados = json.load(file)
    except FileNotFoundError:
        print('arquivo não existe')
        salvar_json(tarefas, caminho_arquivo)
    return dados


def salvar_json(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as file:
        dados = json.dump(
            tarefas,  # dado
            file,  # arquivo
            ensure_ascii=False,  # usar o formatador do seu pc, ou o utf8 se usar no with open
            indent=2  # identar
        )
    return dados


PATH_FILE = 'aula119.json'
todo = ler_json([], PATH_FILE)
refazer_todo = []

while True:
    print('Comandos: listar, desfazer, refazer')
    user_inpt = str(input('Digite uma tarefa ou comando: '))
    # usando dict pra nao usar condicionais, lambda na frente das funções pra adiar a execução delas
    comandos = {
        'listar': lambda: mostrar_todo(todo),
        'desfazer': lambda: desfazer(todo, refazer_todo),
        'refazer': lambda: refazer(todo, refazer_todo),
        'clear': lambda: os.system('cls'),
        'adicionar': lambda:  adicionar(user_inpt, todo)
    }
    comando = comandos.get(user_inpt) if comandos.get(user_inpt) \
        is not None else comandos['adicionar']
    comando()
    salvar_json(todo, PATH_FILE)

    # if user_inpt == 'listar':
    #     mostrar_todo(todo)
    # elif user_inpt == 'desfazer':
    #     desfazer(todo, refazer_todo)
    #     mostrar_todo(todo)
    # elif user_inpt == 'refazer':
    #     refazer(todo, refazer_todo)
    #     mostrar_todo(todo)
    # elif user_inpt == 'clear':
    #     os.system('cls')
    # else:
    #     adicionar(user_inpt, todo)
    #     mostrar_todo(todo)
