# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

PATH_FILE = 'aula127.json'


class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def salvar_json(self, caminho):
        with open(caminho, 'w', encoding='utf8') as file:
            dados = json.dump(
                self.__dict__,
                file,
                ensure_ascii=False,
                indent=2,
            )
        return dados


p1 = Pessoa('carlos', 18)
p2 = Pessoa('eduardo', 42)
p3 = Pessoa('orso', 52)

bd = [vars(p1), vars(p2), vars(p3)]

# p1.salvar_json(PATH_FILE)


def json_dump(dados):
    if __name__ == '__main__':
        with open(PATH_FILE, 'w', encoding='utf8') as file:
            json.dump(dados, file, ensure_ascii=False, indent=2)
    return


json_dump(bd)
