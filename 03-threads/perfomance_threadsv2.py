import datetime
import math
import threading
import multiprocessing


def computar(fim, inicio=1):
    pos = inicio
    fator = 1000 ** 2
    while pos < fim:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))


def main():
    qtd_cores = multiprocessing.cpu_count()
    print(f'Realizando o processamento matemático com {qtd_cores} core(s).')

    inicio = datetime.datetime.now()

    threads = []
    for n in range(1, qtd_cores + 1):
        ini = 50_000_000 * (n - 1) / qtd_cores
        fim = 50_000_000 * n / qtd_cores
        print(f'Core {n} processando de {ini} até {fim}')
        threads.append(
            threading.Thread(
                target=computar,
                kwargs={'inicio': ini, 'fim': fim},
                daemon=True # Mesmo que o pai morra, os filhos continuam.
            )
        )

    [th.start() for th in threads]
    [th.join() for th in threads]

    tempo = datetime.datetime.now() - inicio
    print(f"Terminou em {tempo.total_seconds()} segundos.")


if __name__ == '__main__':
    main()

# Terminou em 7.475034 segundos. -> python_padrao
# Terminou em 5.910261 segundos. -> perfomance_threadsv2


