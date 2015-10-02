import time

from pyemotiv import Epoc

from pyfob import Fob


def Emotiv():
    epoc = Epoc()
    t1 = time.time()
    t2 = time.time()

    print epoc.get_raw()


def Ascension():
    fs = 100.0
    winl = 20.0
    fob = Fob()

    t0 = time.time()
    tp = time.time()

    i = 0
    while time.time() - t0 < winl:
        ti = time.time()
        if ti - tp >= (1.0 / fs):
            tp = time.time()
            print i, fob.get_posang()
            i = i + 1
    fob.close()


if __name__ == '__main__':
    Emotiv()
