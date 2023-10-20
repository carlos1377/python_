# requests para requisição HTTP

import requests

# http -> 80
# https -> 443
url = 'http://localhost:3333/'

response = requests.get(url)

print(response.status_code)
print(response.headers)
print(response.text)
# print(response.json()) # caso retornar um json
