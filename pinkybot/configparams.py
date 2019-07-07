import tkinter as tk
class configparams(tk.Tk):
	"""docstring for parameterconfigclass"""
	def __init__(self,arg):
		# super(parameterconfigclass, self).__init__()
		self.arg = arg
		print("Access to config params")
		tk.Toplevel.__init__(self)

		self.frameConfig = tk.Frame(self ,background = 'green')
		self.frameConfig.grid(row=0,column=0)


		lblconfig=tk.Label(self.frameConfig, text="Config Profile")
		lblconfig.grid(row=0,column=0,sticky="w")

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
		brokeIdopt = tk.OptionMenu(self.frameConfig, var, *choices)

		brokeIdopt.grid(row=0,column=1,sticky="w"+"e")
		#############################################################################3


	
		