# from sys import path

#  https://stackoverflow.com/questions/2386714/why-is-import-bad

# # import aula99_package.modulo # -> aula99_package.modulo.soma_do_modulo()
# # só vai retornar oque estiver no __all__ do moduçp
# from aula99_package.modulo import *
# from aula99_package.modulo import soma_do_modulo

# # print(*path, sep='\n')
# print(soma_do_modulo(3, 7))
# from aula99_package.modulo import soma_do_modulo, fala_oi
# print(__name__)
# print(soma_do_modulo(8, 7))
# fala_oi()

# import aula99_package
from aula99_package import soma_do_modulo, fala_oi


# print(aula99_package.dobra(3))
print(soma_do_modulo(8, 7))
fala_oi()
