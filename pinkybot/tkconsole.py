
import tkinter as tk
import datetime
import sys
from pinkybot.monitor import pinkybot
class outputlog(tk.Tk):
	def __init__(self,selrange):

			tk.Tk.__init__(self)
			self.myvarasso=self.initRangeValue(selrange)


			self.mybot=pinkybot()

			self.title("Output Log")
			# self.resizable(0,0)
			self.geometry('800x500+20+20')
			# self.pack_propagate(0)
			usertxt=tk.StringVar(value="0147500")
			passtxt=tk.StringVar()
			broketxt=tk.StringVar(value="013")
			self.loginSet=[
							broketxt,
							usertxt,
							passtxt,
							
							]

			# print(loginSet[0].get())

			self.frameOutput = tk.Frame(self, width=500, height =200,background = 'blue')
			# self.frameOutput.grid_propagate(0)
			self.frameOutput.grid(row=0,column=0,rowspan = 2, columnspan = 1,sticky = "n"+"s" )



			self.output = tk.Text(self.frameOutput,wrap='word', width=60, height=14, background = 'black', fg='white')
			# self.output.grid_propagate(0)
			self.output.grid(row=0,column=0)
			# self.output.pack(side=tk.LEFT)

			self.scrollbar = tk.Scrollbar(self.frameOutput,orient="vertical", command = self.output.yview)
			# self.scrollbar.grid_propagate(0)
			self.scrollbar.grid(row=0,column=1,sticky="n"+"s")
			# self.scrollbar.pack(side=tk.RIGHT, fill="y")
			self.output['yscrollcommand'] = self.scrollbar.set

			
			self.frameLoginRT = tk.Frame(self)# ,background = 'green')
			# self.framebutton.grid_propagate(0)
			self.frameLoginRT.grid(row=0,column=1,rowspan = 1, columnspan = 1)
		
			self.labelnamebrokeid=tk.Label(self.frameLoginRT, text="Broke ID")
			self.labelnamebrokeid.grid(row=0,column=0)
			self.enterbrokeid=tk.Entry(self.frameLoginRT,textvariable=broketxt)
			self.enterbrokeid.grid(row=0,column=1)      

			self.labelnamelogin=tk.Label(self.frameLoginRT, text="Login ID")
			self.labelnamelogin.grid(row=1,column=0)
			self.enterloginid=tk.Entry(self.frameLoginRT,textvariable=usertxt)
			self.enterloginid.grid(row=1,column=1)

			self.labelnamepassword=tk.Label(self.frameLoginRT, text="Password")
			self.labelnamepassword.grid(row=2,column=0)
			self.enterpassword=tk.Entry(self.frameLoginRT,show="*",textvariable=passtxt)
			self.enterpassword.grid(row=2,column=1)

			self.LoginBtnInFrame=tk.Button(self.frameLoginRT,text="Start Login RT",command=self.executeLogin)
			self.LoginBtnInFrame.grid(row=3,column=1 )

			


			self.frameInitValue=tk.Frame(self, width=100, height =300,background = 'yellow')
			self.frameInitValue.grid(row=1,column=1,rowspan = 1, columnspan = 1)      
			self.labelinitialvalue=tk.Label(self.frameInitValue, text="Input Initial Value")
			self.labelinitialvalue.grid(row=0,column=0)

			self.enterloginid=tk.Entry(self.frameInitValue) #,textvariable=usertxt)
			self.enterloginid.grid(row=0,column=1)


			self.LoginBtnInFrame=tk.Button(self.frameInitValue,text="Start Login",command=self.executeLogin)
			self.LoginBtnInFrame.grid(row=1,column=1 )




			self.canvas=tk.Canvas(self,background="blue")
			# self.canvas.grid_propagate(0)
			self.canvas.grid(row=2,column=0)


			self.frameGroupOutput = tk.Frame(self.canvas,background = 'red')
			# self.frameGroupOutput.grid_propagate(0)
			self.frameGroupOutput.grid(row=2,column=0) # start row 2 since text output occupied 2 rows with 0,1.

			self.scrollbarGroupOutPut = tk.Scrollbar(self,orient="vertical", command = self.canvas.yview)
			# self.scrollbar.grid_propagate(0)
			self.scrollbarGroupOutPut.grid(row=2,column=1,sticky="w"+"n"+"s")
			# self.scrollbar.pack(side=tk.RIGHT, fill="y")
			self.canvas['yscrollcommand'] = self.scrollbarGroupOutPut.set
			self.canvas.bind('<Configure>', self.on_configure)
			self.canvas.create_window((0,0), window=self.frameGroupOutput, anchor='center')

			myvar=[]  
			labelvar={}
			labelinfo={}
			# {0: {'volumn': <tkinter.StringVar object at 0x04331FB0>, 'update': <tkinter.StringVar object at 0x04331F10>, 'order': <tkinter.StringVar object at 0x04331F30>, 'state': <tkinter.StringVar object at 0x04331F70>}} 

			self.labeldisplay={}
			for i,varvalue in enumerate(self.myvarasso):
				print ("i="+str(i))
				# print (self.myvarasso[varvalue]["volumn"])
				# myvar.append(tk.StringVar())
				
				
				labelvar[varvalue]=tk.Label(self.frameGroupOutput, text=varvalue)
				labelvar[varvalue].grid(row=i,column=0)

				labelseparate=tk.Label(self.frameGroupOutput, text=" | ")
				labelseparate.grid(row=i,column=1)
				
				# myinfo={}
				# self.labeldisplay[varvalue]["info"]=myinfo

				rowvalue=self.myvarasso[varvalue]
				for j,varinfo in enumerate(rowvalue):
					# print ("j="+str(j))
					# exit()
					# col+=j
					# self.labeldisplay=tk.Label(self.frameGroupOutput, text=varvalue)
					# self.labeldisplay.grid(row=i,column=j)

					# tempvar=self.myvarasso[varvalue][varinfo].get()
					# print("tempvar="+varinfo)
					labelinfo[varinfo]=tk.Label(self.frameGroupOutput , textvariable=self.myvarasso[varvalue][varinfo])
					# print (myinfo)
					# self.labeldisplay[varvalue][self.myvarasso[varvalue][varinfo].get()]=tk.Label(self.frameGroupOutput , textvariable=self.myvarasso[varvalue][varinfo] )

					# self.labeldisplay.grid_propagate(0)
					labelinfo[varinfo].grid(row=i,column=j+2)
			# print(myinfo)
				self.labeldisplay[varvalue]={"var":labelvar,"info":labelinfo}

			print (self.labeldisplay["5.00"])
			exit()
			self.labeldisplay["5.00"]["info"]["order"].configure(background="red")
			# exit()
			# self.labeldisplay["5.00"]["info"]["order"].configure(background="red")

					# self.labeldisplay[varvalue][self.myvarasso[varvalue][varinfo].get()].grid(row=i,column=j+2)

			# dir(self.labelnamepassword)
			# myvar[0].set("hello1")
			# myvar[1].set("hello2")
			# ["text"]="testhello4"
			# self.labelnamepassword["name"].configure("text")="test"
			self.update_idletasks()
			self.mycount = 0
			self.myvarasso["5.00"]["order"].set("buy")

			


	def on_configure(self,event):
		# update scrollregion after starting 'mainloop'
		# when all widgets are in canvas
		self.canvas.configure(scrollregion=self.canvas.bbox('all'))
	def initRangeValue(self,idx):
		data={
		"A":[0,2,0.01],  # 0 to 2 step 0.01
		"B":[2,4.98,0.02], # 2 up to less than 5  0.02
		"C":[5,10,0.05],
		"D":[10,25,0.10],
		"E":[25,100,0.25],
		"F":[100,200,0.5],
		"G":[200,400,1],
		"H":[400,1000,2],
		}
		series=[]
		i=data[idx][0]
		while i < data[idx][1]:
			chkpad=str(round(i,2)).split(".")
			# print(len(chkpad))
			if len(chkpad)==1:
				stval=str(round(i,2))+".00"
			elif len(chkpad)==2:
				tempval=chkpad[1]+"0"
				stval=chkpad[0]+"." +tempval[:2]

			series.append(stval)
			i+=data[idx][2]
		# print(series)
		return self.rangeline(series)

	def rangeline(self,series):

		# mystock={}
		# linedic={}
		# stockdata={}
		# rowid={}
		datenow = datetime.datetime.now().strftime("%Y-%m-%d")
		timenow = datetime.datetime.now().strftime("%H:%M:%S")

		# vardatetime=tk.StringVar(value="datetime")
		# print(series)
		# mystock["BEAUTY"]=linedic

		varasso={}
		varstep={}
		varinfo={}
		# print (series)
		for rowid,varvalue in enumerate(series):
			# print (rowid)
			# print (varvalue)
			# exit()

			vardate=tk.StringVar(value=datenow)
			vartime=tk.StringVar(value=timenow)
			varorder=tk.StringVar(value="wait")
			varstatus=tk.StringVar(value="wait")
			varvolumn=tk.StringVar(value="wait")
			# varvalue=tk.StringVar(value=data)

			varinfo={
				"updatedate":vardate,
				"updatetime":vartime,
				"volumn":varvolumn,
				"order":varorder,
				"state":varstatus
			}
			# varstep={"value":varvalue}
			varasso[varvalue]=varinfo


		# print (varasso)
	
	
		# mystock["BEAUTY"]=linedic
		# print (rowid)
		# exit()
		return varasso

	def getRangeSeries(self):
		return self.rangestock
	def update():
		pass







	def txtout(self,txtmsg):

			self.timenow = datetime.datetime.now()
			

			self.output.configure(state='normal')
			# print (txtmsg)

			
			# self.highlight_pattern("vol","red")

			self.output.insert(tk.END,self.timenow.strftime("%Y-%m-%d %H:%M:%S ") + str(txtmsg + "\n"))
			

			
			# pos = self.output.search( "Vol","1.0",stopindex="end", count=countVar)
			# print (pos)
			# self.highlight_text("Vol",txtmsg)
			# self.highlight_text("Order",txtmsg)
			# self.highlight_text("Stat",txtmsg)
			self.output.configure(state='disabled')
			
			# self.output.tag_config("a", foreground="blue")
			# self.output.insert(contents, ("n", "a"))
	
	def executeLogin(self):

			# print("hello button Login " + self.loginSet[0].get())
			# print("hello button Login " + self.loginSet[1].get())
			# print("hello button Login " + self.loginSet[2].get())
			
			self.mybot.threadlogin(self.loginSet)

			# print(self.TempVar)

			
			# return LoginParams



			




	def highlight_text(self,word):
			# word="Vol"
			txtmsg=self.output.get("1.0","end")
			# print (txtmsg)
			countVar = tk.StringVar()
			self.output.tag_config("test", background="black", foreground="green")
			if txtmsg:
				pos = '1.0'
				while 1:
					pos = self.output.search( word,pos,stopindex="end", count=countVar)
					if not pos: break
					lastidx = '%s+%dc' % (pos, int(countVar.get()))
					self.output.tag_add('test', pos, lastidx)
					pos = lastidx

			self.output.see(tk.END)
		 
	def Refresher(self):

			self.mycount+=1
			step=10+(self.mycount/10)
			print (step)
			# print (dir(self))
			if not self.mybot.myqueue.empty():

				print(self.mybot.myqueue.get())
				# self.mybot.myqueue.join()

				
			self.output.tag_config("testb", background="white", foreground="red")
			self.output.tag_add('testb', 10.0, step)
			self.after(1000, self.Refresher) # every second...


# if __name__ == '__main__':
#     # print("start logoutput")
#     txtoutput=outputlog()
#     txtoutput.Refresher()
#     txtoutput.mainloop()

# exit()