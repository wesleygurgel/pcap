import multiprocessing

print(f'Iniciandoo o processo com o nome: {multiprocessing.current_process().name}')


def faz_algo(valor):
    print(f'Fazendo algo com o {valor}')


def main():
    pc = multiprocessing.Process(target=faz_algo, args=('bola',), name='Processo faz algo')
    print(f'Iniciando processo com nome: {pc.name}')
    pc.start()
    pc.join()


if __name__ == '__main__':
    main()
