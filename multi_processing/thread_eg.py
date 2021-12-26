from threading import Thread
import os
import time


def square_numbers():
    for i in range(100):
        i*i
        time.sleep(0.1)


if __name__ == "__main__":

    theads = []
    num_threads = 3


    for i in range(num_threads):
        t = Thread(target=square_numbers)
        theads.append(t)


    for t in theads:
        t.start()


    for t in theads:
        t.join()

    print('end main')
