# this class will function as a log
import sched, time, os


def Log(queue, queue2):

    main_queue = queue.get()
    backup_queue = queue2.get()


    if main_queue[1] == True:
        print(f"Monitor: - {main_queue[0]} - {main_queue[2]}")
    else:
        print(f"Monitor: - {main_queue[0]} - died.")
        # main_queue = queue.get()
        if len(main_queue) > 2:
            print(f"Monitor: - {backup_queue[0]} - {backup_queue[2]}")
    # while not queue.empty():
    #     queue.get()

    s = sched.scheduler(time.time, time.sleep)
    s.enter(10, 1, Log(queue, queue2))
    s.run()
