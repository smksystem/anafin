import tkinter as tk
from pinkybot.packsel_model import PackSelModel
class viewconfig(tk.Tk):
	"""docstring for parameterconfigclass"""
	def __init__(self,configparams):
		# super(parameterconfigclass, self).__init__()
		# self.arg = arg
		print("Access to view config params")
		tk.Toplevel.__init__(self)


		# configparams= PackSelModel.getDefaultConfig()
		# print(configparams)
		print(configparams)

		frameviewconfig = tk.Frame(self ,background = 'green')
		frameviewconfig.grid(row=0,column=0)
		#######################################################################################

		for labelidx,(labelkey,labelcontent) in enumerate(configparams.items()):
			print(labelidx,labelkey,labelcontent.get())
			lbldummy=tk.Label(frameviewconfig, text=labelkey)
			lbldummy.grid(row=labelidx,column=0,sticky="w")

			lblplanname=tk.Label(frameviewconfig, text=labelcontent.get())
			lblplanname.grid(row=labelidx,column=1,sticky="w")

		
		btnviewok=tk.Button(frameviewconfig,text="Ok",command=self.viewcancel)
		btnviewok.grid(row=labelidx,column=0,columnspan=2,sticky="w"+"e")


	def viewcancel(self):
		self.destroy()