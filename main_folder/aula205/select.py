import sqlite3
from main import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(f'SELECT * FROM {TABLE_NAME}')  # LIMIT 2

for row in cursor.fetchall():
    # print(row)
    _id, name, weight = row
    print(_id, name, weight)
print()
# cursor.execute(f'SELECT * FROM {TABLE_NAME}')
# row = cursor.fetchone()
# print(*row)

cursor.execute(
    f'SELECT * FROM {TABLE_NAME} '
    'WHERE id = "4"'
)

row = cursor.fetchone()
print(*row)

cursor.close()
connection.close()
