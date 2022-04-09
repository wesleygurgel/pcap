import time
# from concurrent.futures.thread import ThreadPoolExecutor as Executor
from concurrent.futures.process import ProcessPoolExecutor as Executor


def processar():
    print('[', end='', flush=True)
    for _ in range(1, 11):
        print('#', end='', flush=True)
        time.sleep(1)
    print(']', end='', flush=True)

    return 'Hi felas'


if __name__ == '__main__':
    with Executor() as executor:
        ex = executor.submit(processar)

    print(f'Retorno foi de {ex.result()}')
