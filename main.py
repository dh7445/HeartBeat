import multiprocessing
from Sender import Sender
from Receiver import Receiver
import Monitor


q = multiprocessing.Queue()
q2 = multiprocessing.Queue()

p1 = multiprocessing.Process(target=Sender, args=(q,))
p2 = multiprocessing.Process(target=Receiver, args=(q, q2,))
p3 = multiprocessing.Process(target=Monitor.Log, args=(q2,))
print("Init Process 1  (Sender)")
p1.start()
print("Init Process 2  (Receiver)")
p2.start()
print("Init Process 3  (Monitor)")
p3.start()
p1.join()
p2.join()


