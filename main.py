import time
from multiprocessing import Process, Event

from pyemotiv import Epoc

from pyfob import Fob


def Emotiv(e):
    epoc = Epoc()
    e.wait()
    t1 = time.time()
    t2 = time.time()
    i = 0
    while t2 - t1 < 20:
        t2 = time.time()
        data = epoc.get_raw()
        i = i + len(data[1])
        print 'emotiv, ', i / 128.0


def Ascension(e):
    fs = 100.0
    winl = 20.0
    fob = Fob()
    e.set()
    t0 = time.time()
    tp = time.time()

    i = 0
    while time.time() - t0 < winl:
        ti = time.time()
        if ti - tp >= (1.0 / fs):
            tp = time.time()
            fob.get_posang()
            i = i + 1
            print 'ascension, ', i / fs
    fob.close()


if __name__ == '__main__':
    event = Event()
    p1 = Process(target=Emotiv, args=(event,))
    p2 = Process(target=Ascension, args=(event,))
    p1.start()
    p2.start()
