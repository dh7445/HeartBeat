#this class will function as a log
import multiprocessing



def Log(isAlive):
    if isAlive:
        print("Sender is alive!")
    else:
        print("Sender is dead :(")

