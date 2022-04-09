import threading
import time


def processar():
    print('[', end='', flush=True)
    for _ in range(1, 11):
        print('#', end='', flush=True)
        time.sleep(1)
    print(']', end='', flush=True)


if __name__ == '__main__':
    ex = threading.Thread(target=processar)

    ex.start()
    ex.join()