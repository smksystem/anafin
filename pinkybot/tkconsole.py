
import tkinter as tk
import datetime
import sys
import time
from pinkybot.mylogconfig import mylog

from pinkybot.monitor import pinkybot
from pinkybot.packsel_model import PackSelModel
from pinkybot.plugin_fivesteps import fivesteps
from pinkybot.plugin_onestep import onestep
class outputlog(tk.Tk,mylog):
	def __init__(self):

		tk.Tk.__init__(self)
		# mylog.__init__(self)
		
		self.info("Initialize and start to load plugin")


		self.mybot=pinkybot(plugins=[fivesteps()])
		# self.mybot=pinkybot(plugins=[onestep()])
		self.title("Output Log")
		# self.resizable(0,0)
		self.geometry('780x620+20+20')
		# self.grid_columnconfigure(1, weight=1)
		# self.pack_propagate(0)
		usertxt=tk.StringVar(value="014xxxx")
		passtxt=tk.StringVar()
		broketxt=tk.StringVar(value="013")
		# global time1
		self.loginSet=[
						broketxt,
						usertxt,
						passtxt,
						
						]
		
		initinvest=tk.StringVar(value="0")
		volumestep=tk.StringVar(value="0")
		profitstep=tk.StringVar(value="0")
		topvaluerange=tk.StringVar(value="0")
		floorvaluerange=tk.StringVar(value="0")
		startvaluebuy=tk.StringVar(value="0")

		stopvaluerange=tk.StringVar(value="0.00")
		commonstep=tk.StringVar(value="0.00")  # step from range calculation
		totalcostbuy=tk.StringVar(value="0000000000")
		totalvolumebuy=tk.StringVar(value="000")
		stockname=tk.StringVar(value="")
		stockpin=tk.StringVar(value="3333")
		remaininvest=tk.StringVar(value="0")
		runningmode=tk.StringVar(value="auto")		

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
			"runningmode": runningmode,
		}

		self.myvarasso={}



		self.starttime =None




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
		enterbrokeid=tk.Entry(self.frameLoginRT,textvariable=broketxt)
		enterbrokeid.grid(row=0,column=1)      




		labelnamelogin=tk.Label(self.frameLoginRT, text="Login ID")
		labelnamelogin.grid(row=1,column=0)
		enterloginid=tk.Entry(self.frameLoginRT,textvariable=usertxt)
		enterloginid.grid(row=1,column=1)

		labelnamepassword=tk.Label(self.frameLoginRT, text="Password")
		labelnamepassword.grid(row=2,column=0)
		enterpassword=tk.Entry(self.frameLoginRT,show="*",textvariable=passtxt)
		enterpassword.grid(row=2,column=1)

		labelpinpassword=tk.Label(self.frameLoginRT, text="PIN")
		labelpinpassword.grid(row=3,column=0)
		enterpin=tk.Entry(self.frameLoginRT,show="*",textvariable=stockpin)
		enterpin.grid(row=3,column=1)

		btnLoginRT=tk.Button(self.frameLoginRT,text="Start Login RT",command=self.executeLogin)
		btnLoginRT.grid(row=3,column=2 )

		




		frameSetValue=tk.Frame(self,background = 'blue')
		frameSetValue.grid(row=2,column=1,sticky="e"+"n"+"s"+"w")      


		labelmonitor=tk.Label(frameSetValue,text="Monitor => ")
		labelmonitor.grid(row=1,column=0)

		labelstock=tk.Entry(frameSetValue,textvariable=stockname)
		labelstock.grid(row=1,column=1)



		labelinitialvalue=tk.Label(frameSetValue, text="Invest")
		labelinitialvalue.grid(row=2,column=0)

		enterInvest=tk.Entry(frameSetValue,textvariable=initinvest) #,textvariable=usertxt)
		enterInvest.grid(row=2,column=1)


		labelinitialvalue=tk.Label(frameSetValue, text="Volume Step")
		labelinitialvalue.grid(row=3,column=0)

		enterVolumn=tk.Entry(frameSetValue,textvariable=volumestep) #,textvariable=usertxt)
		enterVolumn.grid(row=3,column=1)

		labelinitialvalue=tk.Label(frameSetValue, text="Profit Step")
		labelinitialvalue.grid(row=4,column=0)

		enterVolumn=tk.Entry(frameSetValue,textvariable=profitstep) 
		enterVolumn.grid(row=4,column=1)


		labelinitialvalue=tk.Label(frameSetValue, text="Top Value Range")
		labelinitialvalue.grid(row=5,column=0)

		enterVolumn=tk.Entry(frameSetValue,textvariable=topvaluerange) 
		enterVolumn.grid(row=5,column=1)

		labelvaluebuy=tk.Label(frameSetValue, text="StartValueBuy")
		labelvaluebuy.grid(row=6,column=0)

		entervaluebuy=tk.Entry(frameSetValue,textvariable=startvaluebuy) 
		entervaluebuy.grid(row=6,column=1)

		labelinitialvalue=tk.Label(frameSetValue, text="Floor Value Range")
		labelinitialvalue.grid(row=7,column=0)

		enterVolumn=tk.Entry(frameSetValue,textvariable=floorvaluerange) 
		enterVolumn.grid(row=7,column=1)
		




		btnStartInitCal=tk.Button(frameSetValue,text="Set Parameters",command=self.setparameter)
		btnStartInitCal.grid(row=9,column=1 )



		# self.btnStartvaluebuy=tk.Button(frameSetValue,text="Set Value Buy",command=self.setvaluebuy,state='disabled',)
		# self.btnStartvaluebuy.grid(row=9,column=1 )

		labelvaluebuy=tk.Label(frameSetValue, text="Total Cost Buy:")
		labelvaluebuy.grid(row=9,column=0,sticky="w")

		labelvaluebuy=tk.Label(frameSetValue, textvariable=totalcostbuy)
		labelvaluebuy.grid(row=9,column=0,sticky="e")


		labelvalumebuy=tk.Label(frameSetValue, text="Total Volume Buy:")
		labelvalumebuy.grid(row=10,column=0,sticky="w")

		labelvalumebuy=tk.Label(frameSetValue, textvariable=totalvolumebuy)
		labelvalumebuy.grid(row=10,column=0,sticky="e")

		labelvalumebuy=tk.Label(frameSetValue, text="Remain Invest:")
		labelvalumebuy.grid(row=11,column=0,sticky="w")

		labelvalumebuy=tk.Label(frameSetValue, textvariable=remaininvest)
		labelvalumebuy.grid(row=11,column=0,sticky="e")
		

		framePutValue=tk.Frame(self,background = 'yellow')
		framePutValue.grid(row=3,column=1,sticky="e"+"n"+"s"+"w")      


		btnBuyCommand=tk.Button(framePutValue,text="Buy Now",command=self.buybyclick, width = 10,height=2)
		btnBuyCommand.grid(row=0,column=0,sticky="w")

		btnSellCommand=tk.Button(framePutValue,text="Sell Now",command=self.sellbyclick, width = 10,height=2)
		btnSellCommand.grid(row=0,column=0,sticky="e")

		btnRefreshCmd=tk.Button(framePutValue,text="Refresh",command=self.rtrefresh, width = 25,height=3)
		btnRefreshCmd.grid(row=1,column=0)

		radioauto=tk.Radiobutton(framePutValue,text="auto",variable=runningmode,value="auto",indicatoron=0,command=self.chooserunningmode)
		radioauto.grid(row=0,column=1,sticky="e")

		radiomanual=tk.Radiobutton(framePutValue,text="manual",variable=runningmode,value="manual",indicatoron=0,command=self.chooserunningmode)
		radiomanual.grid(row=0,column=2,sticky="w")



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


		
# when start up to set automatic 
		self.doMenuRange("PlanB")
		self.setparameter()


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
		

		if not self.mybot.mycollectqueues["qtimerefresh"].empty(): 
			timeparams = self.mybot.mycollectqueues["qtimerefresh"].get()

			# print("qtime refresh is call tkconsole.py line 307 def tkclock")
			# print (self.starttime,timeparams)

			if timeparams["command"]=="starttime":
				self.starttime=time.time()
				print("\nstart time count is called tkconsitole.py line 307 def tkclock")
				print(self.starttime)
				print("\n\n")

			elif timeparams["command"]=="monitoring" and self.starttime is not None:
				# print("monitoring value is called tkconsole.py line 314 def tkclock")
				elapsedtime=(time.time() - self.starttime)
				# print(elapsedtime)

				self.mybot.mycollectqueues["qtimerefresh"].put({"command":"monitoring"})			
				# if elapsedtime >= 10 :
				if elapsedtime >= 3 :

					print("refresh time more than 3 seconds packsel.py line 281 def monitoring")
					self.txtout("Put Queue refresh time at : " + self.time2)
					# self.mybot.mycollectqueues["qrefresh"].put({"qrefresh":"refreshdb","refreshtype":"all"})
					self.mybot.mycollectqueues["qrefresh"].put({"qrefresh":"refreshdb","refreshtype":"partial"}) 
					self.starttime=time.time()
					# self.mybot.mycollectqueues["qtimerefresh"].put({"refresh":"refresh"})			
					# self.starttime=time.time()
			else:
				self.mybot.mycollectqueues["qtimerefresh"].put(timeparams)
			# resultvaluechange=self.refreshbtn(driver,"partial")
			# print(self.starttime)


		# print("every 200 ms")
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

	def buybyclick(self):
		pass
	# 	print("Buy set value")
	# 	# self.mybot.myorder("buybyclick",self.configval)

	# 	buyparams={ "ordermode":"buybyclick",

	# 				}

	# 	self.mybot.mycollectqueues["qorder"].put(buyparams)
	# 	print ("Buy finished ")

	def sellbyclick(self):
		print ("sell set value")	

		# self.mybot.threadorderbuy("test")
	def rtrefresh(self):
		print ("refresh button press")
		self.mybot.botrtrefresh()
		# self.mybot.myorder("rtrefresh",self.configval)

	def chooserunningmode(self):
		print("run mode = "+ self.configval["runningmode"].get())
	def setparameter(self):

		# print(self.mybot)
		# print("setting necessary parameter tkconsole.py line 344")
		# print(self.configval)
		self.mybot.setparameter(self.configval,self.labeldisplay,self.txtout) # set default parameter for each plugins.

		return (0)


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
		varmatchordertime=tk.StringVar(value="monitormatchtime")
		varreferorderno=tk.StringVar(value="referorderno")
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
		varreferorderno.set (myvarinfo["referorderno"])
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

			"referorderno":varreferorderno,
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
					"referorderno":"peru",
					"orderside":"plum",
					"volume":"gold",
					"profit":"orchid",
					"state":"dodgerblue",
					"symbole":"white",
					}
		
		for j,varelement in enumerate(varinfo):

			rowid=self.labeldisplay[varvalue][varvalue].grid_info()['row']
			
			if  varelement=="orderno" or varelement=="startordertime" or varelement=="matchordertime"  or varelement =="targetvalue" or varelement=="symbole" :

				self.labeldisplay[varvalue][repeatidx][varelement]=tk.Label(self.frameGroupOutput , textvariable=varinfo[varelement],
														borderwidth=2, relief="groove",height=1,background=backgroudcolor[varelement])

				self.labeldisplay[varvalue][repeatidx][varelement].grid(row=rowid,column=(j+1+int(repeatidx)*6),sticky="n"+"e"+"w",pady=5)

				
			if  varelement=="referorderno" or varelement=="orderside" or varelement=="volume" or varelement == "profit" or varelement=="state" :

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

	def monomatch(self,label,orderno,color="lightgray"):
		print("\n$$$Print label orderno line 627 tkconsole.py in def monomatch")
		print(label,orderno)
		changecolor=False
		for labelidx,labelcontent in label.items():
			print("\n!!! Check loop for label in tkconsole.py line 628 in def monomatch")
			if labelcontent["text"]==orderno :
				changecolor=True
				break;
		if changecolor==True:
			for labelidx,labelcontent in label.items():
				labelcontent.configure(background=color)
		else:
			changecolor=False


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
						self.txtout(tempdict["textout"])

				if "stockvalue" in tempdict:
						logger.debug("stock has been updated !!!!!!!!!!!! tkconsole.py line 727 def Refresher")
						# controlorder={"ordermode":"buybybot","firstbuy":"yes"}
						# self.mybot.myplugins.order(controlorder,{},self.mybot.order)

						self.txtout("Value Change : " + tempdict["stockvalue"])
						lblstockvalue=tempdict["stockvalue"] # get value from queue
						if lblstockvalue in self.labeldisplay:
							self.flash(self.labeldisplay[lblstockvalue][lblstockvalue],9,"green")
				# self.mybot.myqueue.join()
				if "stockname" in tempdict:
						print("\n Monitor the following tempdict and self.configval")
						print ( tempdict["stockname"].upper(),self.configval["stockname"].get().upper())
						if tempdict["stockname"].upper()==self.configval["stockname"].get().upper():
							self.configval["stockname"].set(tempdict["stockname"].upper())



			if not self.mybot.mycollectqueues["qrefresh"].empty() :
				chkrefresh=self.mybot.mycollectqueues["qrefresh"].get()
				# print("check refresh , line 710, tkconsole.py")
				# print(chkrefresh)
				if chkrefresh["qrefresh"]=="refreshtk" and chkrefresh["doupdatetk"] != None :

					# print ("\n !!! Print data to do update refresh tkinter here !!!!! tkconsole.py line 757 in def Refresher")
					# print(chkrefresh)

					# L=chkrefresh["doupdatetk"]
					# chkrefresh["doupdatetk"]=list(filter(None.__ne__, chkrefresh["doupdatetk"]))
					# print(chkrefresh["doupdatetk"])
					# print("finish///....")
					
					for rowupdata in chkrefresh["doupdatetk"] :
						
						# print("\nprint doupdatetk file tkconsole.py line 722 in def Refresher")
						# print(chkrefresh["doupdatetk"])


						if chkrefresh["doupdatetk"]=="NOUPDATE":
							break
						
						# print(self.myvarasso)
						if len(self.myvarasso[rowupdata["price"]]) == 0:

							repeatidx=len(self.myvarasso[rowupdata["price"]])
							self.myvarasso[rowupdata["price"]].append(self.createrepeatinfo(rowupdata["price"],
																			repeatidx,rowupdata))
						else:
							# check if lable already existing then no more create label 
							for chklblorderno in self.myvarasso[rowupdata["price"]] :
								# print (chklblorderno["orderno"].get())
								chkorderno=chklblorderno["orderno"].get()
								
								print ("\ntkconsole.py line 775 compare orderno=" + chkorderno,rowupdata["orderno"])

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

								# print("+++++++need to update partial realtime table tkconsole.py line 790 !!!")
								# print(self.myvarasso[rowupdata["price"]])
								for varparams in self.myvarasso[rowupdata["price"]]:
									# print("print varparams tkconsole.py line 793")
									# print("\nvariable parameter to update tkconsole.py line 797 def Refresher")
									# print (varparams)
									for varrepeatkey,varrepeatvalue in varparams.items():
										# print("!!!!!!!!! show key and value of varparams tkconsole.py line 806")
										# print (varrepeatkey,varrepeatvalue.get())
										# print("\n print rowupdate of data tkconsole.py line 801 in def Refresher")
										# print(rowupdata)

										if varrepeatvalue.get()== rowupdata["orderno"] :
											# print ("********found orderno to update tkconsole.py line 811")

											varparams["orderside"].set(rowupdata["side"])
											varparams["volume"].set(rowupdata["volume"])
											# varparams["matchcomplete"].set(rowupdata["matched"])
											varparams["referorderno"].set(rowupdata["referorderno"])

											# varparams["referorderfrom"].set(rowupdata["referorderfrom"])

											# varparams["balance"].set(rowupdata["balance"])
											varparams["state"].set(rowupdata["status"])
											varparams["matchordertime"].set(rowupdata["matchedtime"])

											if rowupdata["status"] =="Matched(M)":
												# print("\n===Found Match status in has been send to update in tkconsole.py line 796 in def Refresher")
												# print(rowupdata)
												# print(self.labeldisplay)
												targetlabelprice=self.labeldisplay[rowupdata["price"]]
												grayorderno=rowupdata["orderno"]

												print("\n!!! print targetlabelprice line 806 tkconsole.py in def Refresher")
												print(targetlabelprice)

												for labelidx,(findlabel,labelcontent) in enumerate(targetlabelprice.items()):
													print("\n @@@ print labelidx , findlabel,labelcontent line 810 tkconsole.py in def Refresher")
													print( labelidx,findlabel,labelcontent)
													if labelidx> 0:
														# if labelcontent["orderno"]["text"]=grayorderno:
														print("\n### print findlabel[labelidx] in line 821 tkconsole.py in def Refresher")
														print(labelcontent["orderno"])
														self.monomatch(labelcontent,grayorderno)


												# self.flash(,9,"green")



					self.canvas.configure(scrollregion=self.canvas.bbox("all"))
					
				elif chkrefresh["qrefresh"]=="refreshdb":
					self.mybot.mycollectqueues["qrefresh"].put(chkrefresh)

				
			# self.output.tag_config("testb", background="white", foreground="red")
			# self.output.tag_add('testb', 10.0, step)
			self.after(5, self.Refresher) # every second...
