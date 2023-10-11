# método especial __call__
# callable é algo que pode ser executado com parênteses
# emc classes normais, __call__ faz a instância de uma classe "callable"

from typing import Any


class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome, *args: Any, **kwds: Any):
        print(nome, 'está chamando', self.phone)


call1 = CallMe('5458778545')
call1('carlos')
