# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2
from pathlib import Path

from PyPDF2 import PdfReader, PdfWriter, PdfMerger

ROOT_FOLDER = Path(__file__).parent
ORIGINAL_FOLDER = ROOT_FOLDER / 'original_pdf'
NEW_FOLDER = ROOT_FOLDER / 'news_pdf'

RELATORIO_BACEN = ORIGINAL_FOLDER / 'R20231020.pdf'
NEW_FOLDER.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_BACEN)
# print(len(reader.pages))
# for page in reader.pages:
#     print(page)

page0 = reader.pages[0]
image0 = page0.images[0]
# print(page0.extract_text())
# with open(NEW_FOLDER / image0.name, 'wb') as img:
#     img.write(image0.data)


for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(NEW_FOLDER / f'page{i}.pdf', 'wb') as fp:
        writer.add_page(page)
        writer.write(fp)

merger = PdfMerger()
files = [
    NEW_FOLDER / 'page1.pdf',
    NEW_FOLDER / 'page0.pdf',
]

for file in files:
    merger.append(file)  # type: ignore

merger.write(NEW_FOLDER / 'merged.pdf')
merger.close()
