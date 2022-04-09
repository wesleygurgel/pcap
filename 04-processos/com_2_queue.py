import multiprocessing
import math
from Pessoa import Pessoa


# VANTAGEM DO QUEUE É USANDO O LOCK

def ping(queue):
    print('Comecei o PING')
    pessoas = []
    for i in range(30_000_000):
        variavel = math.sqrt(i) ** 3

    for i in range(3):
        pessoa = Pessoa(id=i)
        print(f'Criei a pessoa -> {pessoa.id}')
        pessoa.set_nome(f'Francisco da Silva {i}')
        pessoas.append(pessoa)

    queue.put(pessoas)


def pong(queue, return_dict):
    print('Comecei o PONG')
    msg = queue.get()
    print(f'Peguei a MSG -> {msg}')
    for pessoa in msg:
        pessoa.set_idade(10)
        return_dict[pessoa.id] = pessoa

    return return_dict


def main():
    queue = multiprocessing.Queue()
    manager = multiprocessing.Manager()

    return_dict = manager.dict()

    p1 = multiprocessing.Process(target=ping, args=(queue,))
    p2 = multiprocessing.Process(target=pong, args=(queue, return_dict))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f"return_dict: {return_dict}")
    print(return_dict[0].nome)


if __name__ == '__main__':
    main()
