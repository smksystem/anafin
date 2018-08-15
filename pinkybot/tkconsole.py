
import tkinter as tk
import datetime
import sys
from pinkybot.monitor import pinkybot
class outputlog(tk.Tk):
	def __init__(self,selrange):

			tk.Tk.__init__(self)
			self.selrange=selrange
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


			self.frameGroupOutput = tk.Frame(self, width=500, height =200,background = 'red')
			self.frameGroupOutput.grid_propagate(0)
			self.frameGroupOutput.grid(row=2,column=0) # start row 2 since text output occupied 2 rows with 0,1.


			varasso={}
			varline={}
			# print (self.selrange)
			for stockname,data in enumerate(self.selrange):
				varasso["stockname"]=tk.StringVar(value=data)
				# print(data)
				
				# print(self.selrange[data])
				valueparams=self.selrange[data]
				for value,infodata in enumerate(valueparams):
					# print (infodata)
					varline[value]=infodata
					# tk.StringVar(value=infodata)
				# 		test[value]=tk.StringVar()

						# print (valueparams[infodata]["update"])
				# print (data)
				# print(y)
			varasso["stockname"]{}=varline
			print (varasso)
			exit()

			myvar=[]			
			for i in range(0,5):
				myvar.append(tk.StringVar())
				self.labelnamepassword=tk.Label(self.frameGroupOutput,name="name", text="Initial" + str(i) , textvariable=myvar[i])

				self.labelnamepassword.grid(row=0,column=i)


			# dir(self.labelnamepassword)
			myvar[0].set("hello1")
			myvar[1].set("hello2")
			# ["text"]="testhello4"
			# self.labelnamepassword["name"].configure("text")="test"
			self.update_idletasks()
			self.mycount = 0

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