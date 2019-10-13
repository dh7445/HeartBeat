#this class is where the GPS stuff will be placed
#this class is where the failure needs to occur (?) (Yes)
import sched
import time
import multiprocessing
import datetime
import random
import geocoder

class Sender:

    queue = None;

    def __init__(self, q):
        self.queue = q
        print('init sender')
        self.start()
    
    
    def locate_mycar(self):
        car_location = geocoder.ip('me')
        print("LATITUDE AND LONGTITUDE: ", car_location.latlng)
        print("CITY: ", car_location.city)
        print("STATE: ", car_location.state)
        print("COUNTRY: ", car_location.country)


    def start(self):
        # self.s = sched.scheduler(time.time, time.sleep)

        # try:
        #     rand = random.randint(1, 10)
        #     print("\n\n", rand)
        #     if 10 == rand:
        #
        # except:
        #     raise Exception('unleash hell')

        self.s = sched.scheduler(time.time, time.sleep)
        self.queue.put(datetime.datetime.now())
        # try:
        # print(5/0)
        # except:
        #     print("I crashed")

        # pit_a_pat()

        self.s.enter(1, 1, self.start)
        self.s.run()


    # test = Sender()





