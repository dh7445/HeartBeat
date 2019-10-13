#this class is where the GPS stuff will be placed
#this class is where the failure needs to occur (?)
import sched
import time
import multiprocessing
import datetime
import random


class Sender:

    queue = None;
    maxRandom = 5


    def __init__(self, q):
        self.queue = q
        print('init sender')
        self.start()



    def start(self):

        try:
            if self.randomFault():
                5/0
        except:
           raise
            # self.queue.get()

        self.s = sched.scheduler(time.time, time.sleep)
        self.queue.put(datetime.datetime.now())

        #     print("I crashed")

        # pit_a_pat()

        self.s.enter(5, 1, self.start)
        self.s.run()


    def randomFault(self):
        print(self.maxRandom)
        rand1 = random.randint(1, self.maxRandom)
        print("RANDOM 1:", rand1)
        rand2 = random.randint(1, self.maxRandom)
        print("RANDOM 2:", rand2)
        self.maxRandom = self.maxRandom - 1
        if rand1 == rand2:
            return True
        else:
            return False

    # test = Sender()





