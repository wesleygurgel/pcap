import threading
import time


def main():
    th = threading.Thread(target=contar, args=('elefante', 10))
    th.start()  # adicionar a pool de threads
    print('Podemos fazer outras coisas no programa enquanto a thread vai ficar executando!@')
    print('Wesley Gurgel ' * 2)

    th.join()  # Aguardando aqui a thread terminar a execução.

    print('PRONTO!')


def contar(animal, quantidade):
    for n in range(1, quantidade + 1):
        print(f' {n} {animal}(s)...')
        time.sleep(1)


if __name__ == '__main__':
    main()
