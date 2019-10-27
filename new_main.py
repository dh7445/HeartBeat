import multiprocessing
import Sender
import Receiver
import Monitor
import Backup.Sender_backup
import Backup.Receiver_backup


if __name__ == "__main__":

    #Queues
    q = multiprocessing.Queue()
    q_backup = multiprocessing.Queue()
    q_monitor = multiprocessing.Queue()
    q_monitor2 = multiprocessing.Queue()


    #first group
    p1 = multiprocessing.Process(target=Sender.Sender, args=(q,), name="Main sender")
    p2 = multiprocessing.Process(target=Receiver.Receiver, args=(q, q_monitor,), name='Main receiver')

    #backup group
    p1_b = multiprocessing.Process(target=Backup.Sender_backup.Sender, args=(q_backup,), name="Backup sender")
    p2_b = multiprocessing.Process(target=Backup.Receiver_backup.Receiver, args=(q_backup, q_monitor2,), name="Backup receiver")

    #monitor
    monitor_p = multiprocessing.Process(target=Monitor.Log, args=(q_monitor, q_monitor2))

    # print("Init Process 1  (Sender)")
    # print("Init Process 2  (Receiver)")
    # print("Init Process 3  (Monitor)")

    p1.start()
    p2.start()
    p1_b.start()
    p2_b.start()
    monitor_p.start()

    p1.join()
    p2.join()
    p1_b.join()
    p2_b.join()
    monitor_p.join()



