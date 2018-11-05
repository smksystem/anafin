# this is monitoring buy  sell 
from pinkybot.packsel import packselenium
from pinkybot.buysellorder import buysellorder
import threading
from threading import Thread
import time 
from datetime import datetime
import queue
from multiprocessing import Queue

class pinkybot(packselenium):
    """docstring for firstlogin"""
    def __init__(self):
        # pass

        qorder = Queue() # To send Order request to Runtime
        qvalchange = Queue() # To monitor value change value and refresh to GUI.
        # qtkuprefresh=Queue() # To update tkinter after update refresh into database.
        # qdatarefresh=Queue() # Unuseable since missing qeue To send refresh table between GUI and Refresh button.
        # qdb=Queue()
        # xdebug or xlive
        self.mycollectqueues={"qorder":qorder,
                            "qvalchange":qvalchange,
                            # "qtkuprefresh":qtkuprefresh,
                            # "qdatarefresh":qdatarefresh,

        }
        # print(self.mycollectqueues["qorder"])
        super().__init__("xdebug")


    def myorder(self,orderside,configparams):
        if orderside=="buybyvalue":

            print (configparams)
            buyparams={ 
                    "order":"buy",
                    "stockname":configparams["stockname"].get(),
                    "startvalue":configparams["startvaluebuy"].get(),
                    "startvolume":configparams["totalvolumebuy"].get(),
                    "stockpin": configparams["stockpin"].get(),

            }
            print ("Start:buy buy buy buy buy")

            self.botbuyorder(buyparams)
            
            print ("END:buy buy buy buy buy")
        elif orderside=="sellbyvalue":
            print ("sell sell")
    # for several type of orders
    def botbuyorder(self,buyparams): 
        print("botbuyorder buy now")
        # self.qorder.put(buyparams)
        self.mycollectqueues["qorder"].put(buyparams)

    def botsellorder(self):
        print ("sell order")
    def botrtrefresh(self):
        print ("RT Refresh order monitory.py line 60")
        self.mycollectqueues["qorder"].put({"order":"refreshdb"})

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
        
        mthread=MyThread(self.mycollectqueues["qvalchange"],self.mypinkylogin,args=(LoginParams,))
        mthread.start()
        # mthread.join()

   

    def mypinkylogin(self,loginParams,qvalchange):
        # self.monitoring("test")
        # print (username)
        print (loginParams)
        # exit()

        handlewin=self.login(loginParams,self.mycollectqueues["qvalchange"],)
        # buysellorder.orderbuy(handlewin)
        

        # test here to pass thrue the handlewin


        # exit()
        # handlewin="test"
        timestamp = datetime.now()
        print("login is called")
        
        # Monitor loop here

        while True:
            i=0
            self.monitoring(handlewin,str(i))

        # while True:
        #     i=0
        #     delta=datetime.now()-timestamp
        #     if delta.seconds >= 2:
        #         print ("monitor period=" +str(delta.seconds))
        #         self.monitoring(handlewin,str(i))
        #         timestamp=datetime.now()

class MyThread(threading.Thread):
    def __init__(self, queue,fnrun, args=(), kwargs=None):
        threading.Thread.__init__(self, args=(), kwargs=None)
        self.queue = queue
        self.daemon = True
        print(args)
        self.parameter=args[0]
        self.receive_messages=args[0]
        self.fnrun=fnrun

    def run(self):
        print("start run")
        print (threading.currentThread().getName(),self.receive_messages)

        # self.queue.put("hello1",block=True)
        # self.queue.put("hello2",block=True)
        # self.queue.put("hello3",block=True)
        
        self.fnrun(self.parameter,self.queue)

        val = self.queue.get()
        # self.do_thing_with_message(val)

    def do_thing_with_message(self, message):
        if self.receive_messages:
            with print_lock:
                print (threading.currentThread().getName(), "Received {}".format(message))
