#this class will function as a log
import multiprocessing
from Sender import Sender
from Receiver import Receiver


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=Sender)
    test = Receiver()
    p2 = multiprocessing.Process(target=test.checkAlive)
    p1.start()
    p2.start()
    # p1.join()
    print("hola")

