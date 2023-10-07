"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321

Fatiamento[i:f:p] [::]
Obs. a função len retorna a qntd de caracteres da str
"""
var = "hello"
print(len(var[2:]))
print(var[2:4])
print(var[:-3])
print(var[0:len(var):2])
print(var[::-1])
