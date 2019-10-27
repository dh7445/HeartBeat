import sched
import time
import datetime
import random
import geocoder
import os
import sys


class Sender:
    queue = None
    maxRandom = 5

    def __init__(self, q):
        self.queue = q
        self.s = sched.scheduler(time.time, time.sleep)
        self.start()

    def locate_mycar(self):
        car_location = geocoder.ip('me')
        return f"Sender: -  Car coordinates: {car_location.latlng}. City: {car_location.city}. State: {car_location.state}." \
               f" Country: {car_location.country}"

    def start(self):
        if self.randomFault():
            try:
                5 / 0
            except:
                sys.tracebacklimit = 0
                print(f"Sender - Time of death: {datetime.datetime.now()}")
                raise

        self.queue.put([self.locate_mycar(), datetime.datetime.now()])

        self.s.enter(5, 1, self.start)
        self.s.run()

    def randomFault(self):
        rand1 = random.randint(1, self.maxRandom)
        rand2 = random.randint(1, self.maxRandom)
        self.maxRandom = self.maxRandom - 1
        if rand1 == rand2:
            return True
        else:
            return False
