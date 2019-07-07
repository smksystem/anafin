import tkinter as tk
import json
from pinkybot.packsel_model import PackSelModel


class loginconfig(tk.Tk):
	"""docstring for loginconfig"""
	def __init__(self, arg):

		
		# super(loginconfig, self).__init__()
		# self.arg = arg
		# self.form = arg 
		tk.Toplevel.__init__(self)


		allquery=self.getloginConfig("all")
		print("Print query set after get all data")


		# print("login config is called")
		# self.geometry("400x700+200+200")
		self.profiletxt=tk.StringVar(value="profile")
		self.broketxt=tk.StringVar(value="013")
		self.usertxt=tk.StringVar(value="014xxxx")
		self.passtxt=tk.StringVar()
		self.pintxt=tk.StringVar(value="33")



		self.attributes('-topmost', 'true')
		self.resizable(False, False)
		self.attributes("-toolwindow",1)
		self.update_idletasks()
		# self.overrideredirect(1)
		# self.wm_attributes('-fullscreen','true')

		# self.unitframe={}

		
		# self.rowbtnframe = tk.Frame(self ,width=50, height =10,background = 'green')
		# self.rowbtnframe.grid(row=0,column=0,sticky="e"+"n"+"s"+"w")

		self.frameLoginRT = tk.Frame(self ,background = 'green')
		# self.frameLoginRT.grid_propagate(0)
		# self.frameLoginRT.grid(row=0,column=0,columnspan=2,sticky="e"+"n"+"s"+"w")
		self.frameLoginRT.grid(row=0,column=0)


		# btnUnitTest=tk.Button(self.frameLoginRT,text="Unit Test",command=self.unitTest)
		# btnUnitTest.grid(row=1,column=2 )

		# labelnamelogin=tk.Label(self.frameLoginRT, text="Login Profile")
		# labelnamelogin.grid(row=0,column=0,sticky="w")

		#############################################################################3

		choices=[]
		for brokechoices in range(len(allquery)):
			print(allquery[brokechoices]["profileId"])
			choices.append(allquery[brokechoices]["profileId"])
		choices.append("New")
		var = tk.StringVar()
		var.set('Profile')

		# choices = ['red', 'green', 'blue', 'yellow','white', 'magenta']
		brokeIdopt = tk.OptionMenu(self.frameLoginRT, var, *choices,command=self.showloginconfig)
		brokeIdopt.grid(row=0,column=0,sticky="w"+"e")
		brokeIdopt['menu'].insert_separator(len(choices)-1)

		#############################################################################3
		enterbrokeid=tk.Entry(self.frameLoginRT,textvariable=self.profiletxt)
		enterbrokeid.grid(row=0,column=1)      


		labelnamebrokeid=tk.Label(self.frameLoginRT, text="Broke ID")
		labelnamebrokeid.grid(row=1,column=0,sticky="w")
	
		enterbrokeid=tk.Entry(self.frameLoginRT,textvariable=self.broketxt)
		enterbrokeid.grid(row=1,column=1)      









		labelnamelogin=tk.Label(self.frameLoginRT, text="Login ID")
		labelnamelogin.grid(row=2,column=0,sticky="w")
		enterloginid=tk.Entry(self.frameLoginRT,textvariable=self.usertxt)
		enterloginid.grid(row=2,column=1)

		labelnamepassword=tk.Label(self.frameLoginRT, text="Password")
		labelnamepassword.grid(row=3,column=0,sticky="w")
		# enterpassword=tk.Entry(self.frameLoginRT,show="*",textvariable=self.passtxt)
		enterpassword=tk.Entry(self.frameLoginRT,textvariable=self.passtxt)

		enterpassword.grid(row=3,column=1)

		labelpinpassword=tk.Label(self.frameLoginRT, text="PIN")
		labelpinpassword.grid(row=4,column=0,sticky="w")
		# enterpin=tk.Entry(self.frameLoginRT,show="*",textvariable=self.pintxt)
		enterpin=tk.Entry(self.frameLoginRT,textvariable=self.pintxt)

		enterpin.grid(row=4,column=1)

		labelcurrentuse=tk.Label(self.frameLoginRT, text="CurrentUse")
		labelcurrentuse.grid(row=5,column=0,sticky="w")

		# enterpin=tk.Entry(self.frameLoginRT,show="*",textvariable=self.pintxt)
		# enterpin.grid(row=5,column=1)
		radioyes=tk.Radiobutton(self.frameLoginRT,text="YES",value="YES",indicatoron=1) #,command=self.chooserunningmode)
		radioyes.grid(row=5,column=1,sticky="w")

		radiono=tk.Radiobutton(self.frameLoginRT,text="NO",value="NO",indicatoron=1) #,command=self.chooserunningmode)
		radiono.grid(row=5,column=1,sticky="e")



		btnSetLoginConfig=tk.Button(self.frameLoginRT,text="Set Login Config",command=self.setLoginConfig)
		btnSetLoginConfig.grid(row=6,column=0,columnspan=1,sticky="w"+"e")

		btnCancel=tk.Button(self.frameLoginRT,text="Cancel",command=self.loginCancel)
		btnCancel.grid(row=6,column=1,columnspan=2,sticky="w"+"e")
		
	def showloginconfig(self,value):
		# print(value)
		# print(self.loginparams)
		self.profiletxt.set(value)
		for profilerun,profilename in enumerate(self.loginparams):
			# print(profilerun,profilename)
			# print(profilerun["profileId"])
			if profilename["profileId"] == value:
				self.broketxt.set(profilename["brokeId"])
				self.usertxt.set(profilename["loginId"])
				self.passtxt.set(profilename["passwordId"])
				self.pintxt.set(profilename["pinId"])



	def setLoginConfig(self):

		print("access set login config button menu")
		loginparams={
						"brokeId":self.broketxt.get(),
						"loginId":self.usertxt.get(),
						"passwordId":self.passtxt.get(),
						"pinId":self.pintxt.get(),
						"profileId":self.profiletxt.get(),
		}
		PackSelModel.updateloginModel(loginparams)

	def loginCancel(self):
		self.destroy()
		
	def getloginConfig(self,brokeId='all'):
		print("load Login Config")
		# brokeId="013"
		self.loginparams= PackSelModel.getloginModel(brokeId)
		print(self.loginparams)
		return self.loginparams