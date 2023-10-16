# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'teste novo')
NOVA_PASTA = os.path.join(DESKTOP, 'mover')

os.makedirs(NOVA_PASTA, exist_ok=True)

for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for dir_ in dirs:
        caminho_new_dir = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
        )
        os.makedirs(caminho_new_dir, exist_ok=True)
    for file_ in files:
        caminho_file = os.path.join(root, file_)
        caminho_new_file = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), file_
        )
        print(caminho_new_file)
        shutil.copy(caminho_file, caminho_new_file)
