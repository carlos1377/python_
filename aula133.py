# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.

from functools import partial


class Foo:
    def __init__(self):
        self.public = 'isso é publico'
        self._protected = 'isso é protegido'
        self.__privado = 'isso é private'

    def metodo_publico(self):
        self._metodo_protected()
        print(self._protected)
        return 'metodo publico'

    def _metodo_protected(self):
        return '_metodo_protected'

    def __metodo_privado(self):
        print('__metodo_private')
        return '__metodo_private'


f = Foo()
# print(f.public)
# print(f.metodo_publico())
# print(f.__metodo_privado())
