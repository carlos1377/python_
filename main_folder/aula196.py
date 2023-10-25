from threading import Thread
from time import sleep
from threading import Lock


class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)


# t1 = MeuThread('Thread 1', 5)
# t1.start()

# t2 = MeuThread('Thread 2', 3)
# t2.start()

# t3 = MeuThread('Thread 3', 2)
# t3.start()

# for i in range(20):
#     print(i)
#     sleep(1)


def demorar_(texto, tempo):
    sleep(tempo)
    print(texto)


# t1 = Thread(target=demorar_, args=('heeello', 10))
# t1.start()

# t2 = Thread(target=demorar_, args=('heeello 2', 2))
# t2.start()

# t3 = Thread(target=demorar_, args=('heeello 3', 4))
# t3.start()
# t3.join()

# for i in range(10):
#     print(i)
#     sleep(.5)

# while t1.is_alive():
#     print('waiting thread')
#     sleep(2)


class Ingresso:
    def __init__(self, estoque: int) -> None:
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade: int):
        self.lock.acquire()

        if self.estoque < quantidade:
            print('Estamos sem ingressos')
            self.lock.release()
            return
        sleep(1)

        self.estoque -= quantidade
        print(
            f'Você comprou {quantidade} ingressos, ainda temos {self.estoque}')

        self.lock.release()


if __name__ == '__main__':
    ingressos = Ingresso(10)
    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()
    print(ingressos.estoque)
