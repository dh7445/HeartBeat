#this class is where the GPS stuff will be placed
#this class is where the failure needs to occur (?)
import sched
import time
from Receiver import Receiver
import multiprocessing
import datetime

class Sender:

    queue = None;

    def __init__(self, q):
        self.queue = q;
        self.start()



    def start(self):
        # self.s = sched.scheduler(time.time, time.sleep)
        self.s = sched.scheduler(time.time, time.sleep)
        self.queue.put("I was sent.")
        beat = Receiver()
        beat.pit_a_pat(datetime.datetime.now())

        self.s.enter(5, 1, self.start)
        self.s.run()



    # test = Sender()





