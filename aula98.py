import aula98_m

import importlib

print(aula98_m.variavel)

for i in range(10):
    importlib.reload(aula98_m)  # recarrega o módulo
    # import aula98_m #
    print(i)
