import tkinter as tk
import json
from pinkybot.packsel_model import PackSelModel


class loginconfig(tk.Tk):
	
	def __init__(self, loginlog):

		
		# super(loginconfig, self).__init__()
		# self.arg = arg
		# self.form = arg 
		tk.Toplevel.__init__(self)
		self.log=loginlog


		# print("login config is called")
		# self.geometry("400x700+200+200")
		self.profiletxt=tk.StringVar()
		self.broketxt=tk.StringVar()
		self.usertxt=tk.StringVar()
		self.passtxt=tk.StringVar()
		self.pintxt=tk.StringVar()
		self.defaultprofile=tk.StringVar()


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

		allquery=self.getloginConfig("all")
		self.log["applog"].debug("print query set of log in def __init__ after get all data")
		self.log["applog"].debug(allquery)


		self.choices=[]
		for brokechoices in range(len(allquery)):
			# print(allquery[brokechoices]["profileId"])
			self.choices.append(allquery[brokechoices]["profileId"])
		self.choices.append("New")
		
		self.varmenutxt = tk.StringVar()
		self.varmenutxt.set('Profile')

		# choices = ['red', 'green', 'blue', 'yellow','white', 'magenta']
		self.brokeIdopt = tk.OptionMenu(self.frameLoginRT, self.varmenutxt, *self.choices,command=self.showloginconfig)
		self.brokeIdopt.grid(row=0,column=0,sticky="w"+"e")
		self.brokeIdopt['menu'].insert_separator(len(self.choices)-1)

		#############################################################################3
		enterprofileid=tk.Entry(self.frameLoginRT,textvariable=self.profiletxt)
		enterprofileid.grid(row=0,column=1)      


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
		radioyes=tk.Radiobutton(self.frameLoginRT,text="YES",value="YES",variable=self.defaultprofile,indicatoron=1) #,command=self.chooserunningmode)
		radioyes.grid(row=5,column=1,sticky="w")

		radiono=tk.Radiobutton(self.frameLoginRT,text="NO",value="NO",variable=self.defaultprofile,indicatoron=1) #,command=self.chooserunningmode)
		radiono.grid(row=5,column=1,sticky="e")


		#######################################################################
		##################### Fill initial data from here #####################
		#######################################################################
	
		print("start count database login")
		print(len(allquery))

		if len(allquery)>0:
			self.profiletxt.set(allquery[0]["profileId"])
			self.broketxt.set(allquery[0]["brokeId"])
			self.usertxt.set(allquery[0]["loginId"])
			self.passtxt.set(allquery[0]["passwordId"])
			self.pintxt.set(allquery[0]["pinId"])
			if allquery[0]["currentuseId"]=="YES":
				self.defaultprofile.set("YES")

			elif allquery[0]["currentuseId"]=="NO":
				self.defaultprofile.set("NO")
			else:
				self.defaultprofile.set("UNCHECK")
		#######################################################################
		#######################################################################
		#######################################################################


		btnSetLoginConfig=tk.Button(self.frameLoginRT,text="Set Login Config",command=self.setLoginConfig)
		btnSetLoginConfig.grid(row=6,column=0,columnspan=1,sticky="w"+"e")

		btnDeleteConfig=tk.Button(self.frameLoginRT,text="DeleProfile",command=self.deleteConfig)
		btnDeleteConfig.grid(row=6,column=1,columnspan=1,sticky="w"+"e")


		btnCancel=tk.Button(self.frameLoginRT,text="Cancel",command=self.loginCancel)
		btnCancel.grid(row=6,column=2,columnspan=2,sticky="w"+"e")
		





	def deleteConfig(self):
		brokeId=self.broketxt.get()
		
		# print("Delte Broke ID")

		PackSelModel.deleteloginModel(brokeId)
		self.getloginConfig()



	def showloginconfig(self,value):
		# print("showloginconfig got value below")
		# print(value)
		# print(value.strip())
		# print(self.loginparams)
		# self.profiletxt.set(value)
		


		self.loginparams=self.getloginConfig("all")

		# print(len(self.loginparams))

		if len(self.loginparams)==0 and value.strip() == "New":
			self.profiletxt.set("")
			self.broketxt.set("")
			self.usertxt.set("")
			self.passtxt.set("")
			self.pintxt.set("")
			self.defaultprofile.set("UNSET")

		for profilerun,profilename in enumerate(self.loginparams):
			# print("profileId got parameter below")
			# print(profilename["profileId"].strip())
			if profilename["profileId"].strip() == value.strip():
				# print("found profileId")
				self.varmenutxt.set(profilename["profileId"])
				self.profiletxt.set(profilename["profileId"])
				self.broketxt.set(profilename["brokeId"])
				self.usertxt.set(profilename["loginId"])
				self.passtxt.set(profilename["passwordId"])
				self.pintxt.set(profilename["pinId"])
				if profilename["currentuseId"]=="YES":
					self.defaultprofile.set("YES")

				elif profilename["currentuseId"]=="NO":
					self.defaultprofile.set("NO")
				else:
					self.defaultprofile.set("UNCHECK")
			elif value.strip()=="New":
				# print("New choices is selected.")
				self.profiletxt.set("")
				self.broketxt.set("")
				self.usertxt.set("")
				self.passtxt.set("")
				self.pintxt.set("")
				self.defaultprofile.set("UNSET")
				# print("New choices is selected")




	def setLoginConfig(self):

		# print("access set login config button menu")
		
		loginparams={
						"profileId":self.profiletxt.get(),
						"brokeId":self.broketxt.get(),
						"loginId":self.usertxt.get(),
						"passwordId":self.passtxt.get(),
						"pinId":self.pintxt.get(),
						"currentuseId":self.defaultprofile.get(),
		}
		updateresult=PackSelModel.updateloginModel(loginparams)
		if updateresult=="UPDATED":

			updateparams=self.getloginConfig()
		else:

			self.brokeIdopt['menu'].insert_command(0,label=updateresult,command=lambda:self.showloginconfig(updateresult))	

	def loginCancel(self):
		self.destroy()
		
	def getloginConfig(self,profileId='all'):
		
		self.log["applog"].info ("login config is loaded from databases")

		self.loginparams= PackSelModel.getloginModel(profileId)
		return self.loginparams