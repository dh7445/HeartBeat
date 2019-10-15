# this class will function as a log
import sched, time, os
def Log(queue):

    if queue.get():
        print(f"{os.getpid()}: - Sender is alive!")
    else:
        print(f"{os.getpid()}: - Sender is dead :(")
    s = sched.scheduler(time.time, time.sleep)
    s.enter(15, 1, Log(queue))
    s.run()
