"""
Listas de listas e seus indíces
"""
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', [0, 1, 2, 3, 4]],  # 2
]

# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][2])

for sala in salas:
    for item in sala:
        print(item)
