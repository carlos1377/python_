# Calculadora While


while True:

    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador do cálculo (+, -, /, *): ')

    numeros_validos = None
    try:
        float_numero_1 = float(numero_1)
        float_numero_2 = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos == None:
        print('Os números digitados são inválidos.')
        continue
    else:
        if operador == '+':
            soma = float_numero_1 + float_numero_2
            print(soma)
        elif operador == '-':
            subtracao = float_numero_1 - float_numero_2
            print(subtracao)
        elif operador == '/':
            divisao =  float_numero_1 / float_numero_2
            print(divisao)
        elif operador == '*':
            multip = float_numero_1 * float_numero_2
            print(multip)
        else:
            print('Você não digitou uma operação válida ')
            continue

    ######
    sair = input('Quer sair? [s]im: ').lower().startswith('s') # diminui possiveis erros de tipagem por conversão de str pra bool

    if sair is True:
        break


    

