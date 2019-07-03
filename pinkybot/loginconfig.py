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
		# print("login config is called")
		# self.geometry("400x700+200+200")
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

	
		labelnamebrokeid=tk.Label(self.frameLoginRT, text="Broke ID")
		labelnamebrokeid.grid(row=0,column=0,sticky="w")
		enterbrokeid=tk.Entry(self.frameLoginRT,textvariable=self.broketxt)
		enterbrokeid.grid(row=0,column=1)      

		labelnamelogin=tk.Label(self.frameLoginRT, text="Login ID")
		labelnamelogin.grid(row=1,column=0,sticky="w")
		enterloginid=tk.Entry(self.frameLoginRT,textvariable=self.usertxt)
		enterloginid.grid(row=1,column=1)

		labelnamepassword=tk.Label(self.frameLoginRT, text="Password")
		labelnamepassword.grid(row=2,column=0,sticky="w")
		enterpassword=tk.Entry(self.frameLoginRT,show="*",textvariable=self.passtxt)
		enterpassword.grid(row=2,column=1)

		labelpinpassword=tk.Label(self.frameLoginRT, text="PIN")
		labelpinpassword.grid(row=3,column=0,sticky="w")
		enterpin=tk.Entry(self.frameLoginRT,show="*",textvariable=self.pintxt)
		enterpin.grid(row=3,column=1)

		btnSetLoginConfig=tk.Button(self.frameLoginRT,text="Set Login Config",command=self.setLoginConfig)
		btnSetLoginConfig.grid(row=4,column=0,columnspan=1,sticky="w"+"e")

		btnCancel=tk.Button(self.frameLoginRT,text="Cancel",command=self.loginCancel)
		btnCancel.grid(row=4,column=1,columnspan=2,sticky="w"+"e")
		
		self.getloginConfig()

	def setLoginConfig(self):

		print("access set login config button menu")
		loginparams={
						"brokeId":self.broketxt.get(),
						"loginId":self.usertxt.get(),
						"passwordId":self.passtxt.get(),
						"pinId":self.pintxt.get(),
		}
		PackSelModel.updateloginModel(loginparams)

	def loginCancel(self):
		self.destroy()
	def getloginConfig(self):
		print("load Login Config")
		brokeId="013"
		loginparams= PackSelModel.getloginModel(brokeId)
		print(loginparams)