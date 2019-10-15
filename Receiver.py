# this class will check whether the sender is alive
import sched
import time
import datetime
import Monitor as mon
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
        # print('init receiver')
        self.queue = q
        self.queue2 = q2
        self.s = sched.scheduler(time.time, time.sleep)
        self.pit_a_pat()

    # def __init__(self):
    # self.lastUpdatedTime = datetime

    def updateTime(self):
        print(f"{os.getpid()}: - Beat Received")
        self.lastUpdatedTime = self.queue.get()
        print(f"{os.getpid()}: - Time of last beat: {self.lastUpdatedTime}")
        self.expireTime = self.lastUpdatedTime + datetime.timedelta(seconds=5)
        print(f"{os.getpid()}: - New expire time: {self.expireTime}")
        # print(self.expireTime - self.lastUpdatedTime)

    def pit_a_pat(self):
        if not self.queue.empty():
            self.updateTime()
        self.isAlive = self.checkAlive()
        if self.checkAlive():
            self.queue2.put(True)
        else:
            self.queue2.put(False)
        # mon.Log(self.isAlive)
        self.s.enter(10, 1, self.pit_a_pat)
        self.s.run()

    def checkAlive(self):
        if datetime.datetime.now() - self.lastUpdatedTime > datetime.timedelta(seconds=self.maxWaitingTime):
            time.sleep(2)
            if datetime.datetime.now() - self.lastUpdatedTime > datetime.timedelta(seconds=self.maxWaitingTime):
                print(f"{os.getpid()}: - No beat received after expire time")
                return False
        else:
            # print(q.get());
            print(f"{os.getpid()}: - Sender is still beating")
            return True

# if __name__ == "__main__":
#     test = Receiver()
#     p2 = multiprocessing.Process(target=test.start())
#     p2.start()
#
#
