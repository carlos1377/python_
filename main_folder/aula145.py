# Positional-Only Parameters (/) e Keyword-Only Arguments (*)
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)
# 🟢 Positional-only Parameters (/) - Tudo antes da barra deve
# ser ❗️APENAS❗️ posicional.
# PEP 570 – Python Positional-Only Parameters
# https://peps.python.org/pep-0570/
# 🟢 Keyword-Only Arguments (*) - * sozinho ❗️NÃO SUGA❗️ valores.
# PEP 3102 – Keyword-Only Arguments
# https://peps.python.org/pep-3102/

def soma(a, y, /, x, b):  # limita os argumentos de antes da / devem ser posicional
    print(a + b + x + y)


def soma2(x, y, *, b):  # limita os argumentos de depois do * ser nomeado
    print(x + y + b)


soma(1, 2, 3, 4)
soma(1, 2, x=3, b=4)

# soma2(1, 2, 3)  erro pois b tem q ser kwarg por estar dps do *

soma2(1, 2, b=3)
