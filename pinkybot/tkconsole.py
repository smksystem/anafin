
import tkinter as tk
import datetime
import sys
import time

from pinkybot.monitor import pinkybot
from pinkybot.packsel_model import PackSelModel
class outputlog(tk.Tk):
	def __init__(self):

		

		tk.Tk.__init__(self)
		self.mybot=pinkybot()
		self.title("Output Log")
		# self.resizable(0,0)
		self.geometry('780x620+20+20')

		# self.grid_columnconfigure(1, weight=1)
		# self.pack_propagate(0)
		usertxt=tk.StringVar(value="0147500")
		passtxt=tk.StringVar()
		broketxt=tk.StringVar(value="013")

		# global time1

		self.loginSet=[
						broketxt,
						usertxt,
						passtxt,
						
						]
		
		initinvest=tk.StringVar(value="10000")
		volumestep=tk.StringVar(value="100")
		profitstep=tk.StringVar(value="2")
		topvaluerange=tk.StringVar(value="4.98")
		floorvaluerange=tk.StringVar(value="4.60")
		startvaluebuy=tk.StringVar(value="4.90")
		# startvolumebuy=tk.StringVar(value="0")   # from calculate range.
		stopvaluerange=tk.StringVar(value="0.00")
		commonstep=tk.StringVar(value="0.00")  # step from range calculation
		totalcostbuy=tk.StringVar(value="0000000000")
		totalvolumebuy=tk.StringVar(value="000")
		stockname=tk.StringVar(value="dummy")
		stockpin=tk.StringVar(value="3333")
		remaininvest=tk.StringVar(value="0")

		self.configval={
			"initinvest":initinvest,
			"volumestep":volumestep,
			"profitstep":profitstep,
			"topvaluerange":topvaluerange,	
			"floorvaluerange":floorvaluerange,	
			"commonstep":commonstep,
			"startvaluebuy":startvaluebuy,
			# "startvolumebuy":startvolumebuy,
			"stopvaluerange":stopvaluerange,
			"totalcostbuy":totalcostbuy,
			"totalvolumebuy":totalvolumebuy,
			"stockname":stockname,
			"stockpin":stockpin,
			"remaininvest":remaininvest,

		}

		self.myvarasso={}








		frameOutput = tk.Frame(self, width=500, height =200,background = 'blue')
		# self.frameOutput.grid_propagate(0)
		frameOutput.grid(row=0,column=0,rowspan = 2, columnspan = 1,sticky = "n"+"s" )

		self.output = tk.Text(frameOutput,wrap='word', width=60, height=14, background = 'black', fg='white')
		# self.output.grid_propagate(0)
		self.output.grid(row=0,column=0)
		# self.output.pack(side=tk.LEFT)

		scrollbar = tk.Scrollbar(frameOutput,orient="vertical", command = self.output.yview)
		# scrollbar.grid_propagate(0)
		scrollbar.grid(row=0,column=1,sticky="n"+"s")
		# scrollbar.pack(side=tk.RIGHT, fill="y")
		self.output['yscrollcommand'] = scrollbar.set



		frameTime=tk.Frame(self,background="Blue")
		frameTime.grid(row=0,column=1,sticky="e"+"n"+"s"+"w")
		self.lablecomputetime=tk.Label(frameTime,text="time")
		self.lablecomputetime.grid(row=0,column=0)


		
		self.frameLoginRT = tk.Frame(self ,background = 'green')
		self.frameLoginRT.grid(row=1,column=1,sticky="e"+"n"+"s"+"w")
	
		labelnamebrokeid=tk.Label(self.frameLoginRT, text="Broke ID")
		labelnamebrokeid.grid(row=0,column=0)
		self.enterbrokeid=tk.Entry(self.frameLoginRT,textvariable=broketxt)
		self.enterbrokeid.grid(row=0,column=1)      




		labelnamelogin=tk.Label(self.frameLoginRT, text="Login ID")
		labelnamelogin.grid(row=1,column=0)
		self.enterloginid=tk.Entry(self.frameLoginRT,textvariable=usertxt)
		self.enterloginid.grid(row=1,column=1)

		labelnamepassword=tk.Label(self.frameLoginRT, text="Password")
		labelnamepassword.grid(row=2,column=0)
		self.enterpassword=tk.Entry(self.frameLoginRT,show="*",textvariable=passtxt)
		self.enterpassword.grid(row=2,column=1)

		labelpinpassword=tk.Label(self.frameLoginRT, text="PIN")
		labelpinpassword.grid(row=3,column=0)
		enterpin=tk.Entry(self.frameLoginRT,show="*",textvariable=stockpin)
		enterpin.grid(row=3,column=1)

		self.btnLoginRT=tk.Button(self.frameLoginRT,text="Start Login RT",command=self.executeLogin)
		self.btnLoginRT.grid(row=3,column=2 )





		frameSetValue=tk.Frame(self,background = 'blue')
		frameSetValue.grid(row=2,column=1,sticky="e"+"n"+"s"+"w")      

		labelinitialvalue=tk.Label(frameSetValue, text="Invest")
		labelinitialvalue.grid(row=1,column=0)

		self.enterInvest=tk.Entry(frameSetValue,textvariable=initinvest) #,textvariable=usertxt)
		self.enterInvest.grid(row=1,column=1)


		labelinitialvalue=tk.Label(frameSetValue, text="Volume Step")
		labelinitialvalue.grid(row=2,column=0)

		self.enterVolumn=tk.Entry(frameSetValue,textvariable=volumestep) #,textvariable=usertxt)
		self.enterVolumn.grid(row=2,column=1)

		labelinitialvalue=tk.Label(frameSetValue, text="Profit Step")
		labelinitialvalue.grid(row=3,column=0)

		enterVolumn=tk.Entry(frameSetValue,textvariable=profitstep) 
		enterVolumn.grid(row=3,column=1)


		labelinitialvalue=tk.Label(frameSetValue, text="Top Value Range")
		labelinitialvalue.grid(row=4,column=0)

		enterVolumn=tk.Entry(frameSetValue,textvariable=topvaluerange) 
		enterVolumn.grid(row=4,column=1)

		labelvaluebuy=tk.Label(frameSetValue, text="StartValueBuy")
		labelvaluebuy.grid(row=5,column=0)

		entervaluebuy=tk.Entry(frameSetValue,textvariable=startvaluebuy) 
		entervaluebuy.grid(row=5,column=1)

		labelinitialvalue=tk.Label(frameSetValue, text="Floor Value Range")
		labelinitialvalue.grid(row=6,column=0)

		enterVolumn=tk.Entry(frameSetValue,textvariable=floorvaluerange) 
		enterVolumn.grid(row=6,column=1)
		




		btnStartInitCal=tk.Button(frameSetValue,text="Set Parameters",command=self.setparameter)
		btnStartInitCal.grid(row=8,column=1 )



		# self.btnStartvaluebuy=tk.Button(frameSetValue,text="Set Value Buy",command=self.setvaluebuy,state='disabled',)
		# self.btnStartvaluebuy.grid(row=9,column=1 )

		labelvaluebuy=tk.Label(frameSetValue, text="Total Cost Buy:")
		labelvaluebuy.grid(row=8,column=0,sticky="w")

		labelvaluebuy=tk.Label(frameSetValue, textvariable=totalcostbuy)
		labelvaluebuy.grid(row=8,column=0,sticky="e")


		labelvalumebuy=tk.Label(frameSetValue, text="Total Volume Buy:")
		labelvalumebuy.grid(row=9,column=0,sticky="w")

		labelvalumebuy=tk.Label(frameSetValue, textvariable=totalvolumebuy)
		labelvalumebuy.grid(row=9,column=0,sticky="e")

		labelvalumebuy=tk.Label(frameSetValue, text="Remain Invest:")
		labelvalumebuy.grid(row=10,column=0,sticky="w")

		labelvalumebuy=tk.Label(frameSetValue, textvariable=remaininvest)
		labelvalumebuy.grid(row=10,column=0,sticky="e")
		

		framePutValue=tk.Frame(self,background = 'yellow')
		framePutValue.grid(row=3,column=1,sticky="e"+"n"+"s"+"w")      


		btnBuyCommand=tk.Button(framePutValue,text="Buy Now",command=self.buybyvalue, width = 10,height=2)
		btnBuyCommand.grid(row=0,column=0,sticky="w")

		btnSellCommand=tk.Button(framePutValue,text="Sell Now",command=self.sellbyvalue, width = 10,height=2)
		btnSellCommand.grid(row=0,column=0,sticky="e")

		btnRefreshCmd=tk.Button(framePutValue,text="Refresh",command=self.rtrefresh, width = 25,height=3)
		btnRefreshCmd.grid(row=1,column=0)





		self.canvas=tk.Canvas(self,background="black")
		self.canvas.grid(row=2,column=0,rowspan=2,sticky="nsew")


		self.frameGroupOutput = tk.Frame(self.canvas,background = 'gray')
		self.frameGroupOutput.grid(row=0,column=0) # start row 2 since text output occupied 2 rows with 0,1.

		vsbar = tk.Scrollbar(self,orient="vertical", command = self.canvas.yview)
		vsbar.grid(row=2,column=0,rowspan=2,sticky="e"+"n"+"s")
		self.canvas.configure(yscrollcommand=vsbar.set)

		hsbar = tk.Scrollbar(self,orient="horizontal", command = self.canvas.xview)
		hsbar.grid(row=4,column=0,rowspan=1,sticky="e"+"s"+"w")
		self.canvas.configure(yscrollcommand=hsbar.set)
		# scrollbar.pack(side=tk.RIGHT, fill="y")






		rangeData={
		"A":[0,1.99,0.01],  # 0 to 2 step 0.01
		"B":[2,4.98,0.02], # 2 up to less than 5  0.02
		"C":[5,9.95,0.05],
		"D":[10,24.9,0.10],
		"E":[25,99.75,0.25],
		"F":[100,199.5,0.5],
		"G":[200,399,1],
		"H":[400,1000,2],
		}
		optionList=[]
		for planName,myrange in enumerate(rangeData):
			startfrom=str(rangeData[myrange][0])
			stopfrom=str(rangeData[myrange][1])
			stepfrom=str(rangeData[myrange][2])
			# print (self.rangeData[myrange][0])
			optionList.append("Plan" + myrange +" "+ startfrom+"-"+stopfrom + " step " +stepfrom)

		self.rangeplanVar=tk.StringVar()
		self.rangeplanVar.set("Select range plan") # default choice
		self.rangeplanMenu1 = tk.OptionMenu(frameSetValue, self.rangeplanVar, *optionList,command=self.doMenuRange)
		self.rangeplanMenu1.grid(row=0,column=0,sticky="w")

		self.btnSave=tk.Button(frameSetValue,text="Save",command=self.executeSave)
		self.btnSave.grid(row=0,column=1,sticky="w")
		self.btnSave.update()

		self.btnLoad=tk.Button(frameSetValue,text="Load",command=self.executeLoad)
		self.btnLoad.grid(row=0,column=1,sticky="w",padx=self.btnSave.winfo_width())

		self.alreadyputback=False # To make put back into queue one time and sync to DB.
		self.update_idletasks()
		# self.mycount = 0
		
		# self.myvarasso["5.00"]["order"].set("buy")
		self.txtout("!!! Welcome , Please login !!!")
		self.tkclock()

	def tkclock(self):
		
		# get the current local time from the PC
		self.time2 = time.strftime('%H:%M:%S')
		# if time string has changed, update it

		# if self.time2 != time1:
			# time1 = self.time2
		self.lablecomputetime.config(text=self.time2)
		

		# calls itself every 200 milliseconds
		# to update the time display as needed
		# could use >200 ms, but display gets jerky
		self.lablecomputetime.after(200, self.tkclock)

	def executeSave(self):
		print("saveAllvalue")

	def executeLoad(self):
		print("LoadAllValue")

	def setvaluebuy(self):
		pass

	def buybyvalue(self):
		print("Buy set value")
		self.mybot.myorder("buybyvalue",self.configval)

		print ("Buy finished ")

	def sellbyvalue(self):
		print ("sell set value")	

		# self.mybot.threadorderbuy("test")
	def rtrefresh(self):
		print ("refresh button press")
		self.mybot.botrtrefresh()
		# self.mybot.myorder("rtrefresh",self.configval)


	def setparameter(self):
		print("def startcalculate here tkconsole.py line 359")

		print(self.configval["initinvest"].get())
		i=0


		initinvest=int(self.configval["initinvest"].get())
		volumestep=int(self.configval["volumestep"].get())
		profitstep=int(self.configval["profitstep"].get())
		topvaluerange=float(self.configval["topvaluerange"].get())
		floorvaluerange=float(self.configval["floorvaluerange"].get())

		startvaluebuy=float(self.configval["startvaluebuy"].get())
		commonvaluestep=float(self.configval["commonstep"].get())

		runvalue=float(startvaluebuy) # change text to numbering.
		stopvaluerange=float(topvaluerange)
		commonvaluestep=float(commonvaluestep)

		runinvest=initinvest


		runcostbuy=0 #### purpose variable to calculate in below.
		runvolumebuy=0

		while (runvalue<=stopvaluerange):				
				
			if runinvest > (runvalue*volumestep): #### check not to give -294, -xxx

				print("run value range = " + str(runvalue))
				# stepcost=round((runvalue*volumestep),2)

				##############################################################################
				###### Check padding to avoid key not found with only "4.0" not "4.00" for label
				##############################################################################
				chkpad=str(runvalue).split(".") 

				if len(chkpad[1])==1:
					tempval=chkpad[1]+"0"
					valuelabel=chkpad[0]+"." +tempval

				else:
					valuelabel=str(runvalue)
				self.labeldisplay[valuelabel][valuelabel].configure(background="lightpink")

				### skip for first phase

				# for repeatidx,label in enumerate(self.labeldisplay[valuelabel]):

				# 	# print(repeatidx,label,valuelabel)
				# 	if (label==valuelabel):
				# 		# print(repeatidx,self.labeldisplay[valuelabel][repeatidx]["orderid"])
				# 		self.labeldisplay[valuelabel][repeatidx]["orderid"].configure(background="cyan")
				# 		self.labeldisplay[valuelabel][repeatidx]["startordertime"].configure(background="yellowgreen")
				# 		self.labeldisplay[valuelabel][repeatidx]["matchordertime"].configure(background="lime")
				# 		self.labeldisplay[valuelabel][repeatidx]["matchcomplete"].configure(background="tomato")
				# 		self.labeldisplay[valuelabel][repeatidx]["volumn"].configure(background="peru")
				# 		self.labeldisplay[valuelabel][repeatidx]["orderside"].configure(background="plum")
				# 		self.labeldisplay[valuelabel][repeatidx]["state"].configure(background="gold")
				# 		self.labeldisplay[valuelabel][repeatidx]["targetvalue"].configure(background="orchid")
				# 		self.labeldisplay[valuelabel][repeatidx]["profit"].configure(background="dodgerblue")


				##############################################################################

				runcost=runvalue*volumestep
				runcostbuy +=runcost ### accume initial cost value to buy
				print("initial cost to buy =" , str(runcostbuy))
				
				runvolumebuy+=volumestep

				
				runvalue+=commonvaluestep
				runvalue=round(runvalue,2)
			

				runinvest -=runcost #### resul is 293.99999999999999994
				runinvest=round(runinvest,2)
				print (runinvest)

			elif runinvest < (runvalue*volumestep):
				print ("run invest is not enough break to exit tkconsole.py line 435")
				break


		self.configval["totalcostbuy"].set(runcostbuy)
		self.configval["totalvolumebuy"].set(runvolumebuy)
		self.configval["remaininvest"].set(runinvest)

		print ("Initial Invest ====>>" + str(initinvest))
		print ("Volume Step =====>>" + str(volumestep))
		print ("Profit Step ====>>" + str(profitstep))
		print ("Top Value Range ====>>" + str(topvaluerange))
		print ("Start Value Buy ====>>" + str(startvaluebuy))
		print ("Floor Value Range ====>>" + str(floorvaluerange))
		print ("Total Cost Buy ====>>" + str(runcostbuy))
		print ("Total Volume Buy =======>>" + str(runvolumebuy))
		print ("Remain Invest Cost =========>>" + str(runinvest))

		self.txtout("Set Invest = " + self.configval["initinvest"].get() ,"yellow","gray")
		self.txtout("Set Volume Step = " + self.configval["volumestep"].get() ,"yellow","gray")
		self.txtout("Set Profit Step = " + self.configval["profitstep"].get() ,"yellow","gray")
		self.txtout("Set Top Value Range = " + self.configval["topvaluerange"].get() ,"yellow","gray")
		self.txtout("Set Start Value Buy = " + self.configval["startvaluebuy"].get() ,"yellow","gray")
		self.txtout("Set Floor Value Range = " + self.configval["floorvaluerange"].get() ,"yellow","gray")
		self.txtout("Set Total Price to Pay = " + self.configval["totalcostbuy"].get())
		self.txtout("Set Total Volume = " + self.configval["totalvolumebuy"].get(),"white","peru")
		self.txtout("Remain Invest Cost = " + self.configval["remaininvest"].get())

		return (0)

	# def createlabelgroup(self,rowvalue,varvalue,rowidx):

	# 	# rowvalue=self.myvarasso[varvalue]

		
	# 	for repeatidx,valrepeat in enumerate(rowvalue):

	# 		self.labeldisplay[varvalue][repeatidx]={}
	# 		# if varvalue=="4.00":
	# 			# print(repeatidx,valrepeat)
	# 		# print("tkconsole.py line 553")
	# 		# print(valrepeat)
	# 		for j,varinfo in enumerate(valrepeat):

	# 			# print(varvalue,repeatidx)

	# 			if  varinfo=="orderno" or varinfo=="startordertime" or varinfo=="matchordertime"  or varinfo =="targetvalue":
	# 				# print(varinfo,j)
	# 				self.labeldisplay[varvalue][repeatidx][varinfo]=tk.Label(self.frameGroupOutput , textvariable=self.myvarasso[varvalue][repeatidx][varinfo],borderwidth=2, relief="groove",height=1)
	# 				self.labeldisplay[varvalue][repeatidx][varinfo].grid(row=rowidx,column=j+1+(int(repeatidx)*6),sticky="n"+"e"+"w",pady=5)

	# 			if  varinfo=="matchcomplete" or varinfo=="orderside" or varinfo=="volumn" or varinfo == "profit" or varinfo=="state" :
	# 				# print(varinfo,j)
	# 				self.labeldisplay[varvalue][repeatidx][varinfo]=tk.Label(self.frameGroupOutput , textvariable=self.myvarasso[varvalue][repeatidx][varinfo],borderwidth=2, relief="groove",height=1)
	# 				self.labeldisplay[varvalue][repeatidx][varinfo].grid(row=rowidx,column=j-3+(int(repeatidx)*6),sticky="s"+"e"+"w",pady=5)

	def doMenuRange(self,value):


		plansel=value.split(' ')[0]
		self.myvarasso=self.initRangeValue(plansel[-1])

		# print(self.myvarasso["4.00"])
		# exit()

		if plansel=="PlanA":
			print("planA selected")
		elif plansel=="PlanB":
			print("planB selected")
		elif plansel=="PlanC":
			print("planC selected")

		
		children = self.winfo_children()
		for child in children:
			# print (str(type(child)))
			if (str(type(child)) == "<class 'tkinter.Canvas'>") :
				child.destroy()

				self.canvas=tk.Canvas(self,background="black")
				self.canvas.grid(row=2,column=0,rowspan=2,sticky="nsew")

				self.frameGroupOutput = tk.Frame(self.canvas,background = 'gray')
				self.frameGroupOutput.grid(row=0,column=0,sticky="nsew") # start row 2 since text output occupied 2 rows with 0,1.


				self.scrollbarYGroupOutPut = tk.Scrollbar(self,orient="vertical", command = self.canvas.yview)

				self.scrollbarXGroupOutPut = tk.Scrollbar(self,orient="horizontal", command = self.canvas.xview)
				self.scrollbarYGroupOutPut.grid(row=2,column=0,rowspan=2,sticky="e"+"n"+"s")
				self.scrollbarXGroupOutPut.grid(row=4,column=0,rowspan=1,sticky="e"+"s"+"w")


				break		

		self.labeldisplay={}
		self.labeldisplay.clear()

		# list all value to print with decrease number
		runrangeNo=len(list (self.myvarasso.items()))-1 
		# print(len(list (self.myvarasso.items())))
		for rowidx,myvarvalue in enumerate(self.myvarasso):
			# print (myvarvalue)
			varvalue=list (self.myvarasso.items())[runrangeNo][0]
			# print (varvalue)
			# print (runrangeNo)
			# print ("number of i=" + str(i))
			
			# print(runrangeNo)


			# print("number of variable = " + str(len (self.labeldisplay)))

			self.labeldisplay[varvalue]={}
			self.labeldisplay[varvalue][varvalue]=tk.Label(self.frameGroupOutput, text=varvalue,borderwidth=3, relief="groove",height=3)
			self.labeldisplay[varvalue][varvalue].grid_propagate(0)
			
			self.labeldisplay[varvalue][varvalue].grid(row=rowidx,column=0,sticky="w"+"n"+"e",padx=3)

			runrangeNo-=1

		self.canvas['yscrollcommand'] = self.scrollbarYGroupOutPut.set
		self.canvas['xscrollcommand'] = self.scrollbarXGroupOutPut.set

		self.canvas.bind('<Configure>', self.on_configure)

		self.canvas.create_window((0,0), window=self.frameGroupOutput, anchor='n'+'w')

		self.canvas.update()

		self.txtout("Set Plan = " +value)		


		return

	def on_configure(self,event):
		# update scrollregion after starting 'mainloop'
		# when all widgets are in canvas
		self.canvas.configure(scrollregion=self.canvas.bbox('all'))


	def initRangeValue(self,idx):
		rangeData={
		"A":[0,2,0.01],  # 0 to 2 step 0.01
		"B":[2,4.98,0.02], # 2 up to less than 5  0.02
		"C":[5,10,0.05],
		"D":[10,25,0.10],
		"E":[25,100,0.25],
		"F":[100,200,0.5],
		"G":[200,400,1],
		"H":[400,1000,2],
		}
		series=[]
		i=rangeData[idx][0]
		while i < rangeData[idx][1]:
			chkpad=str(round(i,2)).split(".")
			# print(len(chkpad))
			if len(chkpad)==1:
				stval=str(round(i,2))+".00"
			elif len(chkpad)==2:
				tempval=chkpad[1]+"0"
				stval=chkpad[0]+"." +tempval[:2]

			series.append(stval)
			i+=rangeData[idx][2]
		
		# print ("Range step="+str(rangeData[idx][2]))
		
		# print(series)
		self.configval["commonstep"].set(str(rangeData[idx][2]))

		return self.rangeline(series)

	def createrepeatinfo(self,varvalue,repeatidx,myvarinfo):

		datenow = datetime.datetime.now().strftime("%Y-%m-%d")
		timenow = datetime.datetime.now().strftime("%H:%M:%S")

		varinfo={}
		varorderno=tk.StringVar(value="orderno")
		varstartordertime=tk.StringVar(value=timenow)
		varmatchordertime=tk.StringVar(value="matchordertime")
		varmatchcomplete=tk.StringVar(value="matchcomplete")
		varorderside=tk.StringVar(value="orderside")
		varvolume=tk.StringVar(value="volumn")
		varstatus=tk.StringVar(value="state")
		vartargetvalue=tk.StringVar(value="target")
		varprofit=tk.StringVar(value="profit")
		varsymbole=tk.StringVar(value="symbole")

		# print (myvarinfo)
		varorderno.set(myvarinfo["orderno"])
		varstartordertime.set(myvarinfo["time"])
		# varmatchordertime.set(myvarinfo["matchordertime"])
		varmatchcomplete.set (myvarinfo["matched"])
		varorderside.set(myvarinfo["side"])
		varvolume.set(myvarinfo["volume"])
		varstatus.set(myvarinfo["status"])
		# vartarget.set(myvarinfo[""])
		varsymbole.set(myvarinfo["symbole"])


		varinfo={
			"orderno":varorderno,
			"startordertime":varstartordertime,
			"matchordertime":varmatchordertime,
			"targetvalue":vartargetvalue,
			"symbole":varsymbole,

			"matchcomplete":varmatchcomplete,
			"orderside":varorderside,
			"volume":varvolume,
			"profit":varprofit,
			"state":varstatus,
		}

		
		self.labeldisplay[varvalue][repeatidx]={}
		
		backgroudcolor={
					"orderno":"cyan",
					"startordertime":"yellowgreen",
					"matchordertime":"lime",
					"targetvalue":"tomato",
					"matchcomplete":"peru",
					"orderside":"plum",
					"volume":"gold",
					"profit":"orchid",
					"state":"dodgerblue",
					"symbole":"white",
					}
		
		for j,varelement in enumerate(varinfo):

			# print(varvalue,repeatidx)
			# print(varelement)
			rowid=self.labeldisplay[varvalue][varvalue].grid_info()['row']
			
			if  varelement=="orderno" or varelement=="startordertime" or varelement=="matchordertime"  or varelement =="targetvalue" or varelement=="symbole" :

				self.labeldisplay[varvalue][repeatidx][varelement]=tk.Label(self.frameGroupOutput , textvariable=varinfo[varelement],
														borderwidth=2, relief="groove",height=1,background=backgroudcolor[varelement])

				self.labeldisplay[varvalue][repeatidx][varelement].grid(row=rowid,column=(j+1+int(repeatidx)*6),sticky="n"+"e"+"w",pady=5)

				
			if  varelement=="matchcomplete" or varelement=="orderside" or varelement=="volume" or varelement == "profit" or varelement=="state" :

				self.labeldisplay[varvalue][repeatidx][varelement]=tk.Label(self.frameGroupOutput , textvariable=varinfo[varelement],
														borderwidth=2, relief="groove",height=1,background=backgroudcolor[varelement])

				self.labeldisplay[varvalue][repeatidx][varelement].grid(row=rowid,column=(j-4+int(repeatidx)*6),sticky="s"+"e"+"w",pady=5)

		self.canvas.update()

		return varinfo

	def rangeline(self,series):

		varasso={}
		varstep={}
		
		varrepeat=[]

		for varvalue in series:

			varasso[varvalue]=[]

		return varasso

	def getRangeData(self):
		print("print rangedata")

		return self.rangeData
	def update():
		pass


	def flash(self,Label,count=0,colormode=""):

		if colormode=="green":
			# print ("select color"+colormode)
			Label.configure(foreground="white")
			Label.configure(background="lime")
			colormode=""

		bg = Label.cget('background')
		fg = Label.cget('foreground')
		Label.configure(background=fg,foreground=bg)
		count +=1
		# print ("Count="+str(count))
		if (count < 31):
			self.after(1000,self.flash,Label,count)
		elif (count>=31):
			# print ( "enter count > 31")
			Label.configure(foreground="black")
			Label.configure(background="silver")



	def txtout(self,txtmsg,colorhighlight="",backcolor=""):

			self.timenow = datetime.datetime.now()
			

			self.output.configure(state='normal')
			# print (txtmsg)

			
			# self.highlight_pattern("vol","red")

			self.output.insert(tk.END,self.timenow.strftime("%Y-%m-%d %H:%M:%S ") + str(txtmsg + "\n"))
			
			# pos = self.output.search( "Vol","1.0",stopindex="end", count=countVar)
			# print (pos)
			# self.highlight_text("Vol",txtmsg)
			# self.highlight_text("Order",txtmsg)
			# self.highlight_text("Stat",txtmsg)


			if colorhighlight != "" :
				self.highlight_text(txtmsg,colorhighlight,backcolor)
				colorhighlight=""
				backcolor=""



			self.output.configure(state='disabled')
			
			self.output.see("end")
			# self.output.tag_config("a", foreground="blue")
			# self.output.insert(contents, ("n", "a"))
	
	def executeLogin(self):

			# print("hello button Login " + self.loginSet[0].get())
			for child in self.frameLoginRT.winfo_children():
				child.configure(state='disable')
			# exit()
			self.mybot.threadlogin(self.loginSet)





			# return LoginParams
	def highlight_text(self,word,color="white",backcolor="black"):
			# word="Vol"
			txtmsg=self.output.get("1.0","end")
			# print (txtmsg)
			countVar = tk.StringVar()
			self.output.tag_config(word, background=backcolor, foreground=color)
			if txtmsg:
				pos = '1.0'
				while 1:
					pos = self.output.search( word,pos,stopindex="end", count=countVar)
					if not pos: break
					lastidx = '%s+%dc' % (pos, int(countVar.get()))
					self.output.tag_add(word, pos, lastidx)
					pos = lastidx

			# self.output.see(tk.END)
		 
	def Refresher(self):

			if not self.mybot.mycollectqueues["qvalchange"].empty():
				tempdict=self.mybot.mycollectqueues["qvalchange"].get()
				# print (tempdict)
				# print (tempdict["textout"])
				if "textout" in tempdict:
						self.txtout("value change to:" + tempdict["textout"])

				if "stockvalue" in tempdict:
						print ("stock has been updated !!!!!!!!!!!!")
						self.txtout("Value Change : " + tempdict["stockvalue"])
						lblstockvalue=tempdict["stockvalue"] # get value from queue
						if lblstockvalue in self.labeldisplay:
							self.flash(self.labeldisplay[lblstockvalue][lblstockvalue],9,"green")
				# self.mybot.myqueue.join()
				if "stockname" in tempdict:
						print ("monitor =" + tempdict["stockname"])
						self.configval["stockname"].set(tempdict["stockname"])

			if not self.mybot.mycollectqueues["qrefresh"].empty() :
				chkrefresh=self.mybot.mycollectqueues["qrefresh"].get()

				if chkrefresh["qrefresh"]=="refreshtk":
					print ("<<<<<<<< Print data to do update refresh tkinter here !!!!! tkconsole.py line 757")
					# print(chkrefresh["doupdatetk"])
					for rowupdata in chkrefresh["doupdatetk"] :
						# print("///////////////myvarasso tkconsole.py line 759")

						# print(self.myvarasso[rowupdata["price"]])


						if len(self.myvarasso[rowupdata["price"]]) == 0:

							repeatidx=len(self.myvarasso[rowupdata["price"]])
							self.myvarasso[rowupdata["price"]].append(self.createrepeatinfo(rowupdata["price"],
																			repeatidx,rowupdata))
						else:
							# check if lable already existing then no more create label 
							for chklblorderno in self.myvarasso[rowupdata["price"]] :
								# print (chklblorderno["orderno"].get())
								chkorderno=chklblorderno["orderno"].get()
								print ("tkconsole.py line 775 compare orderno=" + chkorderno,rowupdata["orderno"])
								if chkorderno == rowupdata["orderno"] :
									ignoreadd=True
									break;
								else:
									ignoreadd=False
								# else:
							if ignoreadd==False:	
								repeatidx=len(self.myvarasso[rowupdata["price"]])
								self.myvarasso[rowupdata["price"]].append(self.createrepeatinfo(rowupdata["price"],
																	repeatidx,
																	rowupdata)
																)
							elif ignoreadd==True: ### case already existing of order and need to update for parameter of realtime like status.

								print("+++++++need to update partial realtime table tkconsole.py line 790 !!!")
								# print(self.myvarasso[rowupdata["price"]])
								for varparams in self.myvarasso[rowupdata["price"]]:
									# print("print varparams tkconsole.py line 793")
									# print (varparams)
									for varrepeatkey,varrepeatvalue in varparams.items():
										# print("!!!!!!!!! show key and value of varparams tkconsole.py line 806")
										# print (varrepeatkey,varrepeatvalue.get())
										# print("show price of data tkconsole.py line 808")
										# print(rowupdata["orderno"])
										if varrepeatvalue.get()== rowupdata["orderno"] :
											# print ("********found orderno to update tkconsole.py line 811")

											varparams["orderside"].set(rowupdata["side"])
											varparams["volume"].set(rowupdata["volume"])
											varparams["matchcomplete"].set(rowupdata["matched"])
											# varparams["balance"].set(rowupdata["balance"])
											varparams["state"].set(rowupdata["status"])


					self.canvas.configure(scrollregion=self.canvas.bbox("all"))
					
				elif chkrefresh["qrefresh"]=="refreshdb":
					self.mybot.mycollectqueues["qrefresh"].put(chkrefresh)

			# if not self.mybot.mycollectqueues["qorder"].empty() :
			# 	chkorder=self.mybot.mycollectqueues["qorder"].get()
			# 	print ("chkorder tkconsole.py line 782")
			# 	print (chkorder)
			# 	if chkorder["order"]=="refreshtk":
			# 		# print (chkorder["doupdate"])
			# 		# dbtable_array=PackSelModel.tkrefreshdb()
			# 		# print(dbtable_array)

			# 		print (chkorder["doupdatetk"])

			# 		# self.alreadyputback=False
			# 	elif chkorder["order"]=="refreshdb":
			# 		print (">>>>>>>>Put refresh back DB")
			# 		###### if not refresh tkinter put queue back to refresh at db for thread.
			# 		chkorder=self.mybot.mycollectqueues["qorder"].put(chkorder)
			# 		# self.alreadyputback=True
				
			# self.output.tag_config("testb", background="white", foreground="red")
			# self.output.tag_add('testb', 10.0, step)
			self.after(5, self.Refresher) # every second...
