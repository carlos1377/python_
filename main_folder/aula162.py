# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
from datetime import datetime
from pytz import timezone

data2 = datetime(2023, 4, 29, 10, 45, 23, tzinfo=timezone('Asia/Tokyo'))

# data = datetime.now(timezone('Asia/Tokyo'))

data = datetime.now().timestamp()  # está na base de dados

# timestamp é a quantidade de segundos no formato unix

print(datetime.fromtimestamp(data))  # lendo o numero e retornando uma data

# print(data2)
# data_str = '2023-04-29 10:45:23'
# data_str_fmt = '%Y-%m-%d %H:%M:%S'

# data = datetime.strptime(data_str, data_str_fmt)
# data = datetime(2023, 4, 29, 10, 45, 23)
# print(data)
# print(type(data))
