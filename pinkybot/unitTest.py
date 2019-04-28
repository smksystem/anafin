import tkinter as tk
import json
class unitTest(tk.Tk):
	"""docstring for unitTest"""
	def __init__(self, arg):
		# super(unitTest, self).__init__()
		print("initialize unit test")
		self.form = arg 

		tk.Toplevel.__init__(self)
		self.geometry("800x700")

		rowunitframe = tk.Frame(self ,width=50, height =10,background = 'red')
		rowunitframe.grid(row=0,column=0,sticky="e"+"n"+"s"+"w")

		# postfile=open("stockpost.txt","r")

		postfile=open("stockpost.txt","r+")
	
		test= postfile.readlines()
		id=0
		tempwrite=[]	
		numberid='0'
		for line in test:
		# print ("each line of line views.py line 38")
			
			mydic=json.loads(line)
			print(id)
			# tempwrite.append(mydic)
			if (len(mydic)!= 0):
				print(mydic)
				for myidx,(colid,colval) in enumerate(mydic.items()):
					print(myidx,colid,colval)
					if id==0:
				
						lblval=tk.Label(rowunitframe,text=colid)
						lblval.grid(row=0,column=myidx)

						txtout=str(colval)
						textvar=tk.StringVar(value=txtout)
						txtcol=tk.Entry(rowunitframe,state='disable',textvariable=textvar,width=len(txtout))
						txtcol.grid(row=id+1,column=myidx,sticky="e"+"n"+"s"+"w")      

						# enterbrokeid.grid_propagate(0)      
					else:

						# pass

						# textvar=tk.StringVar(value=colid)
						# enterbrokeid=tk.Entry(self,text=colid,state='disable',textvariable=textvar,width=len(colval))
						# enterbrokeid.grid_propagate(0)      

						txtout=str(colval)
						textvar=tk.StringVar(value=txtout)
						txtcol=tk.Entry(rowunitframe,state='disable',textvariable=textvar,width=len(txtout))
						txtcol.grid(row=id+2,column=myidx,sticky="e"+"n"+"s"+"w")      



				# enterbrokeid.grid(row=0,column=myidx,sticky='e'+'w')
					# enterbrokeid.grid(row=0,column=myidx)

			id=id+1
		# postfile.truncate(0) // empty file
		postfile.close()

		# unitframectl=tk.Frame(self,width=50, height =10,background = 'blue')
		# unitframectl.grid(row=2,column=1,sticky="e"+"n"+"s"+"w")      

		btnset=tk.Button(self,text="Set",command=self.btntestunit, width = 10,height=2)
		btnset.grid(row=id+3,column=0,sticky="w")
		
	def btntestunit(self):
		pass