class fivesteps():


	############# 3 parameter to configure value of label display , color of label display and text out 
	def __init__(self):
		self.waitconfirmfirstorder=""
		self.params={ 
					"ordermode":"",
					# "order":"buy",
					# "stockname":configparams["stockname"].get(),
					# "startvalue":configparams["startvaluebuy"].get(),
					# "startvolume":configparams["totalvolumebuy"].get(),
					# "stockpin": configparams["stockpin"].get(),


			}
	def configlogic(self):
		
		self.buybyclick={
						"ordermode":"buybyclick",

						}
		self.buybybot={}
		self.sellbybot={}

	def setparameter(self,conf_params,conf_labeldisplay,conf_textout):
		print("set parameter of fivestep plugin_fivestep.py line 3")
		
		initinvest=20000
		volumestep	=100
		profitstep=2
		topvaluerange=4.96
		startvaluebuy=4.88
		floorvaluerange=4.78
		stopvaluerange=4.84


		str_initinvest=str(initinvest)
		str_volumestep	=str(volumestep)
		str_profitstep= str(profitstep)
		str_topvaluerange= str(topvaluerange)
		str_startvaluebuy= str(startvaluebuy)
		str_floorvaluerange= str(floorvaluerange)
		str_stopvaluerange= str(stopvaluerange)





		conf_params["initinvest"].set(str(initinvest))
		conf_params["volumestep"].set(str(volumestep))

		conf_params["profitstep"].set(str(profitstep))

		conf_params["topvaluerange"].set(str(topvaluerange))

		conf_params["startvaluebuy"].set(str(startvaluebuy))
		conf_params["floorvaluerange"].set(str(floorvaluerange))

		conf_params["stopvaluerange"].set(str(stopvaluerange))	# stop loss not to buy more	

		commonvaluestep=float(conf_params["commonstep"].get())

		runvalue=startvaluebuy # change text to numbering.
		stopvaluerange=topvaluerange
		runinvest=initinvest


		runcostbuy=0 #### purpose variable to calculate in below.
		runvolumebuy=0
		runconfig=floorvaluerange

		while (runconfig<=topvaluerange):
			runconfig= round(runconfig,2)

			print("run config plugin_fivesteps.py line 58")
			print(runconfig)
			##############################################################################
			###### Check padding to avoid key not found with only "4.0" not "4.00" for label
			##############################################################################
			chkpad=str(runconfig).split(".") 

			if len(chkpad[1])==1:
				tempval=chkpad[1]+"0"
				valuelabel=chkpad[0]+"." +tempval

			else:
				valuelabel=str(runconfig)
				
			print("config value step plugin_fivesteps.py line 71")
			print(valuelabel)
			conf_labeldisplay[valuelabel][valuelabel].configure(background="orangered")
			
			runconfig+=commonvaluestep




		while (runvalue<=stopvaluerange):				
				
			if runinvest > (runvalue*volumestep): #### check not to give -294, -xxx

				print("run value range = " + str(runvalue))
				stepcost=round((runvalue*volumestep),2)

				##############################################################################
				###### Check padding to avoid key not found with only "4.0" not "4.00" for label
				##############################################################################
				chkpad=str(runvalue).split(".") 

				if len(chkpad[1])==1:
					tempval=chkpad[1]+"0"
					valuelabel=chkpad[0]+"." +tempval

				else:
					valuelabel=str(runvalue)
				conf_labeldisplay[valuelabel][valuelabel].configure(background="lightgreen")

				runcost=runvalue*volumestep
				runcostbuy +=runcost ### accume initial cost value to buy
				print("initial cost to buy =" , str(runcostbuy))
				
				runvolumebuy+=volumestep

				
				runvalue+=commonvaluestep
				runvalue=round(runvalue,2)
			

				runinvest -=runcost #### resul is 293.99999999999999994
				runinvest=round(runinvest,2)
				print (runinvest)

			elif runinvest < (runvalue*volumestep):
				print ("run invest is not enough break to exit tkconsole.py line 435")
				break

		

		conf_labeldisplay[str_startvaluebuy][str_startvaluebuy].configure(background="yellow")

		conf_params["totalcostbuy"].set(runcostbuy)
		str_totalcostbuy=str(runcostbuy)
		conf_params["totalvolumebuy"].set(runvolumebuy)
		str_totalvolumebuy=str(runvolumebuy)
		conf_params["remaininvest"].set(runinvest)
		str_remaininvest=str(runinvest)

		print ("Initial Invest ====>>" + str(initinvest))
		print ("Volume Step =====>>" + str(volumestep))
		print ("Profit Step ====>>" + str(profitstep))
		print ("Top Value Range ====>>" + str(topvaluerange))
		print ("Start Value Buy ====>>" + str(startvaluebuy))
		print ("Floor Value Range ====>>" + str(floorvaluerange))
		print ("Total Cost Buy ====>>" + str(runcostbuy))
		print ("Total Volume Buy =======>>" + str(runvolumebuy))
		print ("Remain Invest Cost =========>>" + str(runinvest))

		conf_textout("Set Invest = " + str_initinvest ,"yellow","gray")
		conf_textout("Set Volume Step = " + str_volumestep ,"yellow","gray")
		conf_textout("Set Profit Step = " + str_profitstep ,"yellow","gray")
		conf_textout("Set Top Value Range = " + str_topvaluerange ,"yellow","gray")
		conf_textout("Set Start Value Buy = " + str_startvaluebuy ,"yellow","gray")
		conf_textout("Set Floor Value Range = " + str_floorvaluerange ,"yellow","gray")
		conf_textout("Set Total Price to Pay = " + str_totalcostbuy)
		conf_textout("Set Total Volume = " + str_totalvolumebuy,"white","peru")
		conf_textout("Remain Invest Cost = " + str_remaininvest)


	def process(self):
		print("Hello World")


	def order(self,params="",orderfn=""):


		print("access order process plugin_fivesteps.py line 159 88888888888888888")

		# if params["buycount"]=="1buy":
		self.params=params
		if self.params["ordermode"]=="buybyclick":
			print("first buy mode plugin_fivesteps.py line 161")
			result_order=orderfn(params)
			# print(params)
			# print(result_order)
			# chkrefresh["doupdatetk"]=list(filter(None.__ne__, chkrefresh["doupdatetk"]))
			for ordertoconfirm in result_order:
				self.waitconfirmfirstorder=ordertoconfirm["orderno"]
				print("confirm order plugin_fivesteps.py line 169")
				print ("------------confirm order to monitor="+ self.waitconfirmfirstorder)
				# 
		elif self.params["ordermode"]=="buybybot":
			print("start to sell")

		# else:
			# pass	
	def checkprocess2order(self,chk_params):
		print("check params from plugin_fivesteps.py line 166")
		print(chk_params)
		for chkresult in chk_params:
			if chkresult["orderno"]==self.waitconfirmfirstorder and chkresult["status"]=="Matched(M)":

				print("found match the first order !!!!!!!!!!!!!!!!++++++++")
				self.params["ordermode"]="buybybot"
				return {"confirmorder":chkresult["orderno"],"status":chkresult["status"]}
			else: 
				return "NOUPDATE"
				# result_order=orderfn(params)