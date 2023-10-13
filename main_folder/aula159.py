# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass, asdict, astuple


# @dataclass(init=False)  # desabilita o init padrao da dataclass
# class Pessoa:
#     nome: str
#     sobrenome: str
#     # idade: int

#     def __init__(self, nome, sobrenome) -> None:
#         self.nome = nome
#         self.sobrenome = sobrenome
#         self.nome_completo = f'{self.nome} {self.sobrenome}'

#     def __post_init__(self):
#         print('post init')

#     # @property
#     # def nome_completo(self):
#     #     return f'{self.nome} {self.sobrenome}'

#     # @nome_completo.setter
#     # def nome_completo(self, valor: str):
#     #     nome, *sobrenome = valor.split()
#     #     self.nome = nome
#     #     self.sobrenome = ' '.join(sobrenome)


# if __name__ == '__main__':
#     p1 = Pessoa('carlos', 'eduardo')
#     p1.nome_completo = 'carlos eduardo orso'
#     print(p1)
#     print(p1.nome_completo)


# init, frozen, repr, order

@dataclass(frozen=True, repr=True, order=False)
class Pessoa:
    nome: str
    sobrenome: str


if __name__ == '__main__':
    p1 = Pessoa('carlos', 'orso')
    lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X')]
    ordenadas = sorted(lista, reverse=True, key=lambda p: p.sobrenome)
    # print(ordenadas)
    # print(p1)
    print(astuple(p1))
    print(asdict(p1))
