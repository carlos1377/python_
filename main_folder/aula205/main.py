import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# DELETE SEM WHERE NA TABELA

cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

connection.commit()

cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

# CRIA A TABELA
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)

connection.commit()

# REGISTRAR VALORES NA TABELA
# sql = (
#     f'INSERT INTO {TABLE_NAME} (name, weight) '
#     'VALUES '
#     '(?, ?)'
# )
sql = (
    f'INSERT INTO {TABLE_NAME} (name, weight) '
    'VALUES '
    '(:nome, :peso)'
)
# cursor.execute(sql, ['Joana', 4])'
# cursor.executemany(sql, [('Joana', 22), ('carlos', 80.9)])
cursor.execute(sql, {'nome': 'Olavo', 'peso': 87})

connection.commit()

cursor.executemany(sql, (
    {'nome': 'carlos', 'peso': 87},
    {'nome': 'Maria', 'peso': 13},
    {'nome': 'eduardo', 'peso': 48},
    {'nome': 'Rogeria', 'peso': 150},
))

connection.commit()
if __name__ == '__main__':

    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id = 3'
    )
    
    connection.commit()

    cursor.execute(
        f'UPDATE {TABLE_NAME} '
        'SET name="someone", weight=68.90 '
        'WHERE id = 2'
    )
    
    connection.commit()

    cursor.execute(
        f'SELECT * FROM {TABLE_NAME}'
    )

    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight)


    cursor.close()
    connection.close()
