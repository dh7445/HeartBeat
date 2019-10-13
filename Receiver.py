# this class will check whether the sender is alive
import sched
import time
import datetime
import multiprocessing
import Monitor as mon


class Receiver:
    checkingTime = None
    lastUpdatedTime = datetime.datetime.now()
    checkingInterval = 10
    expireTime = None
    maxWaitingTime = 10
    queue = None
    isAlive = False

    def __init__(self, q):
        print('init receiver')
        self.queue = q
        self.pit_a_pat()


    # def __init__(self):
    # self.lastUpdatedTime = datetime

    def updateTime(self):
        self.lastUpdatedTime = self.queue.get()
        print("Time updated: ", self.lastUpdatedTime)
        self.expireTime = self.lastUpdatedTime + datetime.timedelta(seconds=5)
        print(self.expireTime - self.lastUpdatedTime)


    def pit_a_pat(self):
        print("doing stuff")
        self.updateTime()
        self.isAlive = self.checkAlive()
        print(self.isAlive)
        mon.Log(self.isAlive)
        self.s = sched.scheduler(time.time, time.sleep)
        self.s.enter(1, 2, self.pit_a_pat)
        self.s.run()

    def checkAlive(self):
        if datetime.datetime.now() - self.lastUpdatedTime > datetime.timedelta(seconds=self.maxWaitingTime):
            time.sleep(2)
            if datetime.datetime.now() - self.lastUpdatedTime > datetime.timedelta(seconds=self.maxWaitingTime):
                print("im dead")
                return False
        else:
            # print(q.get());
            print("im Alive")
            return True



    def start(self):
        self.checkAlive()
# print(datetime.datetime.now() - (datetime.datetime.now() - datetime.timedelta(seconds=5)))

#
# if __name__ == "__main__":
#     test = Receiver()
#     p2 = multiprocessing.Process(target=test.start())
#     p2.start()
#
#
