import multiprocessing
import time


def sing(p1):
    while True:
        print("%s:i'm singing..."%p1)
        time.sleep(5)


def dance(p2):
    while True:
        print("%s:i'm dancing..."%p2)
        time.sleep(5)


def main():
    p1 = multiprocessing.Process(target=sing, args=("p1",))
    # p2 = multiprocessing.Process(target=dance, args=("p2",))
    p1.start()
    # p2.start()
    p1.close()


if __name__ == '__main__':
    main()