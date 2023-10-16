# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html
from datetime import datetime

fmt = '%d/%m/%Y'

data = datetime.strptime('2022-11-10 08:10:52', '%Y-%m-%d %H:%M:%S')

print(data.strftime(fmt))
print(data.strftime('%d/%m/%Y %H:%M'))
print(data.strftime('%Y %H:%M'))
print(type(data.strftime(fmt)))
print(type(data.year))

data = datetime.now()
print(data.strftime('%Y %H:%M'))
