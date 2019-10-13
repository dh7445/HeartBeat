# this class will check whether the sender is alive
import sched
import time
import datetime
import multiprocessing


class Receiver:
    checkingTime = None
    lastUpdatedTime = datetime.datetime.now()
    checkingInterval = 10
    expireTime = None
    maxWaitingTime = 10

    # def __init__(self):
    #     print("do something")
    #

    # def __init__(self):
    # self.lastUpdatedTime = datetime

    def updateTime(self, newTime):
        self.lastUpdatedTime = newTime
        print("Time updated: ", self.lastUpdatedTime)
        self.expireTime = self.lastUpdatedTime + datetime.timedelta(seconds=5)
        print(self.expireTime - self.lastUpdatedTime)

    def pit_a_pat(self, newTime):
        print("doing stuff")
        self.updateTime(newTime)

    def checkAlive(self):
        if datetime.datetime.now() - self.lastUpdatedTime > datetime.timedelta(seconds=self.maxWaitingTime):
            time.sleep(2)
            if datetime.datetime.now() - self.lastUpdatedTime > datetime.timedelta(seconds=self.maxWaitingTime):
                print("im dead")
                # return False
        else:
            print("im Alive")
            # return True

        self.s = sched.scheduler(time.time, time.sleep)
        self.s.enter(5, 2, self.checkAlive)
        self.s.run()

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
