import threading
from threading import Thread
import time 
import queue
from datetime import datetime
# from multiprocessing import Queue 

print_lock = threading.Lock()

class MyThread(threading.Thread):
    def __init__(self, queue, args=(), kwargs=None):
        threading.Thread.__init__(self,target=(), args=(), kwargs=None)
        self.queue = queue
        self.daemon = True
        self.receive_messages = args[0]

    def run(self):
        print (threading.currentThread().getName(), self.receive_messages)
        val = self.queue.get()
        self.do_thing_with_message(val)

    def do_thing_with_message(self, message):
        if self.receive_messages:
            with print_lock:
                print (threading.currentThread().getName(), "Received {}".format(message))



def printdatetime(nameprint):
    while 1:
        time.sleep(1)
        print("Currnent time is= " + str(nameprint) +" " + str(datetime.now()))

if __name__ == '__main__':

    mthread=Thread(target=printdatetime,args=(10,))
    mthread.start()
    # for i in range(2):
    #     printdatetime(i)
    while 1:
        time.sleep(1)
        print("hello threads")
    # exit()
    # testthread=threads

    



    
    # exit()
    # threads = []
    # for t in range(10):
    #     q = queue()
    #     threads.append(MyThread(q, args=(t % 2 == 0,)))
    #     threads[t].start()
    #     time.sleep(0.1)

    # for t in threads:
    #     t.queue.put("Print this!")

    # for t in threads:
    #     t.join()