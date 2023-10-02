# métodos em instâncias de classes Python
# hard coded -> algo escrito diretamente no código


class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} esta acelerando...')


string = 'carlos'
print(string.upper())

fusca = Carro('fusca')

celta = Carro('celta')

print(fusca.nome)
print(celta.nome)
fusca.acelerar()
celta.acelerar()
