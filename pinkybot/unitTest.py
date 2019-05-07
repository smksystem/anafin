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

		self.unitframe={}

		
		self.rowbtnframe = tk.Frame(self ,width=50, height =10,background = 'green')
		self.rowbtnframe.grid(row=0,column=0,sticky="e"+"n"+"s"+"w")


		self.rowunitframe = tk.Frame(self ,width=50, height =10,background = 'red')
		self.rowunitframe.grid(row=1,column=0,sticky="e"+"n"+"s"+"w")

		# postfile=open("stockpost.txt","r")

		btnrefresh=tk.Button(self.rowbtnframe,text="Refresh",command=self.refreshunit, width = 10,height=2)
		btnrefresh.grid(row=0,column=0,sticky="w")


		btnset=tk.Button(self.rowbtnframe,text="Set",command=self.btntestunit, width = 10,height=2)
		btnset.grid(row=0,column=2,sticky="w")



		self.refreshfile()

		

	def refreshfile(self):

		postfile=open("stockpost.txt","r")
	
		test= postfile.readlines()
		id=0
		tempwrite=[]	
		numberid='0'
		self.stringdata=[]

		for line in test:
		# print ("each line of line views.py line 38")
			
			mydic=json.loads(line)
			print(id)
			# tempwrite.append(mydic)

			optionList=["Pending (S)","Open(O)","Matched (M)"]



			if (len(mydic)!= 0):
				print(mydic)
				for myidx,(colid,colval) in enumerate(mydic.items()):
					print(myidx,colid,colval)
					# self.stringdata.append({})


					if id==0:
				
						lblval=tk.Label(self.rowunitframe,text=colid)
						lblval.grid(row=0,column=myidx)

						# optionList={0:"1",1:"2"}

						if (colid=="status"):


							choice_var = tk.StringVar()
							statusMenu = tk.OptionMenu(self.rowunitframe,choice_var,*optionList,command=self.setState)
							statusMenu.grid(row=id+1,column=myidx,sticky="w")
							choice_var.set(colval)

						else:

							txtout=str(colval)
							textvar=tk.StringVar(value=txtout)
							# txtcol=tk.Entry(rowunitframe,state='disable',textvariable=textvar,width=len(txtout))
							txtcol=tk.Entry(self.rowunitframe,textvariable=textvar,width=len(txtout))
							txtcol.grid(row=id+1,column=myidx,sticky="e"+"n"+"s"+"w")      

						# enterbrokeid.grid_propagate(0)      
					else:
						if (colid=="status"):


							# optionList=["1","2"]

							choice_var = tk.StringVar()
							statusMenu = tk.OptionMenu(self.rowunitframe, choice_var,*optionList,command=self.setState)
							statusMenu.grid(row=id+2,column=myidx,sticky="w")
							choice_var.set(colval)

						else:



							txtout=str(colval)
							textvar=tk.StringVar(value=txtout)
							# txtcol=tk.Entry(rowunitframe,state='disable',textvariable=textvar,width=len(txtout))
							txtcol=tk.Entry(self.rowunitframe,textvariable=textvar,width=len(txtout))
							txtcol.grid(row=id+2,column=myidx,sticky="e"+"n"+"s"+"w")      



				# enterbrokeid.grid(row=0,column=myidx,sticky='e'+'w')
					# enterbrokeid.grid(row=0,column=myidx)

			id=id+1
		# postfile.truncate(0) // empty file
		postfile.close()
	
		# return id
	# def savefile(self):

		
	def setState(self,setvalue="1"):

		print("Set value")

	def btntestunit(self):


		postfile=open("stockpost.txt","w+")

		# postfile.write(json.dumps(i)+"\n")
		postfile.write(json.dumps(i)+"\n")

		postfile.close()

	def refreshunit(self):

		for ele in self.rowunitframe.winfo_children():
			# print(ele)
			ele.destroy()

		# for ele in self.rowbtnframe.winfo_children():
		# 	ele.destroy()


		self.refreshfile()

