# json.dump e json.load com arquivos
import json
import os

NOME_ARQUIVO = 'aula177.json'
ABSOLUTE_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        NOME_ARQUIVO
    )
)

movie = {
    'title': 'O Senhor dos Anéis: A Sociedade do Anel',
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring',
    'is_movie': True,
    'imdb_rating': 8.8,
    'year': 2001,
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'],
    'budget': None
}

with open(ABSOLUTE_PATH, 'w', encoding='utf8') as file:
    json.dump(movie, file, ensure_ascii=False, indent=2)

with open(ABSOLUTE_PATH, 'r', encoding='utf8') as file:
    movie_pjson = json.load(file)
    print(movie_pjson)
