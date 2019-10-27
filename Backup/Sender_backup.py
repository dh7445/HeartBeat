import sched
import time
import datetime
import geocoder


class Sender:
    queue = None
    maxRandom = 5

    def __init__(self, q):
        self.queue = q
        self.s = sched.scheduler(time.time, time.sleep)
        self.start()

    def locate_mycar(self):
        car_location = geocoder.ip('me')
        return f"Sender Backup: -  Car coordinates: {car_location.latlng}. City: {car_location.city}. State: {car_location.state}." \
               f" Country: {car_location.country}"

    def start(self):
        self.queue.put([self.locate_mycar(), datetime.datetime.now()])
        self.s.enter(5, 1, self.start)
        self.s.run()
