# this class will check whether the sender is alive
import sched
import time
import datetime
import os


class Receiver:
    checkingTime = None
    checkingInterval = 10
    expireTime = None
    maxWaitingTime = 10
    lastUpdatedTime = datetime.datetime.now()
    queue = None
    isAlive = False
    queue_array = []


    def __init__(self, q, q2):
        self.queue = q
        self.queue2 = q2
        self.s = sched.scheduler(time.time, time.sleep)
        self.pit_a_pat()

    def updateTime(self):
        self.lastUpdatedTime = self.queue_array[1]
        self.expireTime = self.lastUpdatedTime + datetime.timedelta(seconds=5)

    def pit_a_pat(self):
        if not self.queue.empty():
            self.queue_array = self.queue.get()
            self.updateTime()
        self.isAlive = self.checkAlive()
        if self.isAlive and len(self.queue_array) > 0:
            self.queue2.put(["Main Process", True, self.queue_array[0]])
        elif not self.isAlive:
            self.queue2.put(["Main Process", False])
        self.s.enter(5, 1, self.pit_a_pat)
        self.s.run()

    def checkAlive(self):
        if datetime.datetime.now() - self.lastUpdatedTime > datetime.timedelta(seconds=self.maxWaitingTime):
            time.sleep(2)
            if datetime.datetime.now() - self.lastUpdatedTime > datetime.timedelta(seconds=self.maxWaitingTime):
                print(f"Receiver: - No beat received after expire time")
                return False
        else:
            print(f"Receiver: - Sender is still beating")
            return True
