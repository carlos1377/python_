# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import pymysql
import dotenv
import os

dotenv.load_dotenv()

TABLE_NAME = 'customers'

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4',
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id)'
            ') '
        )
        # LIMPA A TABELA
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUES (%s, %s) '
        )
        data = ('carlos', 20)
        cursor.execute(sql, data)
        print(sql)
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUES (%(name)s, %(age)s) '
        )
        data2 = {
            "age": 28,
            "name": "eduardo",
        }
        cursor.execute(sql, data2)
        print(sql)
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUES (%(name)s, %(age)s) '
        )
        data3 = (
            {"name": "sophia", "age": 14, },
            {"name": "manu", "age": 15, },
            {"name": "carlinhos", "age": 16, },
        )
        cursor.executemany(sql, data3)
        print(sql)
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUES (%s, %s) '
        )
        data4 = (
            ("dudu", 14, ),
            ("malu", 15, ),
            ("betinha", 16, ),
        )
        cursor.executemany(sql, data4)
        print(sql)
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'SELECT * FROM {TABLE_NAME}'
            ''
        )
        cursor.execute(sql)

        # data5 = cursor.fetchone()
        data5 = cursor.fetchall()
        for row in data5:
            _id, nome, idade = row
            # print(idade, _id, nome)

    with connection.cursor() as cursor:
        # id_menor = int(input('digite o menor id: '))
        # id_maior = int(input('digite o maior id: '))
        id_menor = 3
        id_maior = 6
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE id BETWEEN %s AND %s '
        )

        cursor.execute(sql, (id_menor, id_maior))
        # print(cursor.mogrify(sql, (id_menor, id_maior)))

        # data6 = cursor.fetchall()
        # for row in data6:
        #     print(row)

    with connection.cursor() as cursor:
        sql = (
            f'DELETE FROM {TABLE_NAME} '
            'WHERE id = %s '
        )

        cursor.execute(sql, (1,))
        connection.commit()

        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')
        data7 = cursor.fetchall()

        # for row in data7:
        #     print(row)

    with connection.cursor() as cursor:
        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET nome  = %s, idade=%s '
            'WHERE id = %s '
        )

        cursor.execute(sql, ('topzera', 45, 4,))
        connection.commit()

        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')
        data7 = cursor.fetchall()

        for row in data7:
            print(row)
# cursor.close()
# connection.close()
