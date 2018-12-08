class fivesteps():
	def setparameter(self,conf_params):
		print("set parameter of fivestep plugin_fivestep.py line 3")
		
		initinvest=20000
		volumestep	=100

		conf_params["initinvest"].set(str(initinvest))
		conf_params["volumestep"].set(str(volumestep))

		conf_params["profitstep"].set("2")
		conf_params["topvaluerange"].set("4.96")
		conf_params["startvaluebuy"].set("4.88")
		conf_params["floorvaluerange"].set("4.78")

		conf_params["stopvaluerange"].set("4.84")	# stop loss not to buy more	
		# conf_params["volumestep"].set("100")
		# conf_params["volumestep"].set("100")

		# initinvest=int(self.configval["initinvest"].get()) delete this.
		# volumestep=int(self.configval["volumestep"].get())


		# profitstep=int(self.configval["profitstep"].get())
		# topvaluerange=float(self.configval["topvaluerange"].get())
		# floorvaluerange=float(self.configval["floorvaluerange"].get())

		# startvaluebuy=float(self.configval["startvaluebuy"].get())
		# commonvaluestep=float(self.configval["commonstep"].get())

		# runvalue=float(startvaluebuy) # change text to numbering.
		# stopvaluerange=float(topvaluerange)
		# commonvaluestep=float(commonvaluestep)

		runinvest=initinvest


		# runcostbuy=0 #### purpose variable to calculate in below.
		# runvolumebuy=0


		# while (runvalue<=stopvaluerange):				
				
		# 	if runinvest > (runvalue*volumestep): #### check not to give -294, -xxx

		# 		print("run value range = " + str(runvalue))
		# 		# stepcost=round((runvalue*volumestep),2)

		# 		##############################################################################
		# 		###### Check padding to avoid key not found with only "4.0" not "4.00" for label
		# 		##############################################################################
		# 		chkpad=str(runvalue).split(".") 

		# 		if len(chkpad[1])==1:
		# 			tempval=chkpad[1]+"0"
		# 			valuelabel=chkpad[0]+"." +tempval

		# 		else:
		# 			valuelabel=str(runvalue)
		# 		self.labeldisplay[valuelabel][valuelabel].configure(background="lightpink")

		# 		runcost=runvalue*volumestep
		# 		runcostbuy +=runcost ### accume initial cost value to buy
		# 		print("initial cost to buy =" , str(runcostbuy))
				
		# 		runvolumebuy+=volumestep

				
		# 		runvalue+=commonvaluestep
		# 		runvalue=round(runvalue,2)
			

		# 		runinvest -=runcost #### resul is 293.99999999999999994
		# 		runinvest=round(runinvest,2)
		# 		print (runinvest)

		# 	elif runinvest < (runvalue*volumestep):
		# 		print ("run invest is not enough break to exit tkconsole.py line 435")
		# 		break


		# self.configval["totalcostbuy"].set(runcostbuy)
		# self.configval["totalvolumebuy"].set(runvolumebuy)
		# self.configval["remaininvest"].set(runinvest)



	def process(self):
		print("Hello World")