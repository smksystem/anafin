import tkinter as tk
from pinkybot.packsel_model import PackSelModel
class configparams(tk.Tk):
	"""docstring for parameterconfigclass"""
	def __init__(self,configval,mylog):
		# super(parameterconfigclass, self).__init__()
		self.configval = configval
		self.log=mylog
		self.log["console"].debug(configval)

		# print("Access to config params")
		tk.Toplevel.__init__(self)


		####################################################################################################
		############### define later if need to reuse this parameter or not by pass parameter from database packsel_model.py ?????????? #####################
		####################################################################################################

		self.plannametxt=tk.StringVar()  #### can use self.configval[""]
		self.rangeseltxt=tk.StringVar()
		self.monitortxt=tk.StringVar()
		self.investtxt=tk.StringVar()
		# self.remaininvest=tk.StringVar()
		self.volumesteptxt=tk.StringVar()
		self.profitsteptxt=tk.StringVar()
		self.topvaluebuytxt=tk.StringVar()
		self.startvaluebuytxt=tk.StringVar()
		self.stopvaluebuytxt=tk.StringVar()

		self.floorvaluebuytxt=tk.StringVar()
		self.pluginfiletxt=tk.StringVar()

		self.defaultplanname=tk.StringVar()
		self.varcheckbuy=tk.StringVar()
		self.varcheckdefault=tk.StringVar()


		self.attributes('-topmost', 'true')
		self.resizable(False, False)
		self.attributes("-toolwindow",1)
		self.update_idletasks()



		self.frameConfig = tk.Frame(self ,background = 'green')
		self.frameConfig.grid(row=0,column=0)


		initconfigvar=self.getparamsConfig()
		# print(initconfigvar)

		#############################################################################3

		choices=[]
		# initconfigvar
		for planchoices in range(len(initconfigvar)):
			# print(allquery)
			choices.append(initconfigvar[planchoices]["planname"])

			# choices.append(allquery)
		choices.append("New")
		self.var = tk.StringVar()
		self.var.set(initconfigvar[0]["planname"])

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
		labelmonitor=tk.Label(self.frameConfig, text="Top Value Buy")
		labelmonitor.grid(row=6,column=0,sticky="w")

		entermonitor=tk.Entry(self.frameConfig,textvariable=self.topvaluebuytxt)
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
		labelmonitor=tk.Label(self.frameConfig, text="Floor Value Buy")
		labelmonitor.grid(row=9,column=0,sticky="w")

		entermonitor=tk.Entry(self.frameConfig,textvariable=self.floorvaluebuytxt)
		entermonitor.grid(row=9,column=1)

		#######################################################################
		labelpluginfile=tk.Label(self.frameConfig, text="plugin file")
		labelpluginfile.grid(row=10,column=0,sticky="w")

		enterpluginfile=tk.Entry(self.frameConfig,textvariable=self.pluginfiletxt)
		enterpluginfile.grid(row=10,column=1)

		#######################################################################

		self.checkdefault = tk.Checkbutton(self.frameConfig, text="Default", variable=self.varcheckdefault,offvalue="NO",onvalue="YES")
		self.checkdefault.grid(row=11,column=1)

		if initconfigvar[0]["currentuseId"]=="YES":
			self.checkdefault.select()
		elif initconfigvar[0]["currentuseId"]=="NO":
			self.checkdefault.deselect()


		#######################################################################

		self.checkbuy = tk.Checkbutton(self.frameConfig, text="BuyFlag", variable=self.varcheckbuy,offvalue="NO",onvalue="YES")
		self.checkbuy.grid(row=11,column=0)
		# print(self.checkbuy.get())
		if initconfigvar[0]["firstbuyflag"]=="YES":
			self.checkbuy.select()
		elif initconfigvar[0]["firstbuyflag"]=="NO":
			self.checkbuy.deselect()



		#######################################################################
		##################### Fill initial data from here #####################
		#######################################################################
	
		# print("start count database login")
		# print(len(allquery))

		if len(initconfigvar)>0:
			self.plannametxt.set(initconfigvar[0]["planname"])
			self.rangeseltxt.set(initconfigvar[0]["rangeselect"])
			self.monitortxt.set(initconfigvar[0]["monitorstock"])
			self.investtxt.set(initconfigvar[0]["initinvest"])
			self.volumesteptxt.set(initconfigvar[0]["volumestep"])
			self.profitsteptxt.set(initconfigvar[0]["profitstep"])
			self.topvaluebuytxt.set(initconfigvar[0]["topvaluebuy"])
			self.startvaluebuytxt.set(initconfigvar[0]["startvaluebuy"])
			self.stopvaluebuytxt.set(initconfigvar[0]["stopvaluebuy"])

			self.floorvaluebuytxt.set(initconfigvar[0]["floorvaluebuy"])
			self.pluginfiletxt.set(initconfigvar[0]["pluginfile"])

		#######################################################################
		#######################################################################
		#######################################################################



		btnSetLoginConfig=tk.Button(self.frameConfig,text="Set Login Config",command=self.setparamsConfig)
		btnSetLoginConfig.grid(row=12,column=0,columnspan=1,sticky="w"+"e")

		btnDeleteConfig=tk.Button(self.frameConfig,text="DeleProfile",command=self.deleteConfig)
		btnDeleteConfig.grid(row=12,column=1,columnspan=1,sticky="w"+"e")


		btnCancel=tk.Button(self.frameConfig,text="Cancel",command=self.ConfigCancel)
		btnCancel.grid(row=12,column=2,columnspan=2,sticky="w"+"e")

	# def checkcommand(self):
	# 	print(self.checkbuy.get())
	def selectlistrange(self,value):
		# print("def selectlistrange enter")
		# print(value)
		valueparams=value.split()
		# print(valueparams[0])
		self.rangeseltxt.set(valueparams[0])

	def showitemconfig(self,value):

		confitemparams=self.getparamsConfig(value)
		self.var.set(value)
		

		# print(value,idxm,entry)

		# print("config item parameter")
		# print(confitemparams)
		if len(confitemparams) == 1 :
			self.plannametxt.set(confitemparams[0]["planname"])
			self.rangeseltxt.set(confitemparams[0]["rangeselect"])
			self.monitortxt.set(confitemparams[0]["monitorstock"])
			self.investtxt.set(confitemparams[0]["initinvest"])
			self.volumesteptxt.set(confitemparams[0]["volumestep"])
			self.profitsteptxt.set(confitemparams[0]["profitstep"])
			self.topvaluebuytxt.set(confitemparams[0]["topvaluebuy"])
			self.startvaluebuytxt.set(confitemparams[0]["startvaluebuy"])
			self.stopvaluebuytxt.set(confitemparams[0]["stopvaluebuy"])
			self.floorvaluebuytxt.set(confitemparams[0]["floorvaluebuy"])
			
			self.pluginfiletxt.set(confitemparams[0]["pluginfile"])

			if confitemparams[0]["firstbuyflag"]=="YES":
				self.checkbuy.select()
			elif confitemparams[0]["firstbuyflag"]=="NO":
				self.checkbuy.deselect()

			if confitemparams[0]["currentuseId"]=="YES":
				self.checkdefault.select()
			elif confitemparams[0]["currentuseId"]=="NO":
				self.checkdefault.deselect()
	


		elif len(confitemparams)==0 and value=="New":
			# print("This is new for configuration parameter")
			self.plannametxt.set("")
			self.rangeseltxt.set("")
			self.monitortxt.set("")
			self.investtxt.set("")
			self.volumesteptxt.set("")
			self.profitsteptxt.set("")
			self.topvaluebuytxt.set("")
			self.startvaluebuytxt.set("")
			self.stopvaluebuytxt.set("")
			self.floorvaluebuytxt.set("")
			self.pluginfiletxt.set("")

			self.checkdefault.deselect()
			self.checkbuy.deselect()


	def setparamsConfig(self):
		# print("put parameter config to database")
		confparams={
					"planname":self.plannametxt.get(),
					"rangeselect":self.rangeseltxt.get(),
					"monitorstock":self.monitortxt.get(),

					"initinvest":self.investtxt.get(),
					"volumestep":self.volumesteptxt.get(),
					"profitstep":self.profitsteptxt.get(),
					"topvaluebuy":self.topvaluebuytxt.get(),
					"startvaluebuy":self.startvaluebuytxt.get(),
					"stopvaluebuy":self.stopvaluebuytxt.get(),
					"floorvaluebuy":self.floorvaluebuytxt.get(),
					"pluginfile":self.pluginfiletxt.get(),

					"firstbuyflag":self.varcheckbuy.get(),
					"currentuseId":self.varcheckdefault.get(),

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
			# print("plan name =1 ")
			# self.plannameIdopt['menu'].delete(planname)
			# self.showitemconfig(self.plannameIdopt['menu'].index('end')-1)
			self.showitemconfig(0)

			idxm=self.plannameIdopt['menu'].index("end")
		# print(idxm)
			for iplan in range(idxm-1):
				# print(i)
				entry= self.plannameIdopt['menu'].entrycget(iplan, "label")
				print("entry")
				print(entry)
				if entry==planname:
					print("found!")
					idxm=self.plannameIdopt['menu'].delete(iplan)
					break

			# print(idxm)
			# self.plannameIdopt['menu'].delete(idxm-1)

		# self.getloginConfig()

	def ConfigCancel(self):
		self.destroy()