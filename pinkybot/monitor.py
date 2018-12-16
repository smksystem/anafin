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

	 # def __init__(self, *, plugins: list=list()):
	 #    self.internal_modules = [InternalPrinter()]
	 #    self.myplugins = plugins
	 #    print (self.myplugins)
	
	def setparameter(self,params,labeldisplay,textout):
		self.myplugins.setparameter(params,labeldisplay,textout)

	def checkparams(self,params):
		self.myplugins.checkparams(params)

	def __init__(self, *, plugins: list=list()):
		# pass
		# self.default_modules = [InternalPrinter()]
		self.myplugins = plugins[0]

		# print(self.myplugins)

		qorder = Queue() # To send Order request to Runtime
		qvalchange = Queue() # To monitor value change value and refresh to GUI.
		qrefresh = Queue()
		# qtkuprefresh=Queue() # To update tkinter after update refresh into database.
		# qdatarefresh=Queue() # Unuseable since missing qeue To send refresh table between GUI and Refresh button.
		# qdb=Queue()
		# xdebug or xlive
		self.mycollectqueues={"qorder":qorder,
							"qvalchange":qvalchange,
							"qrefresh":qrefresh, # to decrease complexsity of Queue from order.

		}
		# print(self.mycollectqueues["qorder"])

		super().__init__("xdebug") # configure xdebug or xlive


	def myorder(self,orderside,configparams):
		if orderside=="buybyclick":

			# print (configparams)
			buyparams={ 
					"ordermode":"buybyclick",
					"order":"buy",
					# "stockname":configparams["stockname"].get(),
					# "startvalue":configparams["startvaluebuy"].get(),
					# "startvolume":configparams["totalvolumebuy"].get(),
					"stockpin": configparams["stockpin"].get(),


			}
			# print ("Start:buy buy buy buy buy monitor.py line 47")

			# self.botbuyorder(buyparams)
			# print("botbuyorder buy now")
			self.mycollectqueues["qorder"].put(buyparams)
			
			print ("END:buy buy buy buy buy monitor.py line 51")

		elif orderside=="sellbyvalue":

			buyparams={ 
				"ordermode":"buybyclick",
				"order":"buy",
				"stockname":configparams["stockname"].get(),
				"startvalue":configparams["startvaluebuy"].get(),
				"startvolume":configparams["totalvolumebuy"].get(),
				"stockpin": configparams["stockpin"].get(),


			}

			self.mycollectqueues["qorder"].put(buyparams)


			print ("sell sell")
	# for several type of orders
	# def botbuyorder(self,buyparams): 
	# 	print("botbuyorder buy now")
	# 	# self.qorder.put(buyparams)
	# 	self.mycollectqueues["qorder"].put(buyparams)

	def botsellorder(self):
		print ("sell order")
	def botrtrefresh(self):
		print ("RT Refresh order monitory.py line 60")
		## get command from click button ,assign to be full refresh for all table


		# line below for real all refresh set parameter "refreshtype to be all or partial"
		self.mycollectqueues["qrefresh"].put({"qrefresh":"refreshdb","refreshtype":"all"}) 

		# self.mycollectqueues["qrefresh"].put({"qrefresh":"refreshdb","refreshtype":"partial"}) 

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
		# print (loginParams)
		# exit()

		# handlewin=self.login(loginParams,self.mycollectqueues["qvalchange"],)
		return_login,mydriver=self.login(loginParams)
		# print("return login from login result monitor.py line 135 000000000000")
		# print(return_login)
		# buysellorder.orderbuy(handlewin)
		

		# test here to pass thrue the handlewin


		# exit()
		# handlewin="test"
		timestamp = datetime.now()
		print("login is called")
		
		# Monitor loop here

		while True:
			# i=0
			self.monitoring(mydriver,return_login)


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
