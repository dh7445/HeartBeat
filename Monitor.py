#this class will function as a log
import multiprocessing
from Sender import Sender
from Receiver import Receiver


if __name__ == "__main__":
    q = multiprocessing.Queue();

    p1 = multiprocessing.Process(target=Sender, args=(q,))
    test = Receiver()
    p2 = multiprocessing.Process(target=test.checkAlive, args=(q,))
    p1.start()
    p2.start()
    # p1.join()
    print("hola")

