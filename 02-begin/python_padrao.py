import datetime
import math


def computar(fim, inicio=1):
    pos = inicio
    fator = 1000 ** 2
    while pos < fim:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))


def main():
    inicio = datetime.datetime.now()
    computar(fim=50_000_000)

    tempo = datetime.datetime.now() - inicio
    print(f"Terminou em {tempo.total_seconds()} segundos.")


if __name__ == '__main__':
    main()

# Terminou em 7.475034 segundos.
