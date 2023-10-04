# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero


cliente1 = Cliente('maria')
cliente2 = Cliente('carlos')

cliente1.inserir_endereco('Avenida Brasil', 484)
cliente1.inserir_endereco('Rua Marechal Deodoro', 875)

cliente1.listar_enderecos()
# quando cliente1 é apagado, os endereços também são pq fazem parte do cliente e foram criados na classe cliente
