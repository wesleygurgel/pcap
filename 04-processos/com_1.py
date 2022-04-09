import multiprocessing
import math


def ping(conn):
    print('Comecei o PING')
    for i in range(30_000_000):
        variavel = math.sqrt(i) ** 3
    print('Enviando PING')
    conn.send({"bola": 20, "carro": 30, "feijao": 40})


def pong(conn):
    print('Comecei o PONG')
    msg = conn.recv()
    bola = msg["bola"]
    print(f'bola esta {bola}')
    carro = msg["carro"]
    print(f'carro esta {carro}')
    feijao = msg["feijao"]
    print(f'feijao esta {feijao}')


def main():
    conn1, conn2 = multiprocessing.Pipe(True)
    p1 = multiprocessing.Process(target=ping, args=(conn1,))
    p2 = multiprocessing.Process(target=pong, args=(conn2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == '__main__':
    main()
