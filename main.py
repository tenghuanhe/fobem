import time
import winsound
from multiprocessing import Process, Event, Lock

from pyemotiv import Epoc

from pyfob import Fob

WINL = 300


def emotiv(e):
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
    print 'Emotiv stop...'


def ascension(e):
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

    print 'Ascension stop...'


if __name__ == '__main__':
    Freq = 2500
    Dur = 2000

    event = Event()
    p1 = Process(target=emotiv, args=(event,))
    p2 = Process(target=ascension, args=(event,))
    p1.start()
    p2.start()

    event.wait()

    idx = 0
    t0 = time.time()
    while time.time() - t0 < WINL:
        idx += 1
        print idx
        winsound.Beep(Freq, Dur)
        time.sleep(13)
