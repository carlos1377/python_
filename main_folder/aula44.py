"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o po´rximo valor
iter -> me entregue seu iterador 
"""

texto = 'carlos'  # iterável
iterator = iter(texto)  # iterator

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
