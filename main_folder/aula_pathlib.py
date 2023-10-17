from pathlib import Path

caminho_projeto = Path()

# print(caminho_projeto.absolute())  # retorna o caminho absoluto

caminho_arquivo = Path(__file__)

# print(caminho_arquivo)
new_folder = caminho_arquivo.parent.parent / 'novo'

# print(new_folder / 'arquivo.txt')

caminho_file = Path.home() / 'Desktop' / 'teste.txt'
caminho_file.touch()
caminho_file.write_text('')
with caminho_file.open('a+') as file:
    file.write('one line\n')
    file.write('two line\n')
    file.write('three line\n')

print(caminho_file.read_text())
# file.touch()

# file.write_text('hello woooooo')
# print(file.read_text())
# file.unlink()


caminho_pasta = Path.home() / 'Desktop' / 'toppers'

caminho_pasta.mkdir(exist_ok=True)

subpasta = caminho_pasta / 'subpasta'

subpasta.mkdir(exist_ok=True)

outro_file = subpasta / 'arquivo.txt'

outro_file.touch()

outro_file.write_text('heeey')

# caminho_pasta.rmdir()

files = caminho_pasta / 'files'
files.mkdir(exist_ok=True)

for i in range(10):
    file = files / f'file_{i}.txt'

    if file.exists():
        file.unlink
    else:
        file.touch()

    with file.open('a+') as text_file:
        text_file.write('helnseo \n')
        text_file.write(f'file_{i}.txt')


def rmtree(root: Path, remove_root=True):
    for file in root.glob('*'):
        if file.is_dir():
            rmtree(file, False)
            file.rmdir()
        else:
            file.unlink()
    if remove_root:
        root.rmdir()


rmtree(caminho_pasta)
