entrada = input('[E]ntrar [S]air: ')
senha = input('Senha: ') or 'Sem senha'
print(senha)
senhap = '123'

if (entrada == 'E' or entrada == 'e') and senhap == senha:
    print('Entrar')
else:
    print('Sair')


print(bool(0))
print(bool(''))
print(int(0.6))
