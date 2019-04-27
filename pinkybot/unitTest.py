import tkinter as tk
import json
class unitTest(tk.Tk):
	"""docstring for unitTest"""
	def __init__(self, arg):
		# super(unitTest, self).__init__()
		print("initialize unit test")
		self.form = arg 

		tk.Toplevel.__init__(self)
		self.geometry("800x200")

		rowunitframe = tk.Frame(self ,width=50, height =10,background = 'red')
		rowunitframe.grid(row=0,column=1,sticky="e"+"n"+"s"+"w")

		# postfile=open("stockpost.txt","r")

		postfile=open("stockpost.txt","r+")
	
		test= postfile.readlines()
		tempwrite=[]	
		numberid='0'
		for line in test:
		# print ("each line of line views.py line 38")
			mydic=json.loads(line)
			# tempwrite.append(mydic)
			if (len(mydic)!= 0):
				print(mydic)
				for myidx,(colid,colval) in enumerate(mydic.items()):
					print(colid,colval)

					lbl=tk.Label(self, text=colid + "=")
					lblval=tk.Label(self,text=colval)

					lbl.grid(row=0,column=myidx)
					lblval.grid(row=0,column=myidx+2)

				# tempwrite[-1]["price"]=="4.72":

					# tempwrite[-1]["status"]="Pending(S)"  # else False




		# postfile.truncate(0) // empty file
		postfile.close()

		unitframectl=tk.Frame(self,width=50, height =10,background = 'blue')
		unitframectl.grid(row=2,column=1,sticky="e"+"n"+"s"+"w")      

		btnset=tk.Button(self,text="Set",command=self.btntestunit, width = 10,height=2)
		btnset.grid(row=2,column=0,sticky="w")
		
	def btntestunit(self):
		pass