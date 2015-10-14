import time
import winsound
from multiprocessing import Process, Event, Lock

from pyemotiv import Epoc

from pyfob import Fob

WINL = 50


def emotiv(e, l):
    epoc = Epoc()
    fid = open('emotiv.dat', 'w')
    e.wait()

    t0 = time.time()
    tp = time.time()
    while tp - t0 < WINL:
        tp = time.time()
        data = epoc.get_raw()
        m, n = data.shape
        for i in range(n):
            fid.write(
                "%8.12f %8.12f %8.12f %8.12f %8.12f %8.12f %8.12f %8.12f %8.12f %8.12f %8.12f %8.12f %8.12f %8.12f\n" % tuple(
                    data[:, i]))

    fid.close()


def ascension(e, l):
    fob = Fob()
    fid = open('fob.dat', 'w')
    e.set()

    t0 = time.time()
    tp = time.time()

    while time.time() - t0 < WINL:
        ti = time.time()
        if ti - tp >= (0.0075):
            tp = time.time()
            x, y, z, roll, pitch, yaw = fob.get_posang()
            fid.write("%8.3f %8.3f %8.3f %8.3f %8.3f %8.3f %8.3f\n" % (tp - t0, x, y, z, roll, pitch, yaw))
    fid.close()
    fob.close()


if __name__ == '__main__':
    Freq = 2500
    Dur = 2000

    event = Event()
    lock = Lock()
    p1 = Process(target=emotiv, args=(event, lock,))
    p2 = Process(target=ascension, args=(event, lock,))
    p1.start()
    p2.start()

    event.wait()

    t0 = time.time()
    while time.time() - t0 < WINL:
        winsound.Beep(Freq, Dur)
        time.sleep(8)
