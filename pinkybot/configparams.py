import tkinter as tk
from pinkybot.packsel_model import PackSelModel
class configparams(tk.Tk):
	"""docstring for parameterconfigclass"""
	def __init__(self,arg):
		# super(parameterconfigclass, self).__init__()
		self.arg = arg
		print("Access to config params")
		tk.Toplevel.__init__(self)


		self.plannametxt=tk.StringVar()
		self.rangeseltxt=tk.StringVar()
		self.monitortxt=tk.StringVar()
		self.investtxt=tk.StringVar()
		self.volumesteptxt=tk.StringVar()
		self.profitsteptxt=tk.StringVar()
		self.topvaluerangetxt=tk.StringVar()
		self.startvaluebuytxt=tk.StringVar()
		self.stopvaluebuytxt=tk.StringVar()

		self.floorvaluerangetxt=tk.StringVar()

		self.defaultplanname=tk.StringVar()
		self.checkbuy=tk.StringVar()
		self.checkdefault=tk.StringVar()
		

		self.attributes('-topmost', 'true')
		self.resizable(False, False)
		self.attributes("-toolwindow",1)
		self.update_idletasks()



		self.frameConfig = tk.Frame(self ,background = 'green')
		self.frameConfig.grid(row=0,column=0)


		self.configvar=self.getparamsConfig()
		# print(self.configvar)

		#############################################################################3

		choices=[]
		# self.configvar
		for planchoices in range(len(self.configvar)):
			# print(allquery)
			choices.append(self.configvar[planchoices]["planname"])

			# choices.append(allquery)
		choices.append("New")
		self.var = tk.StringVar()
		self.var.set(self.configvar[0]["planname"])

		# choices = ['red', 'green', 'blue', 'yellow','white', 'magenta']
		# brokeIdopt = tk.OptionMenu(self.frameConfig, var, *choices,command=self.showloginconfig)
		self.plannameIdopt = tk.OptionMenu(self.frameConfig, self.var, *choices,command=self.showitemconfig)
		self.plannameIdopt.grid(row=0,column=0,sticky="w"+"e")
		self.plannameIdopt['menu'].insert_separator(len(choices)-1)
		#############################################################################3

		enterprofileid=tk.Entry(self.frameConfig,textvariable=self.plannametxt)
		enterprofileid.grid(row=0,column=1)  
		#######################################################################


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
			optionList.append(myrange +" "+ startfrom+"-"+stopfrom + " step " +stepfrom)

		self.rangeplanVar=tk.StringVar()
		self.rangeplanVar.set("Range Plan") # default choice
		self.rangeplanMenu1 = tk.OptionMenu(self.frameConfig, self.rangeplanVar, *optionList,command=self.selectlistrange)
		self.rangeplanMenu1.grid(row=1,column=0,sticky="w")


		enterrange=tk.Entry(self.frameConfig,textvariable=self.rangeseltxt)

		enterrange.grid(row=1,column=1)

		#######################################################################
		########################## Parameter config ###########################
		#######################################################################
		#######################################################################
		labelmonitor=tk.Label(self.frameConfig, text="Monitor")
		labelmonitor.grid(row=2,column=0,sticky="w")

		entermonitor=tk.Entry(self.frameConfig,textvariable=self.monitortxt)
		entermonitor.grid(row=2,column=1)
		#######################################################################
		labelmonitor=tk.Label(self.frameConfig, text="Invest Cost")
		labelmonitor.grid(row=3,column=0,sticky="w")

		entermonitor=tk.Entry(self.frameConfig,textvariable=self.investtxt)
		entermonitor.grid(row=3,column=1)
		#######################################################################

		labelmonitor=tk.Label(self.frameConfig, text="Volumn Step")
		labelmonitor.grid(row=4,column=0,sticky="w")

		entermonitor=tk.Entry(self.frameConfig,textvariable=self.volumesteptxt)
		entermonitor.grid(row=4,column=1)
		#######################################################################
		labelmonitor=tk.Label(self.frameConfig, text="Profit Step")
		labelmonitor.grid(row=5,column=0,sticky="w")

		entermonitor=tk.Entry(self.frameConfig,textvariable=self.profitsteptxt)
		entermonitor.grid(row=5,column=1)
		#######################################################################
		labelmonitor=tk.Label(self.frameConfig, text="Top Value Range")
		labelmonitor.grid(row=6,column=0,sticky="w")

		entermonitor=tk.Entry(self.frameConfig,textvariable=self.topvaluerangetxt)
		entermonitor.grid(row=6,column=1)
		#######################################################################
		labelmonitor=tk.Label(self.frameConfig, text="Start Value Buy")
		labelmonitor.grid(row=7,column=0,sticky="w")

		entermonitor=tk.Entry(self.frameConfig,textvariable=self.startvaluebuytxt)
		entermonitor.grid(row=7,column=1)
		#######################################################################
		labelmonitor=tk.Label(self.frameConfig, text="Stop Value Buy")
		labelmonitor.grid(row=8,column=0,sticky="w")

		entermonitor=tk.Entry(self.frameConfig,textvariable=self.stopvaluebuytxt)
		entermonitor.grid(row=8,column=1)
		#######################################################################
		labelmonitor=tk.Label(self.frameConfig, text="Floor Value Range")
		labelmonitor.grid(row=9,column=0,sticky="w")

		entermonitor=tk.Entry(self.frameConfig,textvariable=self.floorvaluerangetxt)
		entermonitor.grid(row=9,column=1)
		#######################################################################

		checkdefault = tk.Checkbutton(self.frameConfig, text="Default", variable=self.checkdefault)
		checkdefault.grid(row=10,column=1)

		# labeldefault=tk.Label(self.frameConfig, text="Default")
		# labeldefault.grid(row=10,column=1,sticky="w")

		# radioyes=tk.Radiobutton(self.frameConfig,text="YES",value="YES",variable=self.defaultplanname,indicatoron=1) #,command=self.chooserunningmode)
		# radioyes.grid(row=10,column=1,sticky="e")

		# radiono=tk.Radiobutton(self.frameConfig,text="NO",value="NO",variable=self.defaultplanname,indicatoron=1) #,command=self.chooserunningmode)
		# radiono.grid(row=10,column=2,sticky="e")
		#######################################################################

		checkbuy = tk.Checkbutton(self.frameConfig, text="BuyFlag", variable=self.checkbuy)
		checkbuy.grid(row=10,column=0)

		#######################################################################
		##################### Fill initial data from here #####################
		#######################################################################
	
		# print("start count database login")
		# print(len(allquery))

		if len(self.configvar)>0:
			self.plannametxt.set(self.configvar[0]["planname"])
			self.rangeseltxt.set(self.configvar[0]["rangeselect"])
			self.monitortxt.set(self.configvar[0]["monitorstock"])
			self.investtxt.set(self.configvar[0]["initinvest"])
			self.volumesteptxt.set(self.configvar[0]["volumestep"])
			self.profitsteptxt.set(self.configvar[0]["profitstep"])
			self.topvaluerangetxt.set(self.configvar[0]["topvaluerange"])
			self.startvaluebuytxt.set(self.configvar[0]["startvaluebuy"])
			self.stopvaluebuytxt.set(self.configvar[0]["stopvaluebuy"])

			self.floorvaluerangetxt.set(self.configvar[0]["floorvaluerange"])

			# if self.configvar[0]["currentuseId"]=="YES":
			# 	self.defaultprofile.set("YES")

			# elif self.configvar[0]["currentuseId"]=="NO":
			# 	self.defaultprofile.set("NO")
			# else:
			# 	self.defaultprofile.set("UNCHECK")
		

		#######################################################################
		#######################################################################
		#######################################################################



		btnSetLoginConfig=tk.Button(self.frameConfig,text="Set Login Config",command=self.setparamsConfig)
		btnSetLoginConfig.grid(row=12,column=0,columnspan=1,sticky="w"+"e")

		btnDeleteConfig=tk.Button(self.frameConfig,text="DeleProfile",command=self.deleteConfig)
		btnDeleteConfig.grid(row=12,column=1,columnspan=1,sticky="w"+"e")


		btnCancel=tk.Button(self.frameConfig,text="Cancel",command=self.ConfigCancel)
		btnCancel.grid(row=12,column=2,columnspan=2,sticky="w"+"e")
	
	def selectlistrange(self,value):
		# print("def selectlistrange enter")
		# print(value)
		valueparams=value.split()
		# print(valueparams[0])
		self.rangeseltxt.set(valueparams[0])

	def showitemconfig(self,value):
		confitemparams=self.getparamsConfig(value)
		self.var.set(value)
		# print("config item parameter")
		# print(len(confitemparams))
		if len(confitemparams) == 1 :
			self.plannametxt.set(confitemparams[0]["planname"])
			self.rangeseltxt.set(confitemparams[0]["rangeselect"])
			self.monitortxt.set(confitemparams[0]["monitorstock"])
			self.investtxt.set(confitemparams[0]["initinvest"])
			self.volumesteptxt.set(confitemparams[0]["volumestep"])
			self.profitsteptxt.set(confitemparams[0]["profitstep"])
			self.topvaluerangetxt.set(confitemparams[0]["topvaluerange"])
			self.startvaluebuytxt.set(confitemparams[0]["startvaluebuy"])
			self.stopvaluebuytxt.set(confitemparams[0]["stopvaluebuy"])
			self.floorvaluerangetxt.set(confitemparams[0]["floorvaluerange"])

		elif len(confitemparams)==0 and value=="New":
			# print("This is new for configuration parameter")
			self.plannametxt.set("")
			self.rangeseltxt.set("")
			self.monitortxt.set("")
			self.investtxt.set("")
			self.volumesteptxt.set("")
			self.profitsteptxt.set("")
			self.topvaluerangetxt.set("")
			self.startvaluebuytxt.set("")
			self.stopvaluebuytxt.set("")
			self.floorvaluerangetxt.set("")
	def setparamsConfig(self):
		# print("put parameter config to database")
		confparams={
					"planname":self.plannametxt.get(),
					"rangeselect":self.rangeseltxt.get(),
					"monitorstock":self.monitortxt.get(),

					"initinvest":self.investtxt.get(),
					"volumestep":self.volumesteptxt.get(),
					"profitstep":self.profitsteptxt.get(),
					"topvaluerange":self.topvaluerangetxt.get(),
					"startvaluebuy":self.startvaluebuytxt.get(),
					"stopvaluebuy":self.stopvaluebuytxt.get(),
					"floorvaluerange":self.floorvaluerangetxt.get(),
		}
		updateresult=PackSelModel.updateconfigModel(confparams)
		# print(updateresult)

		if updateresult!="__UpDated__":
			self.var.set(updateresult)
			self.plannameIdopt['menu'].insert_command(self.plannameIdopt['menu'].index('end')-1,
													label=updateresult,
													command=lambda:self.showitemconfig(updateresult))	

	def getparamsConfig(self,profileId='all'):
		
		# self.log["applog"].info ("login config is loaded from databases")

		configparams= PackSelModel.getConfigModel(profileId)
		return configparams

	def deleteConfig(self):

		planname=self.plannametxt.get()
		resultdelete=PackSelModel.deleteconfigModel(planname)
		if resultdelete==1:
			self.showitemconfig(0)
		# self.getloginConfig()

	def ConfigCancel(self):
		self.destroy()