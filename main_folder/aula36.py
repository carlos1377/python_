contador =0 

while contador < 100:
    contador += 1

    if contador == 6:
        continue  # continue quebra o loop do momento, reiniciando o loop

    print(contador)
    if contador == 40:
        break

print('Acabou')