import multiprocessing
from Sender import Sender
from Receiver import Receiver

if __name__ == "__main__":
    q = multiprocessing.Queue();

    p1 = multiprocessing.Process(target=Sender, args=(q,))
    p2 = multiprocessing.Process(target=Receiver, args=(q,))
    p1.start()
    p2.start()
    p1.join()


