# introdução às generatos functions em python
# generator = (n for n in range(1000000))

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1
        if n >= maximum:
            return

    # yield 1  # pausar
    # print('continuando..')
    # yield 2  # pausar
    # print('continuando dnv..')
    # yield 3
    # print('termino')
    # return 'cabou'


gen = generator(maximum=1000000)
print(next(gen))
print(next(gen))


for n in gen:
    print(n)
