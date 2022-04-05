import threading
import time


def main():
    threads = [
        threading.Thread(target=contar, args=('elefante', 10)),
        threading.Thread(target=contar, args=('buraco', 8)),
        threading.Thread(target=contar, args=('dinheiro', 23)),
        threading.Thread(target=contar, args=('pato', 12)),
    ]

    [th.start() for th in threads]  # adicionar a pool de threads
    print('Podemos fazer outras coisas no programa enquanto a thread vai ficar executando!@')
    print('Wesley Gurgel ' * 2)

    [th.join() for th in threads]  # Aguardando aqui a thread terminar a execução.

    print('PRONTO!')


def contar(coisa, quantidade):
    for n in range(1, quantidade + 1):
        print(f' {n} {coisa}(s)...')
        time.sleep(1)


if __name__ == '__main__':
    main()
