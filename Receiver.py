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

    def __init__(self, q, q2):
        self.queue = q
        self.queue2 = q2
        self.s = sched.scheduler(time.time, time.sleep)
        self.pit_a_pat()

    def updateTime(self):
        print(f"{os.getpid()}: - Beat Received")
        self.lastUpdatedTime = self.queue.get()
        print(f"{os.getpid()}: - Time of last beat: {self.lastUpdatedTime}")
        self.expireTime = self.lastUpdatedTime + datetime.timedelta(seconds=5)
        print(f"{os.getpid()}: - New expire time: {self.expireTime}")

    def pit_a_pat(self):
        if not self.queue.empty():
            self.updateTime()
        self.isAlive = self.checkAlive()
        if self.checkAlive():
            self.queue2.put(True)
        else:
            self.queue2.put(False)
        self.s.enter(10, 1, self.pit_a_pat)
        self.s.run()

    def checkAlive(self):
        if datetime.datetime.now() - self.lastUpdatedTime > datetime.timedelta(seconds=self.maxWaitingTime):
            time.sleep(2)
            if datetime.datetime.now() - self.lastUpdatedTime > datetime.timedelta(seconds=self.maxWaitingTime):
                print(f"{os.getpid()}: - No beat received after expire time")
                return False
        else:
            print(f"{os.getpid()}: - Sender is still beating")
            return True
