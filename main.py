import time

from multiprocessing import Process, Event, Lock

from pyemotiv import Epoc

from pyfob import Fob

winl = 20


def emotiv(e, l):
    epoc = Epoc()
    e.wait()

    t1 = time.time()

    i = 0

    while time.time() - t1 < winl:
        data = epoc.get_raw()
        i += len(data[1])
        l.acquire()
        print '                Emotiv,       ', i
        #        print time.time()
        l.release()


def ascension(e, l):
    fs = 100.0
    fob = Fob()
    e.set()

    t0 = time.time()
    tp = time.time()

    i = 0

    while time.time() - t0 < winl:
        ti = time.time()
        if ti - tp >= (0.75 / fs):
            tp = time.time()
            fob.get_posang()
            i += 1
            l.acquire()
            print 'Ascension, ', i
            #            print time.time()
            l.release()
    fob.close()


if __name__ == '__main__':
    event = Event()
    lock = Lock()
    p1 = Process(target=emotiv, args=(event, lock,))
    p2 = Process(target=ascension, args=(event, lock,))
    p1.start()
    p2.start()
