
import tkinter as tk
import datetime
import sys
import time
import json
from pinkybot.mylogconfig import mylog

from pinkybot.monitor import pinkybot
from pinkybot.packsel_model import PackSelModel
from pinkybot.plugin_fivesteps import fivesteps
from pinkybot.plugin_onestep import onestep
from pinkybot.unitTest import unitTest
from pinkybot.loginconfig import loginconfig
from pinkybot.configparams import configparams
from pinkybot.viewconfig import viewconfig
from PIL import Image, ImageTk
# from pinkybot.unitTest 

class outputlog(tk.Tk,mylog):
# class outputlog(tk.Tk):

	def __init__(self):

		tk.Tk.__init__(self)
		mylog.__init__(self)

		#############################TEST MENU PART########################################
		menubar = tk.Menu()
		# create a pulldown menu, and add it to the menu bar
		filemenu = tk.Menu(menubar, tearoff=0)
		configmenu = tk.Menu(menubar, tearoff=0)
		viewmenu= tk.Menu(menubar,tearoff=0)

		# menubar.add_cascade(label="File", menu=filemenu)
		menubar.add_cascade(label="Config", menu=configmenu)
		menubar.add_cascade(label="View", menu=viewmenu)

		# filemenu.add_command(label="New")
		# filemenu.add_separator()
		# filemenu.add_command(label = 'Quit')
		
		configmenu.add_command(label = "Config Login",command=self.loginconfig)
		configmenu.add_command(label = "Config Parameters",command=self.configparams)

		viewmenu.add_command(label="Show default config",command=self.tkviewconfig)

		self.config(menu = menubar)



		########################## MENU button #########################################

		toolbar = tk.Frame(self, borderwidth=2, relief='raised',bg='red')
		toolbar.grid(row=0,column=0,sticky="we",columnspan=4)	
		
		findbug=Image.open('images/findbug.png')
		findbug=findbug.resize((20,20),Image.ANTIALIAS)
		self.findbug=ImageTk.PhotoImage(findbug)

		findbugBtn=tk.Button(toolbar,image=self.findbug,command=self.unitTest)
		findbugBtn.grid(column=2,row=0,sticky="e")

		configImg=Image.open('images/config.png')
		configImg=configImg.resize((20,20),Image.ANTIALIAS)
		self.configPhoto=ImageTk.PhotoImage(configImg)

		configparamsBtn=tk.Button(toolbar,image=self.configPhoto)
		configparamsBtn.grid(column=3,row=0,sticky="e")		

		startrun=Image.open('images/start.png')
		startrun=startrun.resize((20,20),Image.ANTIALIAS)
		self.startrun=ImageTk.PhotoImage(startrun)

		startrunBtn=tk.Button(toolbar,image=self.startrun,command=self.executeLogin)
		startrunBtn.grid(column=4,row=0,sticky="e")		

		resetrun=Image.open('images/reset.png')
		resetrun=resetrun.resize((20,20),Image.ANTIALIAS)
		self.resetrun=ImageTk.PhotoImage(resetrun)

		resetrunBtn=tk.Button(toolbar,image=self.resetrun,command=self.testreset)
		resetrunBtn.grid(column=5,row=0,sticky="e")		

		self.lblcomputetime=tk.Label(toolbar,text="time")
		self.lblcomputetime.grid(row=0,column=6,sticky="e")
		
        ##################################################################################

		# self.log["console"].info("Initialize and start load plugin")
		# self.log["console"].info("Initialize console")


		##################################################################################
		############ Query default database for parameter to initialize configvalue ######
		self.configval= PackSelModel.getDefaultConfig()
		##################################################################################


		# self.mybot=pinkybot(plugins=[onestep()])
		self.title("Output Log")
		# print()
		# self.resizable(0,0)
		# self.geometry(str(self.winfo_screenwidth())+'x700+0+0')
		self.geometry('1020x700+0+0')

		
		# print(configparams)
		# self.configval={
		# 	"planname":tk.StringVar(value=configparams["planname"]),
		# 	"rangeselect":tk.StringVar(value=configparams["rangeselect"]),
		# 	"stockname":tk.StringVar(value=configparams["monitorstock"]),
		# 	"initinvest":tk.StringVar(value=configparams["initinvest"]),

		# 	"volumestep":tk.StringVar(value=configparams["volumestep"]),
		# 	"profitstep":tk.StringVar(value=configparams["profitstep"]),
		# 	"topvaluebuy":tk.StringVar(value=configparams["topvaluebuy"]),
		# 	"startvaluebuy":tk.StringVar(value=configparams["startvaluebuy"]),
		# 	"stopvaluebuy":tk.StringVar(value=configparams["stopvaluebuy"]),
		# 	"floorvaluebuy":tk.StringVar(value=configparams["floorvaluebuy"]),
		# 	"firstbuyflag":tk.StringVar(value=configparams["firstbuyflag"]),
		# 	"pluginfile":tk.StringVar(value=configparams["pluginfile"]),
		# 	"floorvaluerange":tk.StringVar(value=configparams["floorvaluerange"]),
		# 	"topvaluerange":tk.StringVar(value=configparams["topvaluerange"]),
		# 	"commonvaluestep":tk.StringVar(value=configparams["commonvaluestep"]),
		# 	"runningmode":tk.StringVar(value=configparams["runningmode"]),
		# 	"totalcostbuy":tk.StringVar(value="pluginvalue"),
		# 	"totalvolumebuy":tk.StringVar(value="pluginvalue"),

		# 	# commonstep=tk.StringVar(value=configparams["step"])  # step from range calculation
			
		# 	"stockpin":tk.StringVar(),

		# 	"remaininvest":tk.StringVar(value="pluginvalue"),
		# }

		############# ATTENTIOIN ################################################################
		# Pinkybot is in monitor.py file and send parameter plugin with fivesteps to this bot.
		#########################################################################################
		self.mybot=pinkybot(self.log,plugins=[fivesteps(self.log)])
		
		# stopvaluerange=tk.StringVar(value=configparams["stopvaluerange"])

		self.myvarasso={}



		self.starttime =None

		############################################################################################################################################
		############################# Text output frame #########################################################################################
		############################################################################################################################################


		frameOutput = tk.Frame(self, width=150, height =300,background = 'blue')
		# frameOutput.grid(row=0,column=0,rowspan = 1, columnspan = 1,sticky = "n"+"s" )
		# frameOutput.grid(row=0,column=0) #,rowspan = 1, columnspan = 1,sticky = "n"+"s" )


		frameOutput.grid(row=1,column=0,sticky = "n"+"s"+"w"+"e")
		# frameOutput.grid_propagate(False)

		# self.output = tk.Text(frameOutput,wrap='word', width=60, height=14, background = 'black', fg='white')
		self.output = tk.Text(frameOutput,width=120, height=20,wrap='word', background = 'black', fg='white')

		self.output.grid(row=0,column=0,columnspan=1)

		scrollbar = tk.Scrollbar(frameOutput,orient="vertical", command = self.output.yview)
		scrollbar.grid(row=0,column=1,sticky="ne"+"se")
		scrollbar.grid_propagate(False)

		self.output['yscrollcommand'] = scrollbar.set


		############################################################################################################################################
		############################# Time and unit test frame #########################################################################################
		############################################################################################################################################

		# frameTime=tk.Frame(self,background="Blue")
		# frameTime.grid(row=0,column=1,sticky="e"+"n"+"s"+"w")

		############################################################################################################################################
		############################# Login frame #########################################################################################
		############################################################################################################################################
		
		# self.frameLoginRT = tk.Frame(self ,background = 'green')
		# self.frameLoginRT.grid(row=1,column=2,sticky="e"+"n"+"s"+"w")


		# self.lablecomputetime=tk.Label(self.frameLoginRT,text="time")
		# self.lablecomputetime.grid(row=0,column=2)

		# btnUnitTest=tk.Button(self.frameLoginRT,text="Unit Test",command=self.unitTest)
		# btnUnitTest.grid(row=1,column=2 )

	

		####################################################################################################
		####################################################################################################
		####################################################################################################

		# btnLoginRT=tk.Button(self.frameLoginRT,text="Start Login RT",command=self.executeLogin)
		# btnLoginRT.grid(row=3,column=2 )

		
		
		############################################################################################################################################
		############################# Value parameter set frame #########################################################################################
		############################################################################################################################################



		# frameSetValue=tk.Frame(self,background = 'blue')
		# frameSetValue.grid(row=1,column=3,sticky="e"+"n"+"s"+"w")      



		############################################################################################################################################
		############################# Value select plan #########################################################################################
		############################################################################################################################################

		optionList=[]
		# for planName,myrange in enumerate(rangeData):
		myrange={"test":"test"}
		startfrom=str(myrange["test"])
		# stopfrom=str(rangeData[myrange][1])
		# stepfrom=str(rangeData[myrange][2])
		# print (self.rangeData[myrange][0])
		optionList.append(startfrom)

		# plannameVar=tk.StringVar()
		# plannameVar.set("Choose plan name") # default choice
		# self.rangeplanMenu1 = tk.OptionMenu(frameSetValue, plannameVar, *optionList,command=self.doMenuRange)
		# self.rangeplanMenu1.grid(row=1,column=0,sticky="w")



		# labelmonitor=tk.Label(frameSetValue,text="Planname ")
		# labelmonitor.grid(row=2,column=0)

		# labelstock=tk.Entry(frameSetValue,textvariable=planname)
		# labelstock.grid(row=2,column=1)


		# btnRefreshCmd=tk.Button(frameSetValue,text="Refresh",command=self.rtrefresh, width = 10,height=2)
		# btnRefreshCmd.grid(row=14,column=0)


		# radioauto=tk.Radiobutton(frameSetValue,text="auto",variable=runningmode,value="auto",indicatoron=0,command=self.chooserunningmode)
		# radioauto.grid(row=14,column=1,sticky="w")

		# radiomanual=tk.Radiobutton(frameSetValue,text="manual",variable=runningmode,value="manual",indicatoron=0,command=self.chooserunningmode)
		# radiomanual.grid(row=14,column=1)

		

		############################################################################################################################################
		############################# result buy/sell frame #########################################################################################
		############################################################################################################################################

		self.canvas=tk.Canvas(self,background="red")
		# self.canvas.grid_propagate=1
		self.canvas.grid(row=0,column=3,rowspan=2,columnspan=4,sticky="nsew")

		self.frameGroupOutput = tk.Frame(self.canvas,background = 'gray')
		self.frameGroupOutput.grid(row=0,column=0) # start row 2 since text output occupied 2 rows with 0,1.


		# vsbar = tk.Scrollbar(self,orient="vertical", command = self.canvas.yview)
		# vsbar.grid_propagate=True
		# vsbar.grid(row=2,column=2,rowspan=2,sticky="e"+"n"+"s")
		# self.canvas.configure(yscrollcommand=vsbar.set)

		hsbar = tk.Scrollbar(self,orient="horizontal", command = self.canvas.xview)
		hsbar.grid(row=4,column=0,rowspan=1,sticky="e"+"s"+"w")
		self.canvas.configure(yscrollcommand=hsbar.set)
		# scrollbar.pack(side=tk.RIGHT, fill="y")






		# rangeData={
		# "A":[0,1.99,0.01],  # 0 to 2 step 0.01
		# "B":[2,4.98,0.02], # 2 up to less than 5  0.02
		# "C":[5,9.95,0.05],
		# "D":[10,24.9,0.10],
		# "E":[25,99.75,0.25],
		# "F":[100,199.5,0.5],
		# "G":[200,399,1],
		# "H":[400,1000,2],
		# }
		# optionList=[]
		# for planName,myrange in enumerate(rangeData):
		# 	startfrom=str(rangeData[myrange][0])
		# 	stopfrom=str(rangeData[myrange][1])
		# 	stepfrom=str(rangeData[myrange][2])
		# 	# print (self.rangeData[myrange][0])
		# 	optionList.append("Plan" + myrange +" "+ startfrom+"-"+stopfrom + " step " +stepfrom)

		# self.rangeplanVar=tk.StringVar()
		# self.rangeplanVar.set("Select range plan") # default choice
		# self.rangeplanMenu1 = tk.OptionMenu(frameSetValue, self.rangeplanVar, *optionList,command=self.doMenuRange)
		# self.rangeplanMenu1.grid(row=0,column=0,sticky="w")

		# self.btnSave=tk.Button(frameSetValue,text="Save",command=self.executeSave)
		# self.btnSave.grid(row=0,column=1,sticky="w")
		# self.btnSave.update()

		# self.btnLoad=tk.Button(frameSetValue,text="Load",command=self.executeLoad)
		# self.btnLoad.grid(row=0,column=1,sticky="w",padx=self.btnSave.winfo_width())

		self.alreadyputback=False # To make put back into queue one time and sync to DB.


		
# when start up to set automatic 
		# self.doMenuRange("Plan"+self.configval["rangeselect"])

		self.doMenuRange(self.configval["rangeselect"].get())

		self.setlabeldisplay() ### refer to plugin_fivesteps.py


		self.update_idletasks()
		# self.mycount = 0
		
		# self.myvarasso["5.00"]["order"].set("buy")
		self.txtout("!!! Welcome , Please login !!!")
		self.tkclock()


######################################################
######## Loop to click refresh all the time ##########
######################################################
	def tkclock(self):
		
		# get the current local time from the PC
		self.time2 = time.strftime('%H:%M:%S')
		# if time string has changed, update it

		# if self.time2 != time1:
			# time1 = self.time2
		self.lblcomputetime.config(text=self.time2)
		

		if not self.mybot.mycollectqueues["qtimerefresh"].empty(): 
			timeparams = self.mybot.mycollectqueues["qtimerefresh"].get()

			# print("qtime refresh is call tkconsole.py line 307 def tkclock")
			# print (self.starttime,timeparams)

			if timeparams["command"]=="starttime":
				self.starttime=time.time()
				self.log["applog"].debug("Start time count is called def tkclock")
				self.log["applog"].debug(self.starttime)
				# print("\n\n")
				self.mybot.mycollectqueues["qtimerefresh"].put({"command":"monitoring"})			

			elif timeparams["command"]=="monitoring" and self.starttime is not None:
				# print("monitoring value is called tkconsole.py line 314 def tkclock")
				elapsedtime=(time.time() - self.starttime)
				# print(elapsedtime)

				self.mybot.mycollectqueues["qtimerefresh"].put({"command":"monitoring"})			
				# if elapsedtime >= 10 :
				if elapsedtime >= 1 : ### test 1 second.

					# print("refresh time more than 3 seconds packsel.py line 281 def monitoring")
					self.log["applog"].debug("Refresh time for partial with put into queue for refreshdb")
					# self.txtout("Put Queue refresh time at : " + self.time2)
					
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
		self.lblcomputetime.after(200, self.tkclock)

	# def executeSave(self):
	# 	self.log["console"].info("SaveAllValue")

	def testreset(self):
		self.log["applog"].debug("Reset file test and database Testing done!")
		# print("reset back to begining")
		open('stockpost.txt', 'w').close()
		open('applog.log', 'w').close()

		# print()
		PackSelModel.updatefirstorderbuy(self.configval["planname"].get(),"YES")

	def TESTexecuteLoad(self):
		print("LoadTESTAllValue")
		self.createrepeatinfo("4.98",2,
			
			{
			'id': 2021, 'orderno': '500002', 'time': '20:46:20', 'symbole': 'WHA', 'side': 'B', 'price': '4.72', 'volume': '100', 'matched': '0', 'balance': '0', 'cancelled': '0', 'status': 'Matched(M)', 'date': datetime.date(2019, 5, 16), 'matchedtime': '20:57:08', 'referorderno': '580415'
			}
			)
		self.createrepeatinfo("4.98",1,
			
			{
			'id': 2022, 'orderno': '500001', 'time': '20:46:21', 'symbole': 'WHA', 'side': 'B', 'price': '4.72', 'volume': '100', 'matched': '0', 'balance': '0', 'cancelled': '0', 'status': 'Matched(M)', 'date': datetime.date(2019, 5, 16), 'matchedtime': '20:57:08', 'referorderno': '580415'
			}
			)
		self.createrepeatinfo("4.98",0,
			
			{
			'id': 2022, 'orderno': '500000', 'time': '20:46:22', 'symbole': 'WHA', 'side': 'B', 'price': '4.72', 'volume': '100', 'matched': '0', 'balance': '0', 'cancelled': '0', 'status': 'Matched(M)', 'date': datetime.date(2019, 5, 16), 'matchedtime': '20:57:08', 'referorderno': '580415'
			}
			)
		self.canvas.configure(scrollregion=self.canvas.bbox("all"))

	
	def rtrefresh(self):
		print ("refresh button press")
		self.mybot.botrtrefresh()

		# self.mybot.myorder("rtrefresh",self.configval)
	

	def chooserunningmode(self):
		print("run mode = "+ self.configval["runningmode"].get())
	def setlabeldisplay(self):

		# print(self.mybot)
		# print("setting necessary parameter tkconsole.py line 344")
		# print(self.configval)
		
		##################################################
		# labeldisplay from doMenuRange call via bot keep in both packsel and plugin
		##################################################
		# self.mybot.putconfigval(self.configval)
		self.mybot.pinkymonitordisplay(self.configval,self.labeldisplay,self.txtout) # set default parameter for each plugins.



		return (0)


	def doMenuRange(self,value):


		# plansel=value.split(' ')[0]
		# plansel=value

		# self.myvarasso=self.initRangeValue(plansel[-1])
		self.myvarasso=self.initRangeValue(value)


		# print(self.myvarasso["4.00"])
		# exit()

		# if plansel=="PlanA":
		# 	print("planA selected")
		# elif plansel=="PlanB":
		# 	print("planB selected")
		# elif plansel=="PlanC":


		# 	print("planC selected")



		
		children = self.winfo_children()
		for child in children:
			# print (str(type(child)))
			if (str(type(child)) == "<class 'tkinter.Canvas'>") :
				child.destroy()

				# print("Start to create output group")

				self.canvas=tk.Canvas(self,background="black")
				self.canvas.grid(row=2,column=0,rowspan=2,columnspan=5,sticky="nsew")

				self.frameGroupOutput = tk.Frame(self.canvas,background = 'gray')
				self.frameGroupOutput.grid(row=0,column=0,sticky="nsew") # start row 2 since text output occupied 2 rows with 0,1.


				self.scrollbarYGroupOutPut = tk.Scrollbar(self,orient="vertical", command = self.canvas.yview)
				self.scrollbarYGroupOutPut.grid(row=2,column=5,rowspan=2,sticky="e"+"n"+"s")

				self.scrollbarXGroupOutPut = tk.Scrollbar(self,orient="horizontal", command = self.canvas.xview)
				self.scrollbarXGroupOutPut.grid(row=4,column=0,rowspan=1,columnspan=5,sticky="e"+"s"+"w")


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
		#### Get data from config value which from packsel_model
		i=float(self.configval["floorvaluerange"].get())
		my_topvaluerange=float(self.configval["topvaluerange"].get())

		series=[]
		while i <= my_topvaluerange:

			chkpad=str(round(i,2)).split(".")
			if len(chkpad)==1:
				stval=str(round(i,2))+".00"
			elif len(chkpad)==2:
				tempval=chkpad[1]+"0"
				stval=chkpad[0]+"." +tempval[:2]

			i+=float(self.configval["commonvaluestep"].get())
			i = round(i,2)
			series.append(stval)

		return self.rangeline(series)

	def createrepeatinfo(self,varvalue,repeatidx,myvarinfo):

		# self.log["applog"].debug("Print from createrepeatinfo for myvarinfo")
		
		# self.log["applog"].debug(myvarinfo)
		# self.log["applog"].debug(repeatidx)


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

		#################################################################################################################3333333			
		# This procedure is created to ship all column to right hand side in order to show current block in left handside.
		#################################################################################################################3333333			

		# if repeatidx > 0 :
		# 	repeatstep=0
		# 	print("enterto repeatidx ")
		# 	rowelement=0
		# 	while (repeatidx>repeatstep):
		# 		print("repeatstep")

		# 		for vname,valitem in self.labeldisplay[varvalue][repeatstep].items():
		# 			print(vname)
		# 			print(valitem.grid_info()['column'])
		# 			print(valitem.grid_info()['row'])

		# 			# self.labeldisplay[varvalue][repeatidx][varelement].grid(row=rowid,column=(j-4+int(repeatidx)*6),sticky="s"+"e"+"w",pady=5)
		# 			# valiiem.grid_propagate(1)
		# 			# valitem.columnconfigure(valitem.grid_info()['column']+6,weight=12)
		# 			if rowelement==5:
		# 				print("rowelement")
		# 				print(rowelement)
		# 				valitem.grid(row=valitem.grid_info()['row'],column=valitem.grid_info()['column']+5,sticky="n"+"e"+"w",pady=15)

		# 			else:	
		# 				valitem.grid(row=valitem.grid_info()['row'],column=valitem.grid_info()['column']+5,sticky="n"+"e"+"w")
		# 				rowelement=rowelement+1
		# 				print("case else of rowelement")
		# 				print(rowelement)
		# 			# valitem.columnconfigure(valitem.grid_info()['column']+6,weight=2)

		# 		repeatstep=repeatstep+1
		# 	repeatidx=0
			# exit()
			# self.canvas.update()

		#########################################################
		# End of procedure ship right hand side.
		#########################################################



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

	# def getRangeData(self):
	# 	print("print rangedata")

	# 	return self.rangeData
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
		# print("\n$$$Print label orderno line 627 tkconsole.py in def monomatch")
		# print(label,orderno)
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

			# self.output.insert(tk.END,self.timenow.strftime("%Y-%m-%d %H:%M:%S ") + str(txtmsg + "\n"))
			self.output.insert(tk.END,self.timenow.strftime("%H:%M:%S ") + str(txtmsg + "\n"))
			
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
			# self.loginSet=[
			# 			broketxt,
			# 			usertxt,
			# 			passtxt,
						
			# 			]
			# for child in self.frameLoginRT.winfo_children():
			# 	child.configure(state='disable')
			# # exit()

			self.loginSet=PackSelModel.getloginDefault()
			
			# self.log["console"].debug(self.loginSet)
			# print(self.loginSet)
			self.log["applog"].info("Execute Login")

			self.configval["stockpin"].set(self.loginSet["pinId"])
			# print(self.configval["stockpin"].get())


			self.mybot.threadlogin(self.loginSet)

	def configparams(self):
		# print("############# config parameter ###################")
		# self.log=log
		myconfigparamsresult = configparams(self.configval,self.log)
		# pass


	def tkviewconfig(self):
		viewresult=viewconfig(self.configval)

	def loginconfig(self):
		myloginresult=loginconfig(self.log)

	def unitTest(self):


		myunitTest=unitTest(self)

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
						# logger.debug("stock has been updated !!!!!!!!!!!! tkconsole.py line 727 def Refresher")
						# controlorder={"ordermode":"buybybot","firstbuy":"yes"}
						# self.mybot.myplugins.order(controlorder,{},self.mybot.order)

						self.txtout("Value Change : " + tempdict["stockvalue"])
						lblstockvalue=tempdict["stockvalue"] # get value from queue
						if lblstockvalue in self.labeldisplay:
							self.flash(self.labeldisplay[lblstockvalue][lblstockvalue],9,"green")
				# self.mybot.myqueue.join()
				if "monitorstock" in tempdict:
						self.log["applog"].debug("Monitor the following tempdict and self.configval")
						self.log["applog"].debug( tempdict["monitorstock"].upper())
						self.log["applog"].debug(self.configval["monitorstock"].get().upper())
						if tempdict["monitorstock"].upper()==self.configval["monitorstock"].get().upper():
							self.configval["monitorstock"].set(tempdict["monitorstock"].upper())





			if not self.mybot.mycollectqueues["qrefresh"].empty() :
				chkrefresh=self.mybot.mycollectqueues["qrefresh"].get()
				# print("check refresh , line 710, tkconsole.py")
				# print(chkrefresh)
				if chkrefresh["qrefresh"]=="refreshtk" and chkrefresh["doupdatetk"] != None :

					self.log["applog"].debug("Do update refresh GUI tk according to queue with qrefresh qrefresh=refreshtk and chkrefresh != None")
					self.log["applog"].debug(chkrefresh)
					# print ("\n !!! Print data to do update refresh tkinter here !!!!! tkconsole.py line 757 in def Refresher")
					# print(chkrefresh)

					# L=chkrefresh["doupdatetk"]
					# chkrefresh["doupdatetk"]=list(filter(None.__ne__, chkrefresh["doupdatetk"]))
					# print(chkrefresh["doupdatetk"])
					# print("finish///....")
					
					for rowupdata in chkrefresh["doupdatetk"] :
						
						# print("\nprint doupdatetk file tkconsole.py line 722 in def Refresher")
						# print(chkrefresh["doupdatetk"])
						# self.log["applog"].debug()

						if chkrefresh["doupdatetk"]=="NOUPDATE":
							break
						
						# print(self.myvarasso)
						if len(self.myvarasso[rowupdata["price"]]) == 0:

							repeatidx = len(self.myvarasso[rowupdata["price"]])

							self.log["applog"].debug("print repeatidx case of price == 0")
							self.log["applog"].debug(repeatidx)
							
							self.myvarasso[rowupdata["price"]].append(self.createrepeatinfo(rowupdata["price"],
																			repeatidx ,rowupdata))
						else:
							# check if lable already existing then no more create label 
							for chklblorderno in self.myvarasso[rowupdata["price"]] :
								# print (chklblorderno["orderno"].get())
								chkorderno=chklblorderno["orderno"].get()
								
								# print ("\ntkconsole.py line 775 compare orderno=" + chkorderno,rowupdata["orderno"])

								if chkorderno == rowupdata["orderno"] :
									ignoreadd=True
									break;
								else:
									ignoreadd=False
								# else:
							if ignoreadd==False:	
								repeatidx=len(self.myvarasso[rowupdata["price"]])


								self.log["applog"].debug("print repeatidx case of ignoreadd == False")
								self.log["applog"].debug(repeatidx)

								resultcreate=self.createrepeatinfo(rowupdata["price"],repeatidx,rowupdata)

								self.myvarasso[rowupdata["price"]].append(resultcreate)

								self.log["applog"].debug("Check myvarasso in ignoreadd==FALSE")
								self.log["applog"].debug(self.myvarasso[rowupdata["price"]])



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
													# print("\n @@@ print labelidx , findlabel,labelcontent line 810 tkconsole.py in def Refresher")
													# print( labelidx,findlabel,labelcontent)
													if labelidx> 0:
														# if labelcontent["orderno"]["text"]=grayorderno:
														# print("\n### print findlabel[labelidx] in line 821 tkconsole.py in def Refresher")
														# print(labelcontent["orderno"])
														self.monomatch(labelcontent,grayorderno)


												# self.flash(,9,"green")



					self.canvas.configure(scrollregion=self.canvas.bbox("all"))
					
				elif chkrefresh["qrefresh"]=="refreshdb":
					# self.log["applog"].debug("If not tk GUI do update back refresh DB according to queue with qrefresh qrefresh=refreshdb")
					# self.log["applog"].debug(chkrefresh)
					self.mybot.mycollectqueues["qrefresh"].put(chkrefresh)

				
			# self.output.tag_config("testb", background="white", foreground="red")
			# self.output.tag_add('testb', 10.0, step)
			# self.after(5, self.Refresher) # every second...
			self.after(250, self.Refresher) # every second...

