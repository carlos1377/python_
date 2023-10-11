# Context Manager com função - Criando e Usando gerenciadores de contexto
from contextlib import contextmanager


@contextmanager
def myopen(path_file, mode):
    try:
        print('opening file')
        file = open(path_file, mode, encoding='utf8')
        yield file
    except Exception as e:
        print('ocorreu erro', e)
    finally:
        print('closing file')
        file.close()


with myopen('aula150.txt', 'w') as file:
    file.write('decorator e generator')
    print('with', file)
