import tkinter as tk
class configparams(tk.Tk):
	"""docstring for parameterconfigclass"""
	def __init__(self,arg):
		# super(parameterconfigclass, self).__init__()
		self.arg = arg
		print("Access to config params")
		tk.Toplevel.__init__(self)


		self.profiletxt=tk.StringVar()

		self.monitortxt=tk.StringVar()
		self.rangetxt=tk.StringVar()
		
		# self.usertxt=tk.StringVar()
		# self.passtxt=tk.StringVar()
		# self.pintxt=tk.StringVar()
		# self.defaultprofile=tk.StringVar()






		self.frameConfig = tk.Frame(self ,background = 'green')
		self.frameConfig.grid(row=0,column=0)


		

		#############################################################################3

		choices=[]
		allquery=["test","test2"]
		for brokechoices in range(len(allquery)):
			print(allquery)
			choices.append(allquery)
		choices.append("New")
		var = tk.StringVar()
		var.set('Choose Profile')

		# choices = ['red', 'green', 'blue', 'yellow','white', 'magenta']
		# brokeIdopt = tk.OptionMenu(self.frameConfig, var, *choices,command=self.showloginconfig)
		profileIdopt = tk.OptionMenu(self.frameConfig, var, *choices)

		profileIdopt.grid(row=0,column=0,sticky="w"+"e")
		#############################################################################3

		enterprofileid=tk.Entry(self.frameConfig,textvariable=self.profiletxt)
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
		self.rangeplanMenu1 = tk.OptionMenu(self.frameConfig, self.rangeplanVar, *optionList) #,command=self.doMenuRange)
		self.rangeplanMenu1.grid(row=1,column=0,sticky="w")


		enterrange=tk.Entry(self.frameConfig,textvariable=self.rangetxt)

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

		entermonitor=tk.Entry(self.frameConfig,textvariable=self.monitortxt)
		entermonitor.grid(row=3,column=1)
		#######################################################################

		labelmonitor=tk.Label(self.frameConfig, text="Volumn Step")
		labelmonitor.grid(row=4,column=0,sticky="w")

		entermonitor=tk.Entry(self.frameConfig,textvariable=self.monitortxt)
		entermonitor.grid(row=4,column=1)
		#######################################################################
		labelmonitor=tk.Label(self.frameConfig, text="Profit Step")
		labelmonitor.grid(row=5,column=0,sticky="w")

		entermonitor=tk.Entry(self.frameConfig,textvariable=self.monitortxt)
		entermonitor.grid(row=5,column=1)
		#######################################################################
		labelmonitor=tk.Label(self.frameConfig, text="Top Value Range")
		labelmonitor.grid(row=6,column=0,sticky="w")

		entermonitor=tk.Entry(self.frameConfig,textvariable=self.monitortxt)
		entermonitor.grid(row=6,column=1)
		#######################################################################
		labelmonitor=tk.Label(self.frameConfig, text="Start Value Buy")
		labelmonitor.grid(row=7,column=0,sticky="w")

		entermonitor=tk.Entry(self.frameConfig,textvariable=self.monitortxt)
		entermonitor.grid(row=7,column=1)
		#######################################################################
		labelmonitor=tk.Label(self.frameConfig, text="Floor Value Range")
		labelmonitor.grid(row=8,column=0,sticky="w")

		entermonitor=tk.Entry(self.frameConfig,textvariable=self.monitortxt)
		entermonitor.grid(row=8,column=1)
		#######################################################################








		#######################################################################
		#######################################################################
		#######################################################################



		btnSetLoginConfig=tk.Button(self.frameConfig,text="Set Login Config") #,command=self.setLoginConfig)
		btnSetLoginConfig.grid(row=9,column=0,columnspan=1,sticky="w"+"e")

		btnDeleteConfig=tk.Button(self.frameConfig,text="DeleProfile") #,command=self.deleteConfig)
		btnDeleteConfig.grid(row=9,column=1,columnspan=1,sticky="w"+"e")


		btnCancel=tk.Button(self.frameConfig,text="Cancel") #,command=self.loginCancel)
		btnCancel.grid(row=9,column=2,columnspan=2,sticky="w"+"e")

		