"""
Flag (bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = identidade do valor na memória 
"""

v2 = 'a'
v1 = 'a'
print(id(v1))
print(id(v2))


condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('faça algo')
else:
    print('nao faça algo')

if passou_no_if is None:
    print('Não passou no if')

if passou_no_if is not None:
    print('Passou no if')