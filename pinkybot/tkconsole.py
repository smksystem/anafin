
import tkinter as tk
import datetime
import sys
from pinkybot.monitor import pinkybot

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


		self.loginSet=[
						broketxt,
						usertxt,
						passtxt,
						
						]
		
		initinvest=tk.StringVar(value="10000")
		volumestep=tk.StringVar(value="100")
		profitstep=tk.StringVar(value="2")
		startvaluerange=tk.StringVar(value="4.06")
		startvaluebuy=tk.StringVar(value="0.00")
		startvolumebuy=tk.StringVar(value="0")
		stopvaluerange=tk.StringVar(value="0.00")
		commonstep=tk.StringVar(value="0.00")
		totalcostbuy=tk.StringVar(value="0000000000")
		totalvolumebuy=tk.StringVar(value="000")
		stockname=tk.StringVar(value="dummy")
		stockpin=tk.StringVar(value="3333")
		self.configval={
			"invest":initinvest,
			"volumestep":volumestep,
			"profitstep":profitstep,
			"startvaluerange":startvaluerange,		
			"commonstep":commonstep,
			"startvaluebuy":startvaluebuy,
			"startvolumebuy":startvolumebuy,
			"stopvaluerange":stopvaluerange,
			"totalcostbuy":totalcostbuy,
			"totalvolumebuy":totalvolumebuy,
			"stockname":stockname,
			"stockpin":stockpin,

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

		
		self.frameLoginRT = tk.Frame(self ,background = 'green')
		# self.self.frameLoginRT.grid_propagate(0)
		self.frameLoginRT.grid(row=0,column=1,sticky="e"+"n"+"s"+"w")
	
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


		labelinitialvalue=tk.Label(frameSetValue, text="Volume")
		labelinitialvalue.grid(row=2,column=0)

		self.enterVolumn=tk.Entry(frameSetValue,textvariable=volumestep) #,textvariable=usertxt)
		self.enterVolumn.grid(row=2,column=1)

		labelinitialvalue=tk.Label(frameSetValue, text="Profit Step")
		labelinitialvalue.grid(row=3,column=0)

		self.enterVolumn=tk.Entry(frameSetValue,textvariable=profitstep) 
		self.enterVolumn.grid(row=3,column=1)


		labelinitialvalue=tk.Label(frameSetValue, text="StartValueRange")
		labelinitialvalue.grid(row=4,column=0)

		self.enterVolumn=tk.Entry(frameSetValue,textvariable=startvaluerange) 
		self.enterVolumn.grid(row=4,column=1)


		self.btnStartInitCal=tk.Button(frameSetValue,text="Set Parameters",command=self.startcalculate)
		self.btnStartInitCal.grid(row=5,column=1 )

		labelvaluebuy=tk.Label(frameSetValue, text="StartValueBuy")
		labelvaluebuy.grid(row=6,column=0)

		self.entervaluebuy=tk.Entry(frameSetValue,textvariable=startvaluebuy) 
		self.entervaluebuy.grid(row=6,column=1)

		self.btnStartvaluebuy=tk.Button(frameSetValue,text="Set Value Buy",command=self.setvaluebuy)
		self.btnStartvaluebuy.grid(row=7,column=1 )

		labelvaluebuy=tk.Label(frameSetValue, text="Cost:")
		labelvaluebuy.grid(row=7,column=0,sticky="w")

		labelvaluebuy=tk.Label(frameSetValue, textvariable=totalcostbuy)
		labelvaluebuy.grid(row=7,column=0,sticky="e")


		labelvalumebuy=tk.Label(frameSetValue, text="Volume:")
		labelvalumebuy.grid(row=8,column=0,sticky="w")

		labelvalumebuy=tk.Label(frameSetValue, textvariable=totalvolumebuy)
		labelvalumebuy.grid(row=8,column=0,sticky="e")

		self.framePutValue=tk.Frame(self,background = 'yellow')
		self.framePutValue.grid(row=3,column=1,sticky="e"+"n"+"s"+"w")      

		btnBuyCommand=tk.Button(self.framePutValue,text="Buy Now",command=self.buybyvalue, width = 10,height=2)
		btnBuyCommand.grid(row=0,column=0,sticky="w")

		btnSellCommand=tk.Button(self.framePutValue,text="Sell Now",command=self.sellbyvalue, width = 10,height=2)
		btnSellCommand.grid(row=0,column=0,sticky="e")

		btnRefreshCmd=tk.Button(self.framePutValue,text="Refresh",command=self.rtrefresh, width = 25,height=3)
		btnRefreshCmd.grid(row=1,column=0)





		self.canvas=tk.Canvas(self,background="black")
		self.canvas.grid(row=2,column=0,rowspan=2,sticky="nsew")


		self.frameGroupOutput = tk.Frame(self.canvas,background = 'gray')
		self.frameGroupOutput.grid(row=0,column=0) # start row 2 since text output occupied 2 rows with 0,1.

		self.scrollbarYGroupOutPut = tk.Scrollbar(self,orient="vertical", command = self.canvas.yview)
		self.scrollbarYGroupOutPut.grid(row=2,column=0,rowspan=2,sticky="e"+"n"+"s")

		self.scrollbarXGroupOutPut = tk.Scrollbar(self,orient="horizontal", command = self.canvas.xview)
		self.scrollbarXGroupOutPut.grid(row=4,column=0,rowspan=1,sticky="e"+"s"+"w")

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

	def executeSave(self):
		print("saveAllvalue")

	def executeLoad(self):
		print("LoadAllValue")

	def setvaluebuy(self):

		print("start value buy=" + self.configval["startvaluebuy"].get())
		valuebuy=self.configval["startvaluebuy"].get()

	


		# print (self.configval["stopvaluerange"].get())
		stopvaluerange=float(self.configval["stopvaluerange"].get())
		# print (self.configval["commonstep"].get())
		commonstep=float(self.configval["commonstep"].get())
		
		runvalue=round(float(valuebuy),2)
		priceaccume=0
		volumeaccume=0
		while (runvalue<=stopvaluerange):

			runvalue=round(runvalue,2)
			print ("round run value=" +str(runvalue))
			print ("stopvaluerange=" +str(stopvaluerange))
			chkpad=str(runvalue).split(".")

			if len(chkpad[1])==1:
				tempval=chkpad[1]+"0"
				stval=chkpad[0]+"." +tempval
				runvalue=stval
				# print(self.myvarasso[runvalue])
				priceaccumestep= float(self.myvarasso[runvalue]["price"].get())
				volumeaccumestep= float(self.myvarasso[runvalue]["volumn"].get())

				print (runvalue+" need price = " + str(priceaccumestep))
				


				lblvalue=str(runvalue)
				self.labeldisplay[lblvalue][lblvalue].configure(fg='black',background='green')
				self.labeldisplay[lblvalue]["updatedate"].configure(fg='black',background='green')
				self.labeldisplay[lblvalue]["updatetime"].configure(fg='black',background='green')
				self.labeldisplay[lblvalue]["volumn"].configure(fg='black',background='green')
				self.labeldisplay[lblvalue]["price"].configure(fg='black',background='green')
				self.labeldisplay[lblvalue]["order"].configure(fg='black',background='green')
				self.labeldisplay[lblvalue]["state"].configure(fg='black',background='green')
				self.labeldisplay[lblvalue]["targetvalue"].configure(fg='black',background='green')
				self.labeldisplay[lblvalue]["profit"].configure(fg='black',background='green')	

				runvalue=float(stval)


				priceaccume+=priceaccumestep
				volumeaccume+=volumeaccumestep
				
			else:
				# print(self.myvarasso[str(runvalue)])
				
				
				

				lblvalue=str(runvalue)
				self.labeldisplay[lblvalue][lblvalue].configure(fg='black',background='green')
				self.labeldisplay[lblvalue]["updatedate"].configure(fg='black',background='green')
				self.labeldisplay[lblvalue]["updatetime"].configure(fg='black',background='green')
				self.labeldisplay[lblvalue]["volumn"].configure(fg='black',background='green')
				self.labeldisplay[lblvalue]["price"].configure(fg='black',background='green')
				self.labeldisplay[lblvalue]["order"].configure(fg='black',background='green')
				self.labeldisplay[lblvalue]["state"].configure(fg='black',background='green')
				self.labeldisplay[lblvalue]["targetvalue"].configure(fg='black',background='green')
				self.labeldisplay[lblvalue]["profit"].configure(fg='black',background='green')	

				priceaccumestep=float(self.myvarasso[lblvalue]["price"].get())
				volumeaccumestep= float(self.myvarasso[lblvalue]["volumn"].get())

				print (str(runvalue) +" need price = " + str(priceaccumestep))
				priceaccume+=priceaccumestep
				volumeaccume+=volumeaccumestep

			runvalue+=commonstep
			runvalue=round(runvalue,2)

		self.labeldisplay[valuebuy][valuebuy].configure(fg='white',background='orange')
		self.labeldisplay[valuebuy]["updatedate"].configure(fg='white',background='orange')
		self.labeldisplay[valuebuy]["updatetime"].configure(fg='white',background='orange')
		self.labeldisplay[valuebuy]["volumn"].configure(fg='white',background='orange')
		self.labeldisplay[valuebuy]["price"].configure(fg='white',background='orange')
		self.labeldisplay[valuebuy]["order"].configure(fg='white',background='orange')
		self.labeldisplay[valuebuy]["state"].configure(fg='white',background='orange')
		self.labeldisplay[valuebuy]["targetvalue"].configure(fg='white',background='orange')
		self.labeldisplay[valuebuy]["profit"].configure(fg='white',background='orange')


		print ("Total price to buy =" +str(priceaccume))
		self.configval["totalcostbuy"].set(priceaccume)
		self.configval["totalvolumebuy"].set(volumeaccume)
		self.txtout("Set Value to buy =" + valuebuy)
		self.txtout("Set Value End to buy = " + str(stopvaluerange))
		self.txtout("Set total price to pay = " + str(priceaccume))
		self.txtout("Set total volume to pay = " + str(volumeaccume))

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


	def startcalculate(self):
		print("calculate here")

		print(self.configval["invest"].get())
		i=0
		# for label in self.configval:
		# 	configlabel=tk.Label(self.framePutValue,text=label)
		# 	configlabel.grid(row=i,column=1)   
		# 	i+=1


		startvaluerange=float(self.configval["startvaluerange"].get())
		invest=int(self.configval["invest"].get())
		volumestep=int(self.configval["volumestep"].get())
		profitstep=int(self.configval["profitstep"].get())
		commonvaluestep=float(self.configval["commonstep"].get())

		
		# runvaluerange=startvaluerange


		# for i,valuelabel in enumerate(self.labeldisplay):
		# 	# print ( valuelabel)

		# 	runvaluerange=float(valuelabel)
		# 	if (startvaluerange >= runvaluerange):
		# 		print(str(runvaluerange))


		# exit()


		runinvest=invest
		for i,valuelabel in enumerate(self.myvarasso):
			runvaluerange=float(valuelabel)
			print ("runvaluerange = " +str(runvaluerange))

			if (startvaluerange<=runvaluerange):
				

				print("run value range = " + str(runvaluerange))
				stcost=str(round((runvaluerange*volumestep),2))


				print ("remain invest = " +  str(runinvest))
				if runinvest > (runvaluerange*volumestep):

					chkpad=str(runvaluerange).split(".")

					if len(chkpad[1])==1:
						tempval=chkpad[1]+"0"
						stval=chkpad[0]+"." +tempval
						valuelabel=stval
					else:
						valuelabel=str(runvaluerange)
											
					self.labeldisplay[valuelabel][valuelabel].configure(background="white")
					self.labeldisplay[valuelabel]["updatedate"].configure(background="white")
					self.labeldisplay[valuelabel]["updatetime"].configure(background="white")
					self.labeldisplay[valuelabel]["volumn"].configure(background="white")
					self.labeldisplay[valuelabel]["price"].configure(background="white")

					self.labeldisplay[valuelabel]["order"].configure(background="white")
					self.labeldisplay[valuelabel]["state"].configure(background="white")
					self.labeldisplay[valuelabel]["targetvalue"].configure(background="white")
					self.labeldisplay[valuelabel]["profit"].configure(background="white")

					self.myvarasso[valuelabel]["volumn"].set(volumestep)

					self.myvarasso[valuelabel]["price"].set(stcost)

					target=round((float(commonvaluestep) * profitstep) + float(valuelabel),2)
					# print ("target value="+str(target))
					# exit()
					self.myvarasso[valuelabel]["targetvalue"].set(target)
					runinvest -=(runvaluerange*volumestep)
					stopvaluerange=runvaluerange
					# invest=remaininvest
				else:

					
					print("remain invest that could not put more = " +str(runinvest))
					break



				# runvaluerange+=commonvaluestep
		print ("remain invest = "+ str(runinvest))
		# print ("stopvaluerange at = " + str(stopvaluerange))
		self.configval["stopvaluerange"].set(stopvaluerange)
		# exit()

		self.canvas.yview_moveto(0.01)
		self.canvas.xview_moveto(0.01)
		# self.canvas.yview_moveto(0.5)


		self.txtout("Set Invest = " +str(invest),"yellow","gray")
		self.txtout("Set Step Volumn = " +str(volumestep))
		self.txtout("Set Step Common Value = " +str(commonvaluestep))
		self.txtout("Remain Range Invest =" +str(runinvest),"orange","green")
		
		self.txtout("Set Step Profit = " +str(profitstep))
		self.txtout("Set Start Value Range = " +str(startvaluerange))
		self.txtout("Set Stop Value Range = " +str(stopvaluerange),"green","white")


	def doMenuRange(self,value):


		plansel=value.split(' ')[0]
		self.myvarasso=self.initRangeValue(plansel[-1])

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
				self.frameGroupOutput.grid(row=0,column=0) # start row 2 since text output occupied 2 rows with 0,1.
				self.scrollbarYGroupOutPut = tk.Scrollbar(self,orient="vertical", command = self.canvas.yview)
				self.scrollbarYGroupOutPut.grid(row=2,column=0,rowspan=2,sticky="e"+"n"+"s")

				self.scrollbarXGroupOutPut = tk.Scrollbar(self,orient="horizontal", command = self.canvas.xview)
				self.scrollbarXGroupOutPut.grid(row=4,column=0,rowspan=1,sticky="e"+"s"+"w")

				# self.scrollbarXGroupOutPut = tk.Scrollbar(self,orient="horizontal", command = self.canvas.xview)
				# self.scrollbarXGroupOutPut.grid(row=4,column=0,rowspan=1,sticky="e"+"s"+"w")



				break		

		self.labeldisplay={}
		self.labeldisplay.clear()

		runrangeNo=len(list (self.myvarasso.items()))-1
		for i,myvarvalue in enumerate(self.myvarasso):

			varvalue=list (self.myvarasso.items())[runrangeNo][0]
			# print ("number of i=" + str(i))
			
			# print(runrangeNo)


			self.labeldisplay[varvalue]={}
			# print("number of variable = " + str(len (self.labeldisplay)))

			self.labeldisplay[varvalue][varvalue]=tk.Label(self.frameGroupOutput, text=varvalue)
			self.labeldisplay[varvalue][varvalue].grid(row=i,column=0)

			labelseparate=tk.Label(self.frameGroupOutput, text=" | ")
			labelseparate.grid(row=i,column=1)
			
			rowvalue=self.myvarasso[varvalue]

			for j,varinfo in enumerate(rowvalue):
				# print (varinfo)
				if varinfo=="updatedate" or varinfo=="updatetime" or varinfo=="volumn" or varinfo=="order" or varinfo=="state" or varinfo=="price":
					self.labeldisplay[varvalue][varinfo]=tk.Label(self.frameGroupOutput , textvariable=self.myvarasso[varvalue][varinfo])
					# self.labeldisplay.grid_propagate(0)
					self.labeldisplay[varvalue][varinfo].grid(row=i,column=j+2)
				if varinfo=="buy" or varinfo=="sell" or varinfo=="cancel":
					self.buyBtnInFrame=tk.Button(self.frameGroupOutput,textvariable=self.myvarasso[varvalue][varinfo],command=self.executeLogin)
					self.buyBtnInFrame.grid(row=i,column=j+3 )
				
				if varinfo=="targetvalue" or varinfo =="profit":
					self.labeldisplay[varvalue][varinfo]=tk.Label(self.frameGroupOutput , textvariable=self.myvarasso[varvalue][varinfo])
					# self.labeldisplay.grid_propagate(0)
					self.labeldisplay[varvalue][varinfo].grid(row=i,column=j+4)
			runrangeNo-=1


		# print (self.myvarasso)
		# print ("22"+rowvalue)	
		
		# exit()


		self.canvas['yscrollcommand'] = self.scrollbarYGroupOutPut.set
		self.canvas.bind('<Configure>', self.on_configure)

		self.canvas['xscrollcommand'] = self.scrollbarXGroupOutPut.set
		self.canvas.bind('<Configure>', self.on_configure)

		self.canvas.create_window((0,0), window=self.frameGroupOutput, anchor='center')
		# self.canvas.create_window((0,0), window=self.frameXGroupOutput, anchor='we')

		self.canvas.update()
		# update database at the first time select range
		# print (self.myvarasso)
		# self.mybot.dbqueue.put({"varasso":self.myvarasso})
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

	def rangeline(self,series):

		datenow = datetime.datetime.now().strftime("%Y-%m-%d")
		timenow = datetime.datetime.now().strftime("%H:%M:%S")

		varasso={}
		varstep={}
		varinfo={}
		# print (series)
		for rowid,varvalue in enumerate(series):
			# print (rowid)
			# print (varvalue)
			# exit()

			vardate=tk.StringVar(value=datenow)
			vartime=tk.StringVar(value=timenow)
			varorder=tk.StringVar(value="order")
			varstatus=tk.StringVar(value="state")
			varvolumn=tk.StringVar(value="volumn")
			varprice=tk.StringVar(value="price")
			varbuy=tk.StringVar(value="buy")
			varsell=tk.StringVar(value="sell")
			varcancel=tk.StringVar(value="cancel")
			vartargetvalue=tk.StringVar(value="target")
			varprofit=tk.StringVar(value="profit")
			# varvalue=tk.StringVar(value=data)

			varinfo={
				"updatedate":vardate,
				"updatetime":vartime,
				"volumn":varvolumn,
				"price":varprice,
				"order":varorder,
				"state":varstatus,
				"buy":varbuy,
				"sell":varsell,
				"cancel":varcancel,
				"targetvalue":vartargetvalue,
				"profit":varprofit,
			}
			# varstep={"value":varvalue}
			varasso[varvalue]=varinfo


		# print (varasso)
	
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

			# self.mycount+=1
			# step=10+(self.mycount/10)
			# print (step)
			# print (dir(self))
			# if not self.mybot.qvalchange.empty():
			# print(self.mybot.mycollectqueues)
			# if not self.mybot.mycollectqueues["qdatarefresh"].empty():
			# 	temprefreshdata=self.mybot.mycollectqueues["qdatarefresh"].get()
			# 	print(temprefreshdata)
			# print ("!!!!!!!!!!!!!!!!!! Dump data refresh !!!!!!!!!!!!!")
			# alreadyputback=False

			if not self.mybot.mycollectqueues["qvalchange"].empty():
				tempdict=self.mybot.mycollectqueues["qvalchange"].get()
				print (tempdict)
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

			if not self.mybot.mycollectqueues["qorder"].empty() :
				chkorder=self.mybot.mycollectqueues["qorder"].get()
				print ("chkorder tkconsole.py line 760")
				print (chkorder)
				if chkorder["order"]=="refreshtk":
					print ("<<<<<<<<<<refresh Tk Inter GUI need to refresh now")
					# self.alreadyputback=False
				else:
					print (">>>>>>>>Put refresh back DB")
					chkorder=self.mybot.mycollectqueues["qorder"].put(chkorder)
					# self.alreadyputback=True
				
			# self.output.tag_config("testb", background="white", foreground="red")
			# self.output.tag_add('testb', 10.0, step)
			self.after(50, self.Refresher) # every second...


# if __name__ == '__main__':
#     # print("start logoutput")
#     txtoutput=outputlog()
#     txtoutput.Refresher()
#     txtoutput.mainloop()

# exit()