import ctypes
import multiprocessing


def depositar(saldo, lock):
    for _ in range(10_000):
        with lock:
            saldo.value = saldo.value + 1


def sacar(saldo, lock):
    for _ in range(10_000):
        with lock:
            saldo.value = saldo.value - 1


def realizar_transacoes(saldo, lock):
    pc1 = multiprocessing.Process(target=depositar, args=(saldo, lock))
    pc2 = multiprocessing.Process(target=sacar, args=(saldo, lock))

    pc1.start()
    pc2.start()
    pc1.join()
    pc2.join()


if __name__ == '__main__':
    saldo = multiprocessing.Value(ctypes.c_int, 100)
    print(f'SALDO INICIAL: {saldo.value}')

    lock = multiprocessing.RLock()

    for _ in range(10):
        realizar_transacoes(saldo, lock)

    print(f'Saldo Final: {saldo.value}')