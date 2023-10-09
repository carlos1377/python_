# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)

class MeuError(Exception):
    pass


class OutroError(Exception):
    pass


def levantar():
    exception_ = MeuError('a', 'b', 'c')
    exception_.add_note('olha a nota 1 do erro')
    exception_.add_note('errroouuuu')
    raise exception_


try:
    # 1/0
    levantar()
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error)
    exception_ = OutroError('vou dar erro denovo')
    exception_.add_note('mais uma nota')
    exception_.__notes__ += error.__notes__.copy()
    raise exception_ from error
