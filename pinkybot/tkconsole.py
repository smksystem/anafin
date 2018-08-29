
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
		
		investtxt=tk.StringVar(value="10000")
		volumntxt=tk.StringVar(value="1000")
		profitsteptxt=tk.StringVar(value="2")
		startvaluerangetxt=tk.StringVar(value="2.06")
		startvaluebuytxt=tk.StringVar(value="0.00")
		stopvaluerangetxt=tk.StringVar(value="0.00")
		commonstep=tk.StringVar(value="0.00")
		totalcostbuy=tk.StringVar(value="0000000000")


		self.configval={
			"invest":investtxt,
			"volumnstep":volumntxt,
			"profitstep":profitsteptxt,
			"startvaluerangetxt":startvaluerangetxt,		
			"commonstep":commonstep,
			"startvaluebuy":startvaluebuytxt,
			"stopvaluerangetxt":stopvaluerangetxt,
			"totalcostbuy":totalcostbuy,




		}

		



		self.myvarasso={}

		frameOutput = tk.Frame(self, width=500, height =200,background = 'blue')
		# self.frameOutput.grid_propagate(0)
		frameOutput.grid(row=0,column=0,rowspan = 2, columnspan = 1,sticky = "n"+"s" )

		self.output = tk.Text(frameOutput,wrap='word', width=60, height=14, background = 'black', fg='white')
		# self.output.grid_propagate(0)
		self.output.grid(row=0,column=0)
		# self.output.pack(side=tk.LEFT)

		self.scrollbar = tk.Scrollbar(frameOutput,orient="vertical", command = self.output.yview)
		# self.scrollbar.grid_propagate(0)
		self.scrollbar.grid(row=0,column=1,sticky="n"+"s")
		# self.scrollbar.pack(side=tk.RIGHT, fill="y")
		self.output['yscrollcommand'] = self.scrollbar.set

		
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

		self.btnLoginRT=tk.Button(self.frameLoginRT,text="Start Login RT",command=self.executeLogin)
		self.btnLoginRT.grid(row=3,column=1 )

		frameSetValue=tk.Frame(self,background = 'blue')
		# frameSetValue.grid_propagate(0)
		frameSetValue.grid(row=2,column=1,sticky="e"+"n"+"s"+"w")      

		labelinitialvalue=tk.Label(frameSetValue, text="Invest")
		labelinitialvalue.grid(row=1,column=0)

		self.enterInvest=tk.Entry(frameSetValue,textvariable=investtxt) #,textvariable=usertxt)
		self.enterInvest.grid(row=1,column=1)


		labelinitialvalue=tk.Label(frameSetValue, text="Volumn")
		labelinitialvalue.grid(row=2,column=0)

		self.enterVolumn=tk.Entry(frameSetValue,textvariable=volumntxt) #,textvariable=usertxt)
		self.enterVolumn.grid(row=2,column=1)

		labelinitialvalue=tk.Label(frameSetValue, text="Profit Step")
		labelinitialvalue.grid(row=3,column=0)

		self.enterVolumn=tk.Entry(frameSetValue,textvariable=profitsteptxt) 
		self.enterVolumn.grid(row=3,column=1)


		labelinitialvalue=tk.Label(frameSetValue, text="StartValueRange")
		labelinitialvalue.grid(row=4,column=0)

		self.enterVolumn=tk.Entry(frameSetValue,textvariable=startvaluerangetxt) 
		self.enterVolumn.grid(row=4,column=1)


		self.btnStartInitCal=tk.Button(frameSetValue,text="Set Parameters",command=self.startcalculate)
		self.btnStartInitCal.grid(row=5,column=1 )

		labelvaluebuy=tk.Label(frameSetValue, text="StartValueBuy")
		labelvaluebuy.grid(row=6,column=0)

		self.entervaluebuy=tk.Entry(frameSetValue,textvariable=startvaluebuytxt) 
		self.entervaluebuy.grid(row=6,column=1)

		self.btnStartvaluebuy=tk.Button(frameSetValue,text="Set Value Buy",command=self.setvaluebuy)
		self.btnStartvaluebuy.grid(row=7,column=1 )

		labelvaluebuy=tk.Label(frameSetValue, text="Cost:")
		labelvaluebuy.grid(row=7,column=0,sticky="w")

		labelvaluebuy=tk.Label(frameSetValue, textvariable=totalcostbuy)
		labelvaluebuy.grid(row=7,column=0,sticky="e")






		self.framePutValue=tk.Frame(self,background = 'yellow')
		# frameSetValue.grid_propagate(0)
		self.framePutValue.grid(row=3,column=1,sticky="e"+"n"+"s"+"w")      











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
		optionList=[]
		for planName,myrange in enumerate(rangeData):
			startfrom=str(rangeData[myrange][0])
			stopfrom=str(rangeData[myrange][1])
			stepfrom=str(rangeData[myrange][2])
			# print (self.rangeData[myrange][0])
			optionList.append("Plan" + myrange +" "+ startfrom+"-"+stopfrom + " step " +stepfrom)
		# print (optionlist)
		# optionList = ["Plan A 0-2 step 0.01",
		# 							"Plan B 2-4.98 step ",
		# 							"Plan C",
		# 							]

		# print ("hello this is menu")
		# print (optionList)
		# exit()

		self.rangeplanVar=tk.StringVar()
		self.rangeplanVar.set("Select range plan") # default choice
		self.rangeplanMenu1 = tk.OptionMenu(frameSetValue, self.rangeplanVar, *optionList,command=self.doMenuRange)
		self.rangeplanMenu1.grid(row=0,column=0,sticky="w")

		self.btnSave=tk.Button(frameSetValue,text="Save",command=self.executeSave)
		self.btnSave.grid(row=0,column=1,sticky="w")
		self.btnSave.update()

		self.btnLoad=tk.Button(frameSetValue,text="Load",command=self.executeLoad)
		self.btnLoad.grid(row=0,column=1,sticky="w",padx=self.btnSave.winfo_width())






		self.canvas=tk.Canvas(self,background="black")
		# self.canvas.grid_propagate(0)
		self.canvas.grid(row=2,column=0,rowspan=2,sticky="nsew")


		self.frameGroupOutput = tk.Frame(self.canvas,background = 'gray')
		# self.frameGroupOutput.grid_propagate(0)
		self.frameGroupOutput.grid(row=0,column=0) # start row 2 since text output occupied 2 rows with 0,1.






		# self.scrollbarGroupOutPut = tk.Scrollbar(self,orient="vertical", command = self.canvas.yview)
		# # self.scrollbarGroupOutPut.grid_propagate(0)
		# self.scrollbarGroupOutPut.grid(row=2,column=0,sticky="n"+"s"+"e")
		# # self.scrollbar.pack(side=tk.RIGHT, fill="y")
		# self.canvas['yscrollcommand'] = self.scrollbarGroupOutPut.set
		# self.canvas.bind('<Configure>', self.on_configure)
		# self.canvas.create_window((0,0), window=self.frameGroupOutput, anchor='center')






		# myvar=[]  
		# labelvar={}
		# labelinfo={}
		# # {0: {'volumn': <tkinter.StringVar object at 0x04331FB0>, 'update': <tkinter.StringVar object at 0x04331F10>, 'order': <tkinter.StringVar object at 0x04331F30>, 'state': <tkinter.StringVar object at 0x04331F70>}} 

		# self.labeldisplay={}
		# for i,varvalue in enumerate(self.myvarasso):

		# 	# print ("i="+str(i))
		# 	# print (self.myvarasso[varvalue]["volumn"])
		# 	# myvar.append(tk.StringVar())
		# 	self.labeldisplay[varvalue]={}
		# 	self.labeldisplay[varvalue][varvalue]=tk.Label(self.frameGroupOutput, text=varvalue)
		# 	# labelvar[varvalue]=tk.Label(self.frameGroupOutput, text=varvalue)
		# 	self.labeldisplay[varvalue][varvalue].grid(row=i,column=0)

		# 	labelseparate=tk.Label(self.frameGroupOutput, text=" | ")
		# 	labelseparate.grid(row=i,column=1)
			
		# 	# myinfo={}
		# 	# self.labeldisplay[varvalue]["info"]=myinfo

		# 	rowvalue=self.myvarasso[varvalue]

		# 	for j,varinfo in enumerate(rowvalue):
		# 		# print (varinfo)
		# 		if varinfo=="updatedate" or varinfo=="updatetime" or varinfo=="volumn" or varinfo=="order" or varinfo=="state" :
		# 			self.labeldisplay[varvalue][varinfo]=tk.Label(self.frameGroupOutput , textvariable=self.myvarasso[varvalue][varinfo])
		# 			# self.labeldisplay.grid_propagate(0)
		# 			self.labeldisplay[varvalue][varinfo].grid(row=i,column=j+2)
		# 		if varinfo=="buy" or varinfo=="sell" or varinfo=="cancel":
		# 			self.buyBtnInFrame=tk.Button(self.frameGroupOutput,textvariable=self.myvarasso[varvalue][varinfo],command=self.executeLogin)
		# 			self.buyBtnInFrame.grid(row=i,column=j+3 )
				
		# 		if varinfo=="targetvalue" or varinfo =="profit":
		# 			self.labeldisplay[varvalue][varinfo]=tk.Label(self.frameGroupOutput , textvariable=self.myvarasso[varvalue][varinfo])
		# 			# self.labeldisplay.grid_propagate(0)
		# 			self.labeldisplay[varvalue][varinfo].grid(row=i,column=j+4)

	

		

		# self.labeldisplay["5.00"]["order"].configure(background="red")
		# self.labeldisplay["8.00"]["state"].configure(background="white")
		# self.labeldisplay["8.10"]["order"].configure(background="red",foreground="green")
		# self.myvarasso["8.10"]["order"].set("buy")
		# self.flash(self.labeldisplay["8.10"]["order"],10)


		# self.labeldisplay["8.15"]["order"].configure(background="red",foreground="green")
		# self.myvarasso["8.15"]["order"].set("buy")
		# self.flash(self.labeldisplay["8.15"]["order"],10)


		# self.labeldisplay["8.25"]["state"].configure(background="red",foreground="green")
		# self.myvarasso["8.25"]["state"].set("buy")
		# self.flash(self.labeldisplay["8.25"]["state"],10)

		# exit()

		# dir(self.labelnamepassword)
		# myvar[0].set("hello1")
		# myvar[1].set("hello2")
		# ["text"]="testhello4"
		# self.labelnamepassword["name"].configure("text")="test"




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

		self.labeldisplay[valuebuy][valuebuy].configure(fg='white',background='orange')
		self.labeldisplay[valuebuy]["updatedate"].configure(fg='white',background='orange')
		self.labeldisplay[valuebuy]["updatetime"].configure(fg='white',background='orange')
		self.labeldisplay[valuebuy]["volumn"].configure(fg='white',background='orange')
		self.labeldisplay[valuebuy]["price"].configure(fg='white',background='orange')
		self.labeldisplay[valuebuy]["order"].configure(fg='white',background='orange')
		self.labeldisplay[valuebuy]["state"].configure(fg='white',background='orange')
		self.labeldisplay[valuebuy]["targetvalue"].configure(fg='white',background='orange')
		self.labeldisplay[valuebuy]["profit"].configure(fg='white',background='orange')


		# print (self.configval["stopvaluerangetxt"].get())
		stopvaluerange=float(self.configval["stopvaluerangetxt"].get())
		# print (self.configval["commonstep"].get())
		commonstep=float(self.configval["commonstep"].get())
		runvalue=round(float(valuebuy),2)
		print ("runvalue=" +str(runvalue))
		# print (self.myvarasso)
		while (runvalue<=stopvaluerange):

			chkpad=str(runvalue).split(".")
			# print(chkpad)
			# print(len(chkpad))
			
			if len(chkpad[1])==1:
			# 	stval=str(round(i,2))+".00"
			# elif len(chkpad)==2:
				tempval=chkpad[1]+"0"
				stval=chkpad[0]+"." +tempval
				runvalue=stval
				# print(self.myvarasso[runvalue])
				priceaccume=self.myvarasso[runvalue]["price"].get()

				runvalue= round(float(stval),2)

				print (str(runvalue)+" need price = " + priceaccume)
				
				
			else:
				# print(self.myvarasso[str(runvalue)])
				priceaccume=self.myvarasso[str(runvalue)]["price"].get()

				print (str(runvalue) +" need price = " + priceaccume)
			runvalue+=commonstep
			

			






	def startcalculate(self):
		print("calculate here")

		print(self.configval["invest"].get())
		i=0
		for label in self.configval:
			configlabel=tk.Label(self.framePutValue,text=label)
			configlabel.grid(row=i,column=1)   
			i+=1


		startvaluerange=self.configval["startvaluerangetxt"].get()

		invest=int(self.configval["invest"].get())
		volumnstep=int(self.configval["volumnstep"].get())
		profitstep=int(self.configval["profitstep"].get())

		totalstep=(invest/volumnstep)

		print ("Totalstep="+str(totalstep))


		commonvaluestep=self.configval["commonstep"].get()

		looprange=0

		for i,valuelabel in enumerate(self.labeldisplay):

			if (float(startvaluerange)<=float(valuelabel)):
				looprange+=1
				print ("start value " + valuelabel)
				self.labeldisplay[valuelabel][valuelabel].configure(background="white")
				self.labeldisplay[valuelabel]["updatedate"].configure(background="white")
				self.labeldisplay[valuelabel]["updatetime"].configure(background="white")
				self.labeldisplay[valuelabel]["volumn"].configure(background="white")
				self.labeldisplay[valuelabel]["price"].configure(background="white")

				self.labeldisplay[valuelabel]["order"].configure(background="white")
				self.labeldisplay[valuelabel]["state"].configure(background="white")
				self.labeldisplay[valuelabel]["targetvalue"].configure(background="white")
				self.labeldisplay[valuelabel]["profit"].configure(background="white")

				self.myvarasso[valuelabel]["volumn"].set(volumnstep)




				stcost=str(round(float(valuelabel) * float(volumnstep))) 

				self.myvarasso[valuelabel]["price"].set(stcost)

				target=round((float(commonvaluestep) * profitstep) + float(valuelabel),2)
				# print ("target value="+str(target))
				# exit()
				self.myvarasso[valuelabel]["targetvalue"].set(target)
				# print("common step print in calculate="+self.commonstep)






				if looprange==totalstep:
					print ( "end of value range = " + valuelabel)
					self.configval["stopvaluerangetxt"].set(valuelabel)
					stopvaluerange=valuelabel
					break


		self.canvas.yview_moveto(0.01)
		# self.canvas.yview_moveto(0.5)


		self.txtout("Set Invest = " +str(invest))
		self.txtout("Set Step Volumn = " +str(volumnstep))
		self.txtout("Set Step Common Value = " +str(commonvaluestep))
		self.txtout("Set Step Profit = " +str(profitstep))
		self.txtout("Set Start Value Range = " +str(startvaluerange))
		self.txtout("Set Stop Value Range = " +str(stopvaluerange))







	def doMenuRange(self,value):


		plansel=value.split(' ')[0]
		
		self.myvarasso=self.initRangeValue(plansel[-1])


		if plansel=="PlanA":
			# put on queue here

			# self.myvarasso=self.initRangeValue(selrange)
			print("planA selected")



		elif plansel=="PlanB":
			# self.myvarasso=self.initRangeValue(selrange)
			print("planB selected")
		elif plansel=="PlanC":
			# self.myvarasso=self.initRangeValue(selrange)
			print("planC selected")

		# print ("menurange selected" + value)
		children = self.frameGroupOutput.winfo_children()
		for child in children:
			# print (str(type(child)))
			if str(type(child)) == "<class 'tkinter.scroll'>":
				print ("found scroll")
		children = self.frameGroupOutput.winfo_children()
		for child in children:
			# print (str(type(child)))
			child.destroy()
				# if str(type(child)) == "<class 'tkinter.Message'>":
						# print("Here Message widget will destroy")
		






		self.scrollbarGroupOutPut = tk.Scrollbar(self,orient="vertical", command = self.canvas.yview)
		# self.scrollbar.grid_propagate(0)
		self.scrollbarGroupOutPut.grid(row=2,column=0,rowspan=2,sticky="e"+"n"+"s")
		# self.scrollbar.pack(side=tk.RIGHT, fill="y")
		self.canvas['yscrollcommand'] = self.scrollbarGroupOutPut.set
		self.canvas.bind('<Configure>', self.on_configure)
		self.canvas.create_window((0,0), window=self.frameGroupOutput, anchor='nw')



		myvar=[]  
		labelvar={}
		labelinfo={}
		# {0: {'volumn': <tkinter.StringVar object at 0x04331FB0>, 'update': <tkinter.StringVar object at 0x04331F10>, 'order': <tkinter.StringVar object at 0x04331F30>, 'state': <tkinter.StringVar object at 0x04331F70>}} 

		self.labeldisplay={}
		# print(self.myvarasso)
		for i,varvalue in enumerate(self.myvarasso):

			# print ("i="+str(i))
			# print (self.myvarasso[varvalue]["volumn"])
			# myvar.append(tk.StringVar())
			self.labeldisplay[varvalue]={}
			self.labeldisplay[varvalue][varvalue]=tk.Label(self.frameGroupOutput, text=varvalue)
			# labelvar[varvalue]=tk.Label(self.frameGroupOutput, text=varvalue)
			self.labeldisplay[varvalue][varvalue].grid(row=i,column=0)

			labelseparate=tk.Label(self.frameGroupOutput, text=" | ")
			labelseparate.grid(row=i,column=1)
			
			# myinfo={}
			# self.labeldisplay[varvalue]["info"]=myinfo

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


		self.canvas['yscrollcommand'] = self.scrollbarGroupOutPut.set
		self.canvas.bind('<Configure>', self.on_configure)
		self.canvas.create_window((0,0), window=self.frameGroupOutput, anchor='nw')


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



	def txtout(self,txtmsg):

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
	def highlight_text(self,word):
			# word="Vol"
			txtmsg=self.output.get("1.0","end")
			# print (txtmsg)
			countVar = tk.StringVar()
			self.output.tag_config("test", background="black", foreground="green")
			if txtmsg:
				pos = '1.0'
				while 1:
					pos = self.output.search( word,pos,stopindex="end", count=countVar)
					if not pos: break
					lastidx = '%s+%dc' % (pos, int(countVar.get()))
					self.output.tag_add('test', pos, lastidx)
					pos = lastidx

			self.output.see(tk.END)
		 
	def Refresher(self):

			# self.mycount+=1
			# step=10+(self.mycount/10)
			# print (step)
			# print (dir(self))
			if not self.mybot.myqueue.empty():
				tempdict=self.mybot.myqueue.get()
				# print (tempdict["textout"])
				if "textout" in tempdict:
						self.txtout("value change to:" + tempdict["textout"])
				if "stockvalue" in tempdict:
						print ("stock has been updated !!!!!!!!!!!!")
						self.txtout(tempdict["stockvalue"])
						lblstockvalue=tempdict["stockvalue"] # get value from queue
						if lblstockvalue in self.labeldisplay:
							self.flash(self.labeldisplay[lblstockvalue][lblstockvalue],9,"green")
				# self.mybot.myqueue.join()



				
			# self.output.tag_config("testb", background="white", foreground="red")
			# self.output.tag_add('testb', 10.0, step)
			self.after(1000, self.Refresher) # every second...


# if __name__ == '__main__':
#     # print("start logoutput")
#     txtoutput=outputlog()
#     txtoutput.Refresher()
#     txtoutput.mainloop()

# exit()