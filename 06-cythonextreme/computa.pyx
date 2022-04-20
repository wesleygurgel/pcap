import math


def computar(fim, inicio=1):
    pos = inicio
    fator = 1000 ** 2
    while pos < fim:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))