import sched
import time
import datetime
import random
import geocoder
import os
import sys


class Sender:
    queue = None;
    maxRandom = 5

    def __init__(self, q):
        self.queue = q
        self.s = sched.scheduler(time.time, time.sleep)
        # print('init sender')
        self.start()

    def locate_mycar(self):
        car_location = geocoder.ip('me')
        # print("LATITUDE AND LONGTITUDE: ", car_location.latlng)
        # print("CITY: ", car_location.city)
        # print("STATE: ", car_location.state)
        # print("COUNTRY: ", car_location.country)
        return f"{os.getpid()}: -  Car coordinates: {car_location.latlng}. City: {car_location.city}. State: {car_location.state}." \
               f" Country: {car_location.country}"

    def start(self):
        if self.randomFault():
            try:
                5 / 0
            except:
                sys.tracebacklimit = 0
                print(f"{os.getpid()}: - Beat not sent")
                print(f"{os.getpid()} - Time of death: {datetime.datetime.now()}")
                raise

        self.queue.put(datetime.datetime.now())
        print(f"{self.locate_mycar()}")
        print(f"{os.getpid()}: - Beat sent")
        self.s.enter(5, 1, self.start)
        self.s.run()

    def randomFault(self):
        # print(self.maxRandom)
        rand1 = random.randint(1, self.maxRandom)
        print(f"{os.getpid()}: - RANDOM 1: {rand1}")
        rand2 = random.randint(1, self.maxRandom)
        print(f"{os.getpid()}: - RANDOM 2: {rand2}")
        self.maxRandom = self.maxRandom - 1
        if rand1 == rand2:
            return True
        else:
            return False
