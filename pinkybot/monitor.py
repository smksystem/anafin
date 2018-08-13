# this is monitoring buy  sell 
from pinkybot.packsel import packselenium
from pinkybot.buysellorder import buysellorder
import threading
from threading import Thread
import time 
import queue
from multiprocessing import Queue

class pinkybot(packselenium):
    """docstring for firstlogin"""
    def __init__(self):
        pass


        


    def threadlogin(self,loginSet):
        print ("thread login was called")
        

        # from pinkybot.monitor import pinkybot
        LoginParams={
          "mybrokeId":loginSet[0].get(),
          "myuser":loginSet[1].get(),
          "mypassword":loginSet[2].get(),
          }
        print (LoginParams)
        # self.mypinkylogin(LoginParams)
        q = Queue()
        mthread=MyThread(q,self,args=(LoginParams,))
        mthread.start()



    def mypinkylogin(self,loginParams):
        # self.monitoring("test")
        # print (username)
        print (loginParams)
        # exit()

        handlewin=self.login(loginParams)
        # buysellorder.orderbuy(handlewin)
        

        # test here to pass thrue the handlewin


        # exit()
        # handlewin="test"
        print("login is called")
        while True:
            i=0
            for i in range(0,10):

                self.monitoring(handlewin,str(i))

class MyThread(threading.Thread):
    def __init__(self, queue,fnrun, args=(), kwargs=None):
        threading.Thread.__init__(self, args=(), kwargs=None)
        self.queue = queue
        self.daemon = True
        print(args)
        self.parameter=args[0]
        # self.receive_messages = args[0]
        self.fnrun=fnrun

    def run(self):
        print("start run")
        # print (threading.currentThread().getName(), self.receive_messages)
        
        self.fnrun.mypinkylogin(self.parameter)

        val = self.queue.get()
        self.do_thing_with_message(val)

    def do_thing_with_message(self, message):
        if self.receive_messages:
            with print_lock:
                print (threading.currentThread().getName(), "Received {}".format(message))
