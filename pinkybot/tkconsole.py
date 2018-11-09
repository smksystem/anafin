
import tkinter as tk
import datetime
import sys

from pinkybot.monitor import pinkybot

class outputlog(tk.Tk):
	def __init__(self):

		tk.Tk.__init__(self)
		self.mybot=pinkybot()
		self.title("Output Log")
		# self.resizable(0,0)
		self.geometry('780x620+20+20')

		# self.grid_columnconfigure(1, weight=1)
		# self.pack_propagate(0)
		usertxt=tk.StringVar(value="0147500")
		passtxt=tk.StringVar()
		broketxt=tk.StringVar(value="013")


		self.loginSet=[
						broketxt,
						usertxt,
						passtxt,
						
						]
		
		initinvest=tk.StringVar(value="10000")
		volumestep=tk.StringVar(value="100")
		profitstep=tk.StringVar(value="2")
		topvaluerange=tk.StringVar(value="4.98")
		startvaluebuy=tk.StringVar(value="4.90")
		startvolumebuy=tk.StringVar(value="0")   # from calculate range.
		stopvaluerange=tk.StringVar(value="0.00")
		commonstep=tk.StringVar(value="0.00")  # step from range calculation
		totalcostbuy=tk.StringVar(value="0000000000")
		totalvolumebuy=tk.StringVar(value="000")
		stockname=tk.StringVar(value="dummy")
		stockpin=tk.StringVar(value="3333")

		self.configval={
			"invest":initinvest,
			"volumestep":volumestep,
			"profitstep":profitstep,
			"topvaluerange":topvaluerange,		
			"commonstep":commonstep,
			"startvaluebuy":startvaluebuy,
			"startvolumebuy":startvolumebuy,
			"stopvaluerange":stopvaluerange,
			"totalcostbuy":totalcostbuy,
			"totalvolumebuy":totalvolumebuy,
			"stockname":stockname,
			"stockpin":stockpin,

		}

		self.myvarasso={}

		frameOutput = tk.Frame(self, width=500, height =200,background = 'blue')
		# self.frameOutput.grid_propagate(0)
		frameOutput.grid(row=0,column=0,rowspan = 2, columnspan = 1,sticky = "n"+"s" )

		self.output = tk.Text(frameOutput,wrap='word', width=60, height=14, background = 'black', fg='white')
		# self.output.grid_propagate(0)
		self.output.grid(row=0,column=0)
		# self.output.pack(side=tk.LEFT)

		scrollbar = tk.Scrollbar(frameOutput,orient="vertical", command = self.output.yview)
		# scrollbar.grid_propagate(0)
		scrollbar.grid(row=0,column=1,sticky="n"+"s")
		# scrollbar.pack(side=tk.RIGHT, fill="y")
		self.output['yscrollcommand'] = scrollbar.set

		
		self.frameLoginRT = tk.Frame(self ,background = 'green')
		# self.self.frameLoginRT.grid_propagate(0)
		self.frameLoginRT.grid(row=0,column=1,sticky="e"+"n"+"s"+"w")
	
		labelnamebrokeid=tk.Label(self.frameLoginRT, text="Broke ID")
		labelnamebrokeid.grid(row=0,column=0)
		self.enterbrokeid=tk.Entry(self.frameLoginRT,textvariable=broketxt)
		self.enterbrokeid.grid(row=0,column=1)      

		labelnamelogin=tk.Label(self.frameLoginRT, text="Login ID")
		labelnamelogin.grid(row=1,column=0)
		self.enterloginid=tk.Entry(self.frameLoginRT,textvariable=usertxt)
		self.enterloginid.grid(row=1,column=1)

		labelnamepassword=tk.Label(self.frameLoginRT, text="Password")
		labelnamepassword.grid(row=2,column=0)
		self.enterpassword=tk.Entry(self.frameLoginRT,show="*",textvariable=passtxt)
		self.enterpassword.grid(row=2,column=1)

		labelpinpassword=tk.Label(self.frameLoginRT, text="PIN")
		labelpinpassword.grid(row=3,column=0)
		enterpin=tk.Entry(self.frameLoginRT,show="*",textvariable=stockpin)
		enterpin.grid(row=3,column=1)

		self.btnLoginRT=tk.Button(self.frameLoginRT,text="Start Login RT",command=self.executeLogin)
		self.btnLoginRT.grid(row=3,column=2 )





		frameSetValue=tk.Frame(self,background = 'blue')
		frameSetValue.grid(row=2,column=1,sticky="e"+"n"+"s"+"w")      

		labelinitialvalue=tk.Label(frameSetValue, text="Invest")
		labelinitialvalue.grid(row=1,column=0)

		self.enterInvest=tk.Entry(frameSetValue,textvariable=initinvest) #,textvariable=usertxt)
		self.enterInvest.grid(row=1,column=1)


		labelinitialvalue=tk.Label(frameSetValue, text="Volume")
		labelinitialvalue.grid(row=2,column=0)

		self.enterVolumn=tk.Entry(frameSetValue,textvariable=volumestep) #,textvariable=usertxt)
		self.enterVolumn.grid(row=2,column=1)

		labelinitialvalue=tk.Label(frameSetValue, text="Profit Step")
		labelinitialvalue.grid(row=3,column=0)

		enterVolumn=tk.Entry(frameSetValue,textvariable=profitstep) 
		enterVolumn.grid(row=3,column=1)


		labelinitialvalue=tk.Label(frameSetValue, text="topvaluerange")
		labelinitialvalue.grid(row=4,column=0)

		enterVolumn=tk.Entry(frameSetValue,textvariable=topvaluerange) 
		enterVolumn.grid(row=4,column=1)

		labelvaluebuy=tk.Label(frameSetValue, text="StartValueBuy")
		labelvaluebuy.grid(row=5,column=0)

		self.entervaluebuy=tk.Entry(frameSetValue,textvariable=startvaluebuy) 
		self.entervaluebuy.grid(row=5,column=1)

		self.btnStartInitCal=tk.Button(frameSetValue,text="Set Parameters",command=self.setparameter)
		self.btnStartInitCal.grid(row=7,column=1 )



		self.btnStartvaluebuy=tk.Button(frameSetValue,text="Set Value Buy",command=self.setvaluebuy,state='disabled',)
		self.btnStartvaluebuy.grid(row=8,column=1 )

		labelvaluebuy=tk.Label(frameSetValue, text="Cost:")
		labelvaluebuy.grid(row=7,column=0,sticky="w")

		labelvaluebuy=tk.Label(frameSetValue, textvariable=totalcostbuy)
		labelvaluebuy.grid(row=7,column=0,sticky="e")


		labelvalumebuy=tk.Label(frameSetValue, text="Volume:")
		labelvalumebuy.grid(row=8,column=0,sticky="w")

		labelvalumebuy=tk.Label(frameSetValue, textvariable=totalvolumebuy)
		labelvalumebuy.grid(row=8,column=0,sticky="e")

		self.framePutValue=tk.Frame(self,background = 'yellow')
		self.framePutValue.grid(row=3,column=1,sticky="e"+"n"+"s"+"w")      

		btnBuyCommand=tk.Button(self.framePutValue,text="Buy Now",command=self.buybyvalue, width = 10,height=2)
		btnBuyCommand.grid(row=0,column=0,sticky="w")

		btnSellCommand=tk.Button(self.framePutValue,text="Sell Now",command=self.sellbyvalue, width = 10,height=2)
		btnSellCommand.grid(row=0,column=0,sticky="e")

		btnRefreshCmd=tk.Button(self.framePutValue,text="Refresh",command=self.rtrefresh, width = 25,height=3)
		btnRefreshCmd.grid(row=1,column=0)





		self.canvas=tk.Canvas(self,background="black")
		self.canvas.grid(row=2,column=0,rowspan=2,sticky="nsew")


		self.frameGroupOutput = tk.Frame(self.canvas,background = 'gray')
		self.frameGroupOutput.grid(row=0,column=0) # start row 2 since text output occupied 2 rows with 0,1.

		vsbar = tk.Scrollbar(self,orient="vertical", command = self.canvas.yview)
		vsbar.grid(row=2,column=0,rowspan=2,sticky="e"+"n"+"s")
		self.canvas.configure(yscrollcommand=vsbar.set)

		hsbar = tk.Scrollbar(self,orient="horizontal", command = self.canvas.xview)
		hsbar.grid(row=4,column=0,rowspan=1,sticky="e"+"s"+"w")
		self.canvas.configure(yscrollcommand=hsbar.set)
		# scrollbar.pack(side=tk.RIGHT, fill="y")






		rangeData={
		"A":[0,1.99,0.01],  # 0 to 2 step 0.01
		"B":[2,4.98,0.02], # 2 up to less than 5  0.02
		"C":[5,9.95,0.05],
		"D":[10,24.9,0.10],
		"E":[25,99.75,0.25],
		"F":[100,199.5,0.5],
		"G":[200,399,1],
		"H":[400,1000,2],
		}
		optionList=[]
		for planName,myrange in enumerate(rangeData):
			startfrom=str(rangeData[myrange][0])
			stopfrom=str(rangeData[myrange][1])
			stepfrom=str(rangeData[myrange][2])
			# print (self.rangeData[myrange][0])
			optionList.append("Plan" + myrange +" "+ startfrom+"-"+stopfrom + " step " +stepfrom)

		self.rangeplanVar=tk.StringVar()
		self.rangeplanVar.set("Select range plan") # default choice
		self.rangeplanMenu1 = tk.OptionMenu(frameSetValue, self.rangeplanVar, *optionList,command=self.doMenuRange)
		self.rangeplanMenu1.grid(row=0,column=0,sticky="w")

		self.btnSave=tk.Button(frameSetValue,text="Save",command=self.executeSave)
		self.btnSave.grid(row=0,column=1,sticky="w")
		self.btnSave.update()

		self.btnLoad=tk.Button(frameSetValue,text="Load",command=self.executeLoad)
		self.btnLoad.grid(row=0,column=1,sticky="w",padx=self.btnSave.winfo_width())

		self.alreadyputback=False # To make put back into queue one time and sync to DB.
		self.update_idletasks()
		# self.mycount = 0
		
		# self.myvarasso["5.00"]["order"].set("buy")
		self.txtout("!!! Welcome , Please login !!!")

	def executeSave(self):
		print("saveAllvalue")

	def executeLoad(self):
		print("LoadAllValue")

	def setvaluebuy(self):

		print("start value buy=" + self.configval["startvaluebuy"].get())
		valuebuy=self.configval["startvaluebuy"].get()

	


		# print (self.configval["stopvaluerange"].get())
		stopvaluerange=float(self.configval["stopvaluerange"].get())
		# print (self.configval["commonstep"].get())
		commonstep=float(self.configval["commonstep"].get())
		
		runvalue=round(float(valuebuy),2)
		priceaccume=0
		volumeaccume=0
		
		print ("runvalue")
		print(runvalue)
		print ("stopvaluerange")
		print (stopvaluerange)

		while (runvalue<=stopvaluerange):
			print ("enter while loop")
			runvalue=round(runvalue,2)
			print ("round run value=" +str(runvalue))
			print ("stopvaluerange=" +str(stopvaluerange))
			chkpad=str(runvalue).split(".")

			if len(chkpad[1])==1:
				tempval=chkpad[1]+"0"
				stepval=chkpad[0]+"." +tempval
				runvalue=stepval
				# print(self.myvarasso[runvalue])
				# priceaccumestep= float(self.myvarasso[runvalue][runvalue].get())
				priceaccumestep= runvalue
				print("tkconsole.py line 280 runvalue=" + runvalue)
				volumeaccumestep= float(self.myvarasso[runvalue][0]["volumn"].get())
				# exit()

				print (runvalue+" need price = " + str(priceaccumestep))
				


				lblvalue=str(runvalue)
				# for repeatidx in self.labeldisplay[valuebuy]:
				# if repeatidx!=valuebuy:	
				
				self.labeldisplay[lblvalue][lblvalue].configure(fg='black',background='green')
				self.labeldisplay[lblvalue]["updatedate"].configure(fg='black',background='green')
				self.labeldisplay[lblvalue]["updatetime"].configure(fg='black',background='green')
				self.labeldisplay[lblvalue]["volumn"].configure(fg='black',background='green')
				self.labeldisplay[lblvalue]["price"].configure(fg='black',background='green')
				self.labeldisplay[lblvalue]["order"].configure(fg='black',background='green')
				self.labeldisplay[lblvalue]["state"].configure(fg='black',background='green')
				self.labeldisplay[lblvalue]["targetvalue"].configure(fg='black',background='green')
				self.labeldisplay[lblvalue]["profit"].configure(fg='black',background='green')	

				runvalue=float(stval)


				priceaccume+=priceaccumestep
				volumeaccume+=volumeaccumestep
				
			else:
				# print(self.myvarasso[str(runvalue)])
				
				
				

				lblvalue=str(runvalue)
				self.labeldisplay[lblvalue][lblvalue].configure(fg='black',background='green')
				self.labeldisplay[lblvalue]["updatedate"].configure(fg='black',background='green')
				self.labeldisplay[lblvalue]["updatetime"].configure(fg='black',background='green')
				self.labeldisplay[lblvalue]["volumn"].configure(fg='black',background='green')
				self.labeldisplay[lblvalue]["price"].configure(fg='black',background='green')
				self.labeldisplay[lblvalue]["order"].configure(fg='black',background='green')
				self.labeldisplay[lblvalue]["state"].configure(fg='black',background='green')
				self.labeldisplay[lblvalue]["targetvalue"].configure(fg='black',background='green')
				self.labeldisplay[lblvalue]["profit"].configure(fg='black',background='green')	

				priceaccumestep=float(self.myvarasso[lblvalue]["price"].get())
				volumeaccumestep= float(self.myvarasso[lblvalue]["volumn"].get())

				print (str(runvalue) +" need price = " + str(priceaccumestep))
				priceaccume+=priceaccumestep
				volumeaccume+=volumeaccumestep

			runvalue+=commonstep
			runvalue=round(runvalue,2)


		self.labeldisplay[valuebuy][valuebuy].configure(fg='white',background='orange')
		for repeatidx in self.labeldisplay[valuebuy]:
			if repeatidx!=valuebuy:	

				self.labeldisplay[valuebuy][repeatidx]["orderid"].configure(fg='white',background='orange')
				self.labeldisplay[valuebuy][repeatidx]["startordertime"].configure(fg='white',background='orange')
				self.labeldisplay[valuebuy][repeatidx]["matchordertime"].configure(fg='white',background='orange')
				self.labeldisplay[valuebuy][repeatidx]["matchcomplete"].configure(fg='white',background='orange')
				self.labeldisplay[valuebuy][repeatidx]["volumn"].configure(fg='white',background='orange')
				self.labeldisplay[valuebuy][repeatidx]["orderside"].configure(fg='white',background='orange')
				self.labeldisplay[valuebuy][repeatidx]["state"].configure(fg='white',background='orange')
				self.labeldisplay[valuebuy][repeatidx]["targetvalue"].configure(fg='white',background='orange')
				self.labeldisplay[valuebuy][repeatidx]["profit"].configure(fg='white',background='orange')


		print ("Total price to buy =" +str(priceaccume))
		self.configval["totalcostbuy"].set(priceaccume)
		self.configval["totalvolumebuy"].set(volumeaccume)
		self.txtout("Set Value to buy =" + valuebuy)
		self.txtout("Set Value End to buy = " + str(stopvaluerange))
		self.txtout("Set total price to pay = " + str(priceaccume))
		self.txtout("Set total volume to pay = " + str(volumeaccume))

	def buybyvalue(self):
		print("Buy set value")
		self.mybot.myorder("buybyvalue",self.configval)

		print ("Buy finished ")

	def sellbyvalue(self):
		print ("sell set value")	

		# self.mybot.threadorderbuy("test")
	def rtrefresh(self):
		print ("refresh button press")
		self.mybot.botrtrefresh()
		# self.mybot.myorder("rtrefresh",self.configval)


	def setparameter(self):
		print("def startcalculate here tkconsole.py line 359")

		print(self.configval["invest"].get())
		i=0
		# for label in self.configval:
		# 	configlabel=tk.Label(self.framePutValue,text=label)
		# 	configlabel.grid(row=i,column=1)   
		# 	i+=1


		invest=int(self.configval["invest"].get())
		volumestep=int(self.configval["volumestep"].get())
		profitstep=int(self.configval["profitstep"].get())
		topvaluerange=float(self.configval["topvaluerange"].get())
		startvaluebuy=float(self.configval["startvaluebuy"].get())
		commonvaluestep=float(self.configval["commonstep"].get())


		self.parameterconfig={
			"invest":invest,
			"volumestep":volumestep,
			"profitstep":profitstep,
			"topvaluerange":topvaluerange,
			"startvaluebuy":startvaluebuy,
			"commonvaluestep":commonvaluestep,
		}
		# valuebuy=startvaluebuy
		runvalue=float(startvaluebuy) # change text to numbering.
		stopvaluerange=float(topvaluerange)
		commonvaluestep=float(commonvaluestep)
		# volumestep=float(volumestep)
		# print (runvalue)
		# print (commonvaluestep)
		# print (type(runvalue))
		# print(type(stopvaluerange))
		# exit()
		while (runvalue<=stopvaluerange):				
			# print ("enter while loop")
			# runvalue=round(runvalue,2)
			# print ("round run value=" +str(runvalue))

			# if (stopvaluerange<=runvalue):
				

			print("run value range = " + str(runvalue))
			stepcost=round((runvalue*volumestep),2)
			runinvest -=(runvaluerange*volumestep)
			runvalue+=commonvaluestep
			runvalue=round(runvalue,2)
			
			print ("step cost = " + stepcost)

			# print ("remain invest = " +  str(invest))
			
				# if runinvest > (runvaluerange*volumestep):

				# 	chkpad=str(runvaluerange).split(".")

				# 	if len(chkpad[1])==1:
				# 		tempval=chkpad[1]+"0"
				# 		stval=chkpad[0]+"." +tempval
				# 		valuelabel=stval
				# 	else:
				# 		valuelabel=str(runvaluerange)




			# print ("topvaluerange=" +str(topvaluerange))

			# chkpad=str(runvalue).split(".")

			# if len(chkpad[1])==1:
			# 	tempval=chkpad[1]+"0"
			# 	stepval=chkpad[0]+"." +tempval
			# 	runvalue=stepval
				# print(self.myvarasso[runvalue])
				# priceaccumestep= float(self.myvarasso[runvalue][runvalue].get())
				# priceaccumestep= runvalue


		print("end test")
		exit()


		# runvaluerange=topvaluerange


		# for i,valuelabel in enumerate(self.labeldisplay):
		# 	# print ( valuelabel)

		# 	runvaluerange=float(valuelabel)
		# 	if (topvaluerange >= runvaluerange):
		# 		print(str(runvaluerange))


		# exit()


		runinvest=invest
		for i,valuelabel in enumerate(self.myvarasso):
			runvaluerange=float(valuelabel)
			print ("runvaluerange = " +str(runvaluerange))


							# varinfo={
		# 		"orderid":varorderid,
		# 		"startordertime":varstartordertime,
		# 		"matchordertime":varmatchordertime,
		# 		"matchcomplete":varmatchcomplete,
		# 		"orderside":varorderside,
		# 		"volumn":varvolumn,
		# 		"state":varstatus,
		# 		"targetvalue":vartargetvalue,
		# 		"profit":varprofit,
		# 		}
			self.labeldisplay[valuelabel][valuelabel].configure(background="lightpink")
				# print(self.labeldisplay[valuelabel][0])
			for repeatidx in self.labeldisplay[valuelabel]:
				if repeatidx!=valuelabel:

					self.labeldisplay[valuelabel][repeatidx]["orderid"].configure(background="lightpink")
					self.labeldisplay[valuelabel][repeatidx]["startordertime"].configure(background="lightpink")
					self.labeldisplay[valuelabel][repeatidx]["matchordertime"].configure(background="lightpink")
					self.labeldisplay[valuelabel][repeatidx]["matchcomplete"].configure(background="lightpink")
					self.labeldisplay[valuelabel][repeatidx]["volumn"].configure(background="lightpink")
					self.labeldisplay[valuelabel][repeatidx]["orderside"].configure(background="lightpink")
					self.labeldisplay[valuelabel][repeatidx]["state"].configure(background="lightpink")
					self.labeldisplay[valuelabel][repeatidx]["targetvalue"].configure(background="lightpink")
					self.labeldisplay[valuelabel][repeatidx]["profit"].configure(background="lightpink")

					self.myvarasso[valuelabel][repeatidx]["volumn"].set(volumestep)
					# print (self.myvarasso[valuelabel])
					# exit()
					# self.myvarasso[valuelabel]["price"].set(stcost)

					target=round((float(commonvaluestep) * profitstep) + float(valuelabel),2)
					# print ("target value="+str(target))
					# exit()
					self.myvarasso[valuelabel][repeatidx]["targetvalue"].set(target)
					runinvest -=(runvaluerange*volumestep)
					stopvaluerange=runvaluerange
				# invest=remaininvest
			else:

				
				print("remain invest that could not put more = " +str(runinvest))
				break



				# runvaluerange+=commonvaluestep
		print ("remain invest = "+ str(runinvest))
		# print ("stopvaluerange at = " + str(stopvaluerange))
		self.configval["stopvaluerange"].set(stopvaluerange)
		# exit()

		self.canvas.yview_moveto(0.01)
		self.canvas.xview_moveto(0.01)
		# self.canvas.yview_moveto(0.5)


		self.txtout("Set Invest = " +str(invest),"yellow","gray")
		self.txtout("Set Step Volumn = " +str(volumestep))
		self.txtout("Set Step Common Value = " +str(commonvaluestep))
		self.txtout("Remain Range Invest =" +str(runinvest),"orange","green")
		
		self.txtout("Set Step Profit = " +str(profitstep))
		self.txtout("Set Start Value Range = " +str(topvaluerange))
		self.txtout("Set Stop Value Range = " +str(stopvaluerange),"green","white")


	def doMenuRange(self,value):


		plansel=value.split(' ')[0]
		self.myvarasso=self.initRangeValue(plansel[-1])

		# print(self.myvarasso["4.00"])
		# exit()

		if plansel=="PlanA":
			print("planA selected")
		elif plansel=="PlanB":
			print("planB selected")
		elif plansel=="PlanC":
			print("planC selected")

		
		children = self.winfo_children()
		for child in children:
			# print (str(type(child)))
			if (str(type(child)) == "<class 'tkinter.Canvas'>") :
				child.destroy()

				self.canvas=tk.Canvas(self,background="black")
				self.canvas.grid(row=2,column=0,rowspan=2,sticky="nsew")

				self.frameGroupOutput = tk.Frame(self.canvas,background = 'gray')
				self.frameGroupOutput.grid(row=0,column=0) # start row 2 since text output occupied 2 rows with 0,1.
				self.scrollbarYGroupOutPut = tk.Scrollbar(self,orient="vertical", command = self.canvas.yview)
				self.scrollbarYGroupOutPut.grid(row=2,column=0,rowspan=2,sticky="e"+"n"+"s")

				self.scrollbarXGroupOutPut = tk.Scrollbar(self,orient="horizontal", command = self.canvas.xview)
				self.scrollbarXGroupOutPut.grid(row=4,column=0,rowspan=1,sticky="e"+"s"+"w")

				# self.scrollbarXGroupOutPut = tk.Scrollbar(self,orient="horizontal", command = self.canvas.xview)
				# self.scrollbarXGroupOutPut.grid(row=4,column=0,rowspan=1,sticky="e"+"s"+"w")



				break		

		self.labeldisplay={}
		self.labeldisplay.clear()

		# list all value to print with decrease number
		runrangeNo=len(list (self.myvarasso.items()))-1 
		# print(len(list (self.myvarasso.items())))
		for i,myvarvalue in enumerate(self.myvarasso):
			# print (myvarvalue)
			varvalue=list (self.myvarasso.items())[runrangeNo][0]
			# print (varvalue)
			# print (runrangeNo)
			# print ("number of i=" + str(i))
			
			# print(runrangeNo)


			self.labeldisplay[varvalue]={}
			# print("number of variable = " + str(len (self.labeldisplay)))

			self.labeldisplay[varvalue][varvalue]=tk.Label(self.frameGroupOutput, text=varvalue,borderwidth=3, relief="groove",height=3)
			self.labeldisplay[varvalue][varvalue].grid_propagate(0)
			self.labeldisplay[varvalue][varvalue].grid(row=i,column=0,sticky="w")

			# labelseparate=tk.Label(self.frameGroupOutput, text=" | ")
			# labelseparate.grid(row=i,column=1)
			
			rowvalue=self.myvarasso[varvalue]
			# print ("tkconsole.py line 542")
			# print (rowvalue)
			# exit()
			# print("doMenuRange tkconsole.py line 525")
			# print(rowvalue)
			# if varvalue=="4.00":
			# 	print(rowvalue)
			for repeatidx,valrepeat in enumerate(rowvalue):

				self.labeldisplay[varvalue][repeatidx]={}
				# if varvalue=="4.00":
					# print(repeatidx,valrepeat)
				# print("tkconsole.py line 553")
				# print(valrepeat)
				for j,varinfo in enumerate(valrepeat):
					# print (varinfo)

					# varinfo={
					# 		"orderid":varorderid,
					# 		"startordertime":varstartordertime,
					# 		"matchordertime":varmatchordertime,
					# 		"matchcomplete":varmatchcomplete,
					# 		"orderside":varorderside,
					# 		"volumn":varvolumn,
					# 		"state":varstatus,
					# 		"targetvalue":vartargetvalue,
					# 		"profit":varprofit,
					# 		}

					# print(varvalue,repeatidx)

					if  varinfo=="orderid" or varinfo=="startordertime" or varinfo=="matchordertime"  or varinfo =="targetvalue":
						# print(varinfo,j)
						self.labeldisplay[varvalue][repeatidx][varinfo]=tk.Label(self.frameGroupOutput , textvariable=self.myvarasso[varvalue][repeatidx][varinfo],borderwidth=2, relief="groove",height=1)
						self.labeldisplay[varvalue][repeatidx][varinfo].grid(row=i,column=j+1+(int(repeatidx)*6),sticky="n"+"e"+"w",pady=5)

					if  varinfo=="matchcomplete" or varinfo=="orderside" or varinfo=="volumn" or varinfo == "profit" or varinfo=="state" :
						# print(varinfo,j)
						self.labeldisplay[varvalue][repeatidx][varinfo]=tk.Label(self.frameGroupOutput , textvariable=self.myvarasso[varvalue][repeatidx][varinfo],borderwidth=2, relief="groove",height=1)
						self.labeldisplay[varvalue][repeatidx][varinfo].grid(row=i,column=j-3+(int(repeatidx)*6),sticky="s"+"e"+"w",pady=5)

					# if  varinfo=="state" :
					# 	# print(varinfo,j)
					# 	self.labeldisplay[varvalue][repeatidx][varinfo]=tk.Label(self.frameGroupOutput , textvariable=self.myvarasso[varvalue][repeatidx][varinfo],borderwidth=2, relief="groove",height=3)
					# 	self.labeldisplay[varvalue][repeatidx][varinfo].grid(row=i,column=j+5+int(repeatidx),sticky="s"+"e"+"w",pady=7)
					# 	self.labeldisplay[varvalue][repeatidx][varinfo].grid_propagate(False)
					# if varinfo=="targetvalue":

					# 	self.labeldisplay[varvalue][repeatidx][varinfo]=tk.Label(self.frameGroupOutput , textvariable=self.myvarasso[varvalue][repeatidx][varinfo])
					# 	# self.labeldisplay.grid_propagate(0)
					# 	self.labeldisplay[varvalue][repeatidx][varinfo].grid(row=i,column=j+5)
			runrangeNo-=1


		# print (self.myvarasso)
		# print ("22"+rowvalue)	
		
		# exit()


		self.canvas['yscrollcommand'] = self.scrollbarYGroupOutPut.set
		self.canvas.bind('<Configure>', self.on_configure)

		self.canvas['xscrollcommand'] = self.scrollbarXGroupOutPut.set
		self.canvas.bind('<Configure>', self.on_configure)

		self.canvas.create_window((0,0), window=self.frameGroupOutput, anchor='center')
		# self.canvas.create_window((0,0), window=self.frameXGroupOutput, anchor='we')

		self.canvas.update()
		# update database at the first time select range
		# print (self.myvarasso)
		# self.mybot.dbqueue.put({"varasso":self.myvarasso})
		self.txtout("Set Plan = " +value)		
		return

	def on_configure(self,event):
		# update scrollregion after starting 'mainloop'
		# when all widgets are in canvas
		self.canvas.configure(scrollregion=self.canvas.bbox('all'))


	def initRangeValue(self,idx):
		rangeData={
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
		i=rangeData[idx][0]
		while i < rangeData[idx][1]:
			chkpad=str(round(i,2)).split(".")
			# print(len(chkpad))
			if len(chkpad)==1:
				stval=str(round(i,2))+".00"
			elif len(chkpad)==2:
				tempval=chkpad[1]+"0"
				stval=chkpad[0]+"." +tempval[:2]

			series.append(stval)
			i+=rangeData[idx][2]
		
		# print ("Range step="+str(rangeData[idx][2]))
		
		# print(series)
		self.configval["commonstep"].set(str(rangeData[idx][2]))

		return self.rangeline(series)

	def rangeline(self,series):
		# print(len(series))
		# exit()
		datenow = datetime.datetime.now().strftime("%Y-%m-%d")
		timenow = datetime.datetime.now().strftime("%H:%M:%S")

		varasso={}
		varstep={}
		varinfo={}
		# varinfogroup=[]
		varrepeat=[]

# /*********** TEST ****************
		# series=['2.00','2.02','2.04','2.06']
		# for varvalue in series:
		# 	varorderid=tk.StringVar(value="orderid")
		# 	varinfo={
		# 		"orderid":varorderid,
		# 	}
		# 	varrepeat.append(varinfo)
		# 	varasso[varvalue]=varrepeat
		# 	varrepeat=[]
		# 	# print (varvalue)
		# 	# print(varrepeat)
		# 	# print(varvalue)
		# 	if varvalue=="2.02":
		# 		break
		# print (varasso)

		# exit()	
################################################

		for varvalue in series:
			# print(varvalue)
			varorderid=tk.StringVar(value="orderid")
			varstartordertime=tk.StringVar(value=timenow)
			varmatchordertime=tk.StringVar(value="matchordertime")
			varmatchcomplete=tk.StringVar(value="matchcomplete")
			varorderside=tk.StringVar(value="orderside")
			varvolumn=tk.StringVar(value="volumn")
			varstatus=tk.StringVar(value="state")
			vartargetvalue=tk.StringVar(value="target")
			varprofit=tk.StringVar(value="profit")
			varinfo={
				"orderid":varorderid,
				"startordertime":varstartordertime,
				"matchordertime":varmatchordertime,
				"targetvalue":vartargetvalue,
				"matchcomplete":varmatchcomplete,
				"orderside":varorderside,
				"volumn":varvolumn,
				"profit":varprofit,
				"state":varstatus,
			}
			varrepeat.append(varinfo)

			# print (varrepeat[1])
			# exit()
			############################################################################
			# skip this for testing when multi result box
			# if varvalue=="4.00":
			# 	varrepeat.append(varinfo)
			# 	varrepeat.append(varinfo)
			# 	varrepeat.append(varinfo)
			# 	varrepeat.append(varinfo)
			# 	varrepeat.append(varinfo)
				
			############################################################################	
				# print (varvalue,varrepeat)
				# exit()
			varasso[varvalue]=varrepeat
			varrepeat=[]

			# print (varvalue)
			# print(varrepeat)
		# print (varasso)
		# exit()
		# print (varasso)
		# exit()
		return varasso

	def getRangeData(self):
		print("print rangedata")





		return self.rangeData
	def update():
		pass


	def flash(self,Label,count=0,colormode=""):

		if colormode=="green":
			# print ("select color"+colormode)
			Label.configure(foreground="white")
			Label.configure(background="lime")
			colormode=""

		bg = Label.cget('background')
		fg = Label.cget('foreground')
		Label.configure(background=fg,foreground=bg)
		count +=1
		# print ("Count="+str(count))
		if (count < 31):
			self.after(1000,self.flash,Label,count)
		elif (count>=31):
			# print ( "enter count > 31")
			Label.configure(foreground="black")
			Label.configure(background="silver")



	def txtout(self,txtmsg,colorhighlight="",backcolor=""):

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


			if colorhighlight != "" :
				self.highlight_text(txtmsg,colorhighlight,backcolor)
				colorhighlight=""
				backcolor=""



			self.output.configure(state='disabled')
			
			self.output.see("end")
			# self.output.tag_config("a", foreground="blue")
			# self.output.insert(contents, ("n", "a"))
	
	def executeLogin(self):

			# print("hello button Login " + self.loginSet[0].get())
			for child in self.frameLoginRT.winfo_children():
				child.configure(state='disable')
			# exit()
			self.mybot.threadlogin(self.loginSet)





			# return LoginParams
	def highlight_text(self,word,color="white",backcolor="black"):
			# word="Vol"
			txtmsg=self.output.get("1.0","end")
			# print (txtmsg)
			countVar = tk.StringVar()
			self.output.tag_config(word, background=backcolor, foreground=color)
			if txtmsg:
				pos = '1.0'
				while 1:
					pos = self.output.search( word,pos,stopindex="end", count=countVar)
					if not pos: break
					lastidx = '%s+%dc' % (pos, int(countVar.get()))
					self.output.tag_add(word, pos, lastidx)
					pos = lastidx

			# self.output.see(tk.END)
		 
	def Refresher(self):

			# self.mycount+=1
			# step=10+(self.mycount/10)
			# print (step)
			# print (dir(self))
			# if not self.mybot.qvalchange.empty():
			# print(self.mybot.mycollectqueues)
			# if not self.mybot.mycollectqueues["qdatarefresh"].empty():
			# 	temprefreshdata=self.mybot.mycollectqueues["qdatarefresh"].get()
			# 	print(temprefreshdata)
			# print ("!!!!!!!!!!!!!!!!!! Dump data refresh !!!!!!!!!!!!!")
			# alreadyputback=False

			if not self.mybot.mycollectqueues["qvalchange"].empty():
				tempdict=self.mybot.mycollectqueues["qvalchange"].get()
				print (tempdict)
				# print (tempdict["textout"])
				if "textout" in tempdict:
						self.txtout("value change to:" + tempdict["textout"])

				if "stockvalue" in tempdict:
						print ("stock has been updated !!!!!!!!!!!!")
						self.txtout("Value Change : " + tempdict["stockvalue"])
						lblstockvalue=tempdict["stockvalue"] # get value from queue
						if lblstockvalue in self.labeldisplay:
							self.flash(self.labeldisplay[lblstockvalue][lblstockvalue],9,"green")
				# self.mybot.myqueue.join()
				if "stockname" in tempdict:
						print ("monitor =" + tempdict["stockname"])
						self.configval["stockname"].set(tempdict["stockname"])

			if not self.mybot.mycollectqueues["qorder"].empty() :
				chkorder=self.mybot.mycollectqueues["qorder"].get()
				print ("chkorder tkconsole.py line 760")
				print (chkorder)
				if chkorder["order"]=="refreshtk":
					print ("<<<<<<<<<<refresh Tk Inter GUI need to refresh now")
					# self.alreadyputback=False
				else:
					print (">>>>>>>>Put refresh back DB")
					chkorder=self.mybot.mycollectqueues["qorder"].put(chkorder)
					# self.alreadyputback=True
				
			# self.output.tag_config("testb", background="white", foreground="red")
			# self.output.tag_add('testb', 10.0, step)
			self.after(50, self.Refresher) # every second...


# if __name__ == '__main__':
#     # print("start logoutput")
#     txtoutput=outputlog()
#     txtoutput.Refresher()
#     txtoutput.mainloop()

# exit()