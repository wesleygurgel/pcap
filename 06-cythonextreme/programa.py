import datetime
import computa


def main():
    inicio = datetime.datetime.now()
    computa.computar(fim=50_000_000)

    tempo = datetime.datetime.now() - inicio
    print(f"Terminou em {tempo.total_seconds()} segundos.")


if __name__ == '__main__':
    main()


# Terminou em 7.475034 segundos.
#
