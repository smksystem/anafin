import datetime
from pinkybot.packsel_model import PackSelModel
class fivesteps():


	############# 3 parameter to configure value of label display , color of label display and text out 
	def __init__(self):
		print("initialization of plugin_fivestep.py line 6 --------------")
		# self.waitconfirmfirstorder=""
		self.matchedordermonitor=[]
		# self.conf_params={}

	# def configlogic(self):
		
	# 	self.buybyclick={
	# 					"ordermode":"buybyclick",

	# 					}
	# 	self.buybybot={}
	# 	self.sellbybot={}

	def setparameter(self,conf_params,conf_labeldisplay,conf_textout):
		print("set parameter of fivestep plugin_fivestep.py line 3")
		
		initinvest=20000
		volumestep	=100
		profitstep=2
		topvaluerange=4.82
		startvaluebuy=4.72
		floorvaluerange=4.60
		stopvaluerange=4.84







		conf_params["initinvest"].set(str(initinvest))
		conf_params["volumestep"].set(str(volumestep))

		conf_params["profitstep"].set(str(profitstep))

		conf_params["topvaluerange"].set(str(topvaluerange))

		conf_params["startvaluebuy"].set(str(startvaluebuy))
		conf_params["floorvaluerange"].set(str(floorvaluerange))

		conf_params["stopvaluerange"].set(str(stopvaluerange))	# stop loss not to buy more	

		commonvaluestep=float(conf_params["commonstep"].get())
		stockname=conf_params["stockname"].get()
		stockpin=conf_params["stockpin"].get()
		runvalue=startvaluebuy # change text to numbering.
		stopvaluerange=topvaluerange
		runinvest=initinvest


		runcostbuy=0 #### purpose variable to calculate in below.
		runvolumebuy=0
		runconfig=floorvaluerange


		str_initinvest=str(initinvest)
		str_volumestep	=str(volumestep)
		str_profitstep= str(profitstep)
		str_topvaluerange= str(topvaluerange)
		str_startvaluebuy= str(startvaluebuy)
		str_floorvaluerange= str(floorvaluerange)
		str_stopvaluerange= str(stopvaluerange)
		str_commonvaluestep=str(commonvaluestep)






		while (runconfig<=topvaluerange):
			runconfig= round(runconfig,2)

			# print("run config plugin_fivesteps.py line 58")
			# print(runconfig)
			##############################################################################
			###### Check padding to avoid key not found with only "4.0" not "4.00" for label
			##############################################################################
			chkpad=str(runconfig).split(".") 

			if len(chkpad[1])==1:
				tempval=chkpad[1]+"0"
				valuelabel=chkpad[0]+"." +tempval

			else:
				valuelabel=str(runconfig)
				
			# print("config value step plugin_fivesteps.py line 71")
			# print(valuelabel)
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
		print("Common Value Step ====>>" + str(commonvaluestep))
		print ("Top Value Range ====>>" + str(topvaluerange))
		print ("Start Value Buy ====>>" + str(startvaluebuy))
		print ("Floor Value Range ====>>" + str(floorvaluerange))
		print ("Total Cost Buy ====>>" + str(runcostbuy))
		print ("Total Volume Buy =======>>" + str(runvolumebuy))
		print ("Remain Invest Cost =========>>" + str(runinvest))
		print("StockName =========>>" + (stockname))  # get value from login function in pacsel.py self.stockdata.

		conf_textout("Set Invest = " + str_initinvest ,"yellow","gray")
		conf_textout("Set Volume Step = " + str_volumestep ,"yellow","gray")
		conf_textout("Set Profit Step = " + str_profitstep ,"yellow","gray")
		conf_textout("Set Common Value Step = " + str_commonvaluestep ,"red","white")
		conf_textout("Set Top Value Range = " + str_topvaluerange ,"yellow","gray")
		conf_textout("Set Start Value Buy = " + str_startvaluebuy ,"yellow","gray")
		conf_textout("Set Floor Value Range = " + str_floorvaluerange ,"yellow","gray")
		conf_textout("Set Total Price to Pay = " + str_totalcostbuy)
		conf_textout("Set Total Volume = " + str_totalvolumebuy,"white","peru")
		conf_textout("Remain Invest Cost = " + str_remaininvest)
		conf_textout("StockName = " + stockname)
		
		# print("Config parameter is following plugin_fivesteps.py line 170")
		# print(conf_params)
		self.conf_params={"initinvest":initinvest,
							"volumestep":volumestep,
							"profitstep":profitstep,
							"commonvaluestep":commonvaluestep,
							"topvaluerange":topvaluerange,
							"startvaluebuy":str_startvaluebuy,
							"floorvaluerange":floorvaluerange,
							"totalcostbuy":runcostbuy,
							"totalvolumebuy":runvolumebuy,
							"remaininvest":runinvest,
							"stockname":stockname,
							"stockpin":stockpin,
		}
		# conf_params

		return self.conf_params

	def process(self):
		print("Hello World")

	def putordermonitoring(self,result_order):

		for linetable in result_order:
				if linetable["status"] != "Matched(M)":
					self.matchedordermonitor.append({"orderno":linetable["orderno"],
														"status":linetable["status"],
													})
				print("\norder buy plugin_fivesteps.py line 254 in def checkprocess2order")
				print(linetable)

	def order(self,controlorder="",orderdetail={},orderfn=""):


		print("\naccess order process plugin_fivesteps.py line 159 ")
		print(controlorder)
		print(orderdetail)

		


		# if params["buycount"]=="1buy":
		# self.params=params

		if controlorder["ordermode"]=="buybybot" and controlorder["firstbuy"]=="yes":

			orderdetail["stockname"]=self.conf_params["stockname"]
			orderdetail["startvolume"]=self.conf_params["totalvolumebuy"]
			orderdetail["startvalue"]=self.conf_params["startvaluebuy"]
			orderdetail["stockpin"]=self.conf_params["stockpin"]
			orderdetail["order"]="buy"
			# self.params[""]


			result_order=orderfn(orderdetail)

			
			# print("======= debug plugin_fivesteps.py line 205")
			print("result_order first buy mode plugin_fivesteps.py line 228")
			# print(params)
			print(result_order)
			self.putordermonitoring(result_order)
			# self.mycollectqueues["qtimerefresh"].put({"command":"starttime"})			


			# chkrefresh["doupdatetk"]=list(filter(None.__ne__, chkrefresh["doupdatetk"]))
			# for ordertoconfirm in result_order:
			# 	self.waitconfirmfirstorder=ordertoconfirm["orderno"]


			# 	print("\nconfirm first buy order plugin_fivesteps.py line 169")
			# 	print ("------------confirm order to monitor="+ self.waitconfirmfirstorder)
				# 



		elif controlorder["ordermode"]=="buybybot" and controlorder["firstbuy"]=="no":
			pass
		elif controlorder["ordermode"]=="buybybot" and controlorder["firstbuy"]=="no":
			pass
		elif controlorder["ordermode"]=="sellbybot" and controlorder["firstbuy"]=="no":
			# monitor_return
			for orderidx in orderdetail:
				print("\norder idx before order line 207 plugin_fivesteps.py def order")
				print(orderidx)

				result_order=orderfn(orderidx) ### got result from refreshbtn output.
				# [{'orderno': '174766', 'time': '14:03:56', 'symbole': 'WHA', 'side': 'S', 'price': '4.76', 'volume': '100', 'matched': '0', 'balance': '0', 'cancelled': '0', 'status': 'Pending(S)', 'matchedtime': 'matchtime', 'referorderfrom': 'refodfrm'}]
				
				# assume that result_order with row 0 always the correct order result.
				result_order[0]["referorderfrom"]=orderidx["referfromorderno"]
				
				print("\n === result_order from orderfn (order in packsel.py) plugin_fivesteps.py line 269 def order")
				print(result_order,orderidx)

				PackSelModel.updatereferorderfrom(result_order[0]["orderno"],orderidx["referfromorderno"])

				# This is function to add monitoring
				self.putordermonitoring(result_order) 


			return result_order

		
		# else:
			# pass	
	def checkprocess2order(self,rt_table,price_change,orderfn=""):
		print ("\nprint price_change from checkprocess2order to order next plugin_fivesteps.py line 239")
		print( price_change)
		# params={}
		
		# if table of realtime empty do execute below...
		if not rt_table and price_change==self.conf_params["startvaluebuy"]:
			# print("start first buy plugin_fivesteps.py line 241")

			# params["stockname"]=self.conf_params["stockname"]
			# params["startvolume"]=self.conf_params["totalvolumebuy"]
			# params["startvalue"]=self.conf_params["startvaluebuy"]
			# params["stockpin"]=self.conf_params["stockpin"]
			# params["order"]="buy"

			# use self.order instead direct call orderfn
			resultbuy=self.order({'ordermode':'buybybot','firstbuy':'yes'},{},orderfn)
			# resultbuy=orderfn(params) # return result from refresh for all line.
			

			# move append monitoring to order function.
			

		print("\nprint self.matchedordermonitor to monitor in plugin_fivesteps.py line 309 def checkprocess2order ")
		print(self.matchedordermonitor)
		return self.matchedordermonitor


	def checkprocess2matchstatus(self,chk_params,orderfn=""):
		print("\ncheck params from plugin_fivesteps.py line 166")
		print(chk_params)
		print (self.matchedordermonitor)
		return_params=[]
		orderlist=[]
		datenow = datetime.datetime.now().strftime("%Y-%m-%d")
		matchedtime = datetime.datetime.now().strftime("%H:%M:%S")
		# currentdatetime=datenow+"_"+timenow

		# exit()
		for chkresult in chk_params:
			# for matchindex,chkmatch in enumerate(self.matchedordermonitor):
			for chkmatch in self.matchedordermonitor:


				# print("\nindex of enumerate for monitoring plugin_fivesteps.py line 338 def checkprocess2matchstatus")
				# print (matchindex)

				if chkresult["orderno"]==chkmatch["orderno"] and chkresult["status"]=="Matched(M)":

					print("\nfound Match(M) the first order plugin_fivesteps.py line 289 def checkprocess2matchstatus")



					chkmatch.update({
									"status":chkresult["status"],
									"volume":chkresult["volume"],
									"price": chkresult["price"],
									"matchdate":datenow,
									"matchtime":matchedtime,
									"nextordermode":"tosellbybot",

									})
					
					PackSelModel.updatematchstatus(chkmatch)
					# remove match index after add into database

					print("\nSet commonvaluestep plugin_fivesteps.py line 304 def checkprocess2matchstatus")
					print(self.conf_params)

					commonvaluestep=float(self.conf_params["commonvaluestep"])
					profitstep=float(self.conf_params["profitstep"])
					startvaluebuy=float(self.conf_params["startvaluebuy"])

					
					allvol=int(chkmatch["volume"])
					stepvol=int(self.conf_params["volumestep"])

					halfvolidx=int((((allvol/stepvol)/2)))
					allvolidx=int(allvol/stepvol) 

					# print(allvolidx)


					orderno=chkresult["orderno"]
					stockname=chkresult["symbole"]
					sellprice= startvaluebuy
					buyprice= startvaluebuy

					
					# self.matchedordermonitor.remove(self.matchedordermonitor[matchindex])
					self.matchedordermonitor.remove(chkmatch)


					for runvolidx in range(allvolidx):
						# runvol=
						print("\n!!! print volume")
						print(allvol)

						allvol= allvol-stepvol
						
						if runvolidx < halfvolidx:
							# sell price order
							sellprice=  round(((profitstep * commonvaluestep) + sellprice),2)
							chkpad=str(sellprice).split(".") 

							if len(chkpad[1])==1:
								tempval=chkpad[1]+"0"
								strprice=chkpad[0]+"." +tempval

							else:
								strprice=str(sellprice)
							orderside="sell"
							print("\n--- summary sell price runvolidx,halfvolidx,buyprice")
							print(runvolidx,halfvolidx,buyprice)

						elif runvolidx >= halfvolidx :
							# buy price order
							buyprice=  round((buyprice - (profitstep * commonvaluestep)),2)

							chkpad=str(buyprice).split(".") 

							if len(chkpad[1])==1:
								tempval=chkpad[1]+"0"
								strprice=chkpad[0]+"." +tempval

							else:
								strprice=str(buyprice)
							orderside="buy"
							print("\n--- summary buy price runvolidx,halfvolidx,buyprice")
							print(runvolidx,halfvolidx,buyprice)
						print("\n---order price")
						print(strprice)

						orderlist.append({"startvalue":strprice,
										"startvolume":str(stepvol),
										"order":orderside,
										"stockname":stockname,
										"referfromorderno":orderno,
										"stockpin":self.conf_params["stockpin"],
							})
					


					# sellvolume=conf_params["volumestep"]
					print("\ntotal order to buy after check match is below plugin_fivesteps.py line 347 def checkprocess2matchstatus")
					print(orderlist)
					
					# 		print(chkresult)
					print("\nupdate monitor order after check with rt table plugin_fivesteps.py line 299 def checkprocess2matchstatus")
					print(self.matchedordermonitor)
					# print(chkmatch)
					

					ordertomonitor=self.order({'ordermode':'sellbybot','firstbuy':'no'},orderlist,orderfn)
					print("+++ ordertomonitor plugin_fivesteps.py line 439 in def checkprocess2matchstatus")
					print (ordertomonitor)

					# only single match if more than one match need to add with array
					chkreturn={"orderno":orderno, "matchedtime":matchedtime}

					return chkreturn


				elif chkresult["orderno"]==chkmatch["orderno"] and chkresult["status"]!= "Matched(M)": 
					# 		return chk_params
					print("+++ Case else with not match but order match plugin_fivesteps.py def checkprocess2matchstatus line 414")
					print(chk_params)
					chkmatch["status"]=chkresult["status"]
					# chkmatch[""]=ordertomonitor["referfromorderno"]

					return chk_params
				# result_order=orderfn(params)
