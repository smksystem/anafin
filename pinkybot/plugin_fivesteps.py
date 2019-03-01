import datetime
from pinkybot.packsel_model import PackSelModel
class fivesteps():


	############# 3 parameter to configure value of label display , color of label display and text out 
	def __init__(self):
		print("initialization of plugin_fivestep.py line 6 --------------")
		# self.waitconfirmfirstorder=""
		self.matchedordermonitor=[]
		self.firstbuyflag="FIRSTBUY"
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
		profitstep=1
		topvaluerange=4.80
		startvaluebuy=4.72
		floorvaluerange=4.60
		stopvaluerange=4.70

		# initinvest=20000
		# volumestep	=100
		# profitstep=1
		# topvaluerange=24.80
		# startvaluebuy=24.40
		# floorvaluerange=24.00
		# stopvaluerange=24.20		


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


		totalcostbuy=0 #### purpose variable to calculate in below.
		totalvolumebuy=0
		# runconfig=floorvaluerange


		str_initinvest=str(initinvest)
		str_volumestep	=str(volumestep)
		str_profitstep= str(profitstep)
		str_topvaluerange= str(topvaluerange)
		str_startvaluebuy= str(startvaluebuy)
		str_floorvaluerange= str(floorvaluerange)
		str_stopvaluerange= str(stopvaluerange)
		str_commonvaluestep=str(commonvaluestep)




		diffrange=round( stopvaluerange-startvaluebuy,2)
		print("\n==== Difference between top value buy and start value buy below plugin_fivesteps.py line 74 in def setparameter")
		print(diffrange)

		totalvolumebuy=int((diffrange/commonvaluestep)*volumestep)

		print("\n==== Total volume to buy from the initial buy value is blow plugin_fivesteps.py line 78 in def setparameter")
		print(totalvolumebuy)
		# runvolumebuy=totalvolumebuy


		totalcostbuy=totalvolumebuy * startvaluebuy

		print("\n=== Total cost to buy from the initial value is below plugin_fivesteps.py line 90 in def setparameter")
		print(totalcostbuy)

		remaininvest=round(initinvest-totalcostbuy,2)
		print("\n=== Remain cost buy from initial buy value is below plugin_fivesteps.py line 96 in def setparameter")
		print(remaininvest)
##################################################
# To set upper range of initial buy value
##################################################

		while (runvalue<=stopvaluerange):	

				
			if runinvest > (runvalue*volumestep): #### check not to give -294, -xxx

				# print("run value range = " + str(runvalue))
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

				# runcost=runvalue*volumestep
				# runcostbuy +=runcost ### accume initial cost value to buy
				# print("initial cost to buy =" , str(runcostbuy))
				
				# runvolumebuy+=volumestep

				
				runvalue+=commonvaluestep
				runvalue=round(runvalue,2)
			

				# runinvest -=runcost #### resul is 293.99999999999999994
				# runinvest=round(runinvest,2)
				# print (runinvest)

			elif runinvest < (runvalue*volumestep):
				print ("run invest is not enough break to exit tkconsole.py line 435")
				break


##################################################
# To set under range of initial buy value
##################################################
		runvalue=floorvaluerange
		while (runvalue<=startvaluebuy):
			runvalue= round(runvalue,2)

			# print("run config plugin_fivesteps.py line 58")
			# print(runvalue)
			##############################################################################
			###### Check padding to avoid key not found with only "4.0" not "4.00" for label
			##############################################################################
			chkpad=str(runvalue).split(".") 

			if len(chkpad[1])==1:
				tempval=chkpad[1]+"0"
				valuelabel=chkpad[0]+"." +tempval

			else:
				valuelabel=str(runvalue)
				
			# print("config value step plugin_fivesteps.py line 71")
			# print(valuelabel)
			
			conf_labeldisplay[valuelabel][valuelabel].configure(background="orangered")
			
			runvalue+=commonvaluestep


		

		conf_labeldisplay[str_startvaluebuy][str_startvaluebuy].configure(background="yellow")

		conf_params["totalcostbuy"].set(totalcostbuy)
		str_totalcostbuy=str(totalcostbuy)
		conf_params["totalvolumebuy"].set(totalvolumebuy)
		str_totalvolumebuy=str(totalvolumebuy)
		conf_params["remaininvest"].set(remaininvest)
		str_remaininvest=str(remaininvest)

		print ("Initial Invest ====>>" + str(initinvest))
		print ("Volume Step =====>>" + str(volumestep))
		print ("Profit Step ====>>" + str(profitstep))
		print("Common Value Step ====>>" + str(commonvaluestep))
		print ("Top Value Range ====>>" + str(topvaluerange))
		print ("Start Value Buy ====>>" + str(startvaluebuy))
		print ("Floor Value Range ====>>" + str(floorvaluerange))
		print ("Total Cost Buy ====>>" + str(totalcostbuy))
		print ("Total Volume Buy =======>>" + str(totalvolumebuy))
		print ("Remain Invest Cost =========>>" + str(remaininvest))
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
		
		self.conf_params={"initinvest":initinvest,
							"volumestep":volumestep,
							"profitstep":profitstep,
							"commonvaluestep":commonvaluestep,
							"topvaluerange":topvaluerange,
							"startvaluebuy":str_startvaluebuy,
							"floorvaluerange":floorvaluerange,
							"totalcostbuy":str_totalcostbuy,
							"totalvolumebuy":str_totalvolumebuy,
							"remaininvest":str_remaininvest,
							"stockname":stockname,
							"stockpin":stockpin,
		}
		# conf_params

		print("\n---Config parameter is following plugin_fivesteps.py line 170")
		print(self.conf_params)
		return self.conf_params

	def process(self):
		print("Hello World")

	def putordermonitoring(self,result_order):

		for linetable in result_order:
				if linetable["status"] != "Matched(M)":
					self.matchedordermonitor.append({"orderno":linetable["orderno"],
														"status":linetable["status"],
														"referorderno":linetable["referorderno"],
													})
					# self.matchedordermonitor.append(linetable)
					

				print("\nMonitor below data plugin_fivesteps.py line 254 in def putordermonitoring")
				print(self.matchedordermonitor)

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

			print("\n*** First volume to buy orderdetail plugin_fivesteps.py line 265 in def order")
			print(orderdetail)

			result_order=orderfn(orderdetail)

			
			# print("======= debug plugin_fivesteps.py line 205")
			print("result_order first buy mode plugin_fivesteps.py line 228")
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

			for orderidx in orderdetail:
				print("\n ==! order idx buybybot before orderfn line 286 plugin_fivesteps.py def order")
				print(orderidx)

				result_order=orderfn(orderidx) ### got result from refreshbtn output.
				# [{'orderno': '174766', 'time': '14:03:56', 'symbole': 'WHA', 'side': 'S', 'price': '4.76', 'volume': '100', 'matched': '0', 'balance': '0', 'cancelled': '0', 'status': 'Pending(S)', 'matchedtime': 'matchtime', 'referorderfrom': 'refodfrm'}]
				
				# assume that result_order with row 0 always the correct order result.


				print("---Print result_order return from orderfn in for loop of orderdetail line 303 plugin_fivesteps.py line 303 in def order")
				print(result_order,len(result_order))


				if len(result_order)!=0:
					result_order[0]["referorderno"]=orderidx["referorderno"]
					self.putordermonitoring(result_order) 
				
				# This is function to add monitoring

		elif controlorder["ordermode"]=="sellbybot" and controlorder["firstbuy"]=="no":
			# monitor_return
			# print("\n!!! print of orderdetail before for order idx plugin_fivesteps.py line 285 in def order ")
			# print(orderdetail)

			for orderidx in orderdetail:
				# print("\n ==! order idx before orderfn line 286 plugin_fivesteps.py def order")
				# print(orderidx)

				result_order=orderfn(orderidx) ### got result from refreshbtn output.
				# [{'orderno': '174766', 'time': '14:03:56', 'symbole': 'WHA', 'side': 'S', 'price': '4.76', 'volume': '100', 'matched': '0', 'balance': '0', 'cancelled': '0', 'status': 'Pending(S)', 'matchedtime': 'matchtime', 'referorderfrom': 'refodfrm'}]
				
				# assume that result_order with row 0 always the correct order result.
				if len(result_order)!=0:
					result_order[0]["referorderno"]=orderidx["referorderno"]
				
				# This is function to add monitoring
					self.putordermonitoring(result_order) 

			print("\nresult_order from sellbybot and firstbuy no plugin_fivesteps.py line 277 in def order")
			print(result_order)
			
			return result_order

		
		# else:
			# pass	

	# called by change value
	def checkprocess2order(self,rt_table,price_change,orderfn=""):
		print ("\nprint price_change from checkprocess2order to order next plugin_fivesteps.py line 239")
		print( price_change)
		# params={}
		
		# if table of realtime empty do execute below...

		print("\nprint rt_table this value should be empty for first time buy")
		print(rt_table)


		if not rt_table and price_change==self.conf_params["startvaluebuy"] and self.firstbuyflag=="FIRSTBUY":
			# print("start first buy plugin_fivesteps.py line 241")

			# params["stockname"]=self.conf_params["stockname"]
			# params["startvolume"]=self.conf_params["totalvolumebuy"]
			# params["startvalue"]=self.conf_params["startvaluebuy"]
			# params["stockpin"]=self.conf_params["stockpin"]
			# params["order"]="buy"

			# use self.order instead direct call orderfn
			resultbuy=self.order({'ordermode':'buybybot','firstbuy':'yes'},{},orderfn)
			self.firstbuyflag="DONE"
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

		# chk_params ==> result from check refresh_btn
		for chkresult in chk_params:
			# for matchindex,chkmatch in enumerate(self.matchedordermonitor):
			for chkmatch in self.matchedordermonitor:


				# print("\nindex of enumerate for monitoring plugin_fivesteps.py line 338 def checkprocess2matchstatus")
				# print (matchindex)

				if chkresult["orderno"]==chkmatch["orderno"] and chkresult["status"]=="Matched(M)":

					# print("\nfound Match(M) the first order plugin_fivesteps.py line 289 def checkprocess2matchstatus")


					# chkmatch=chkresult

					# all below is needed in the refresh for tkconsole.
					chkmatch.update({
									"status":chkresult["status"],
									"volume":chkresult["volume"],
									"price": chkresult["price"],
									"matcheddate":datenow,
									"matchedtime":matchedtime,
									"side":"B",
									# "nextordermode":"tosellbybot",

									})

					# print("\n @@@ Check Matched chkmatch=chkresult before put into database ")
					# print(chkmatch)
					
					PackSelModel.updatematchstatus(chkmatch)
					# remove match index after add into database


					self.mycollectqueues["qrefresh"].put({"qrefresh":"refreshtk",
												"doupdatetk":[chkmatch]})

					# print("\n Value now of matchedordermonitor is below plugin_fivesteps.py line 411 in def checkprocess2matchstatus")
					# print(self.matchedordermonitor)
					self.matchedordermonitor.remove(chkmatch)
					# print("\nFinish remove chkmatch print matchedordermonitor again")
					# print (self.matchedordermonitor)



					print("\nSet commonvaluestep plugin_fivesteps.py line 304 def checkprocess2matchstatus")
					print(self.conf_params)

					commonvaluestep=float(self.conf_params["commonvaluestep"])
					profitstep=float(self.conf_params["profitstep"])
					startvaluebuy=float(self.conf_params["startvaluebuy"])

					
					allvol=int(chkresult["volume"])
					stepvol=int(self.conf_params["volumestep"])
					floorvaluerange=float(self.conf_params["floorvaluerange"])
					topvaluerange=float(self.conf_params["topvaluerange"])

					difvaluerange=round((topvaluerange - floorvaluerange),2)
					print("\n---Print difvaluerange for topvaluerange - floorvaluerange in plugin_fivesteps.py line 445 def checkprocess2matchstatus")
					print(difvaluerange)
					# halfvolidx=int((((allvol/stepvol)/2)))

					allvalueidx=int(difvaluerange/commonvaluestep) 

					print("\n---Print allvalueidx for step value with difvaluerange/commonvaluestep in plugin_fivesteps.py line 449 def checkprocess2matchstatus")
					print(allvalueidx)

					# print(allvolidx)


					orderno=chkresult["orderno"]
					stockname=chkresult["symbole"]
					sellprice= startvaluebuy
					buyprice= startvaluebuy

					
					# for runvolidx in range(allvolidx):
					if allvol >100 :
						for runvolidx in range(allvalueidx):

							# runvol=
							print("\n!!! Loop to print allvol volume plugin_fivesteps.py line 448 in def checkprocess2matchstatus")
							print(allvol)

							
							# if runvolidx < halfvolidx:
							if sellprice < topvaluerange:

								allvol= allvol-stepvol
								# sell price order
								sellprice=  round(((profitstep * commonvaluestep) + sellprice),2)
								chkpad=str(sellprice).split(".") 

								if len(chkpad[1])==1:
									tempval=chkpad[1]+"0"
									strprice=chkpad[0]+"." +tempval

								else:
									strprice=str(sellprice)
								
								orderside="sell"
								print("\n--- summary sell price runvolidx,sellprice,buyprice,allvol")
								print(runvolidx,sellprice,buyprice,allvol)
								
								orderlist=[{"startvalue":strprice,
											"startvolume":str(stepvol),
											"order":orderside,
											"stockname":stockname,
											"referorderno":orderno,
											"stockpin":self.conf_params["stockpin"],
								}]


								ordercontrol={'ordermode':'sellbybot','firstbuy':'no'}


								ordertomonitor=self.order(ordercontrol,orderlist,orderfn)

								print("\n@@@ ordertomonitor sell after def order line 447 plugin_fivesteps.py def order")
								print(ordertomonitor)
								
								# self.mycollectqueues["qrefresh"].put({"qrefresh":"refreshtk",
													# "doupdatetk":ordertomonitor})

								self.mycollectqueues["qvalchange"].put({"textout":"SELL==>>" + strprice + " VOLUME ==>>" + str(stepvol) })


							elif (buyprice >=floorvaluerange) and (allvol==0) :
								# buy price order
								buyprice=  round((buyprice - (profitstep * commonvaluestep)),2)

								print("\nprint buy value before processing line 462 plugin_fivesteps.py in def checkprocess2matchstatus")
								print (buyprice)


								chkpad=str(buyprice).split(".") 

								if len(chkpad[1])==1:
									tempval=chkpad[1]+"0"
									strprice=chkpad[0]+"." +tempval

								else:
									strprice=str(buyprice)

								orderside="buy"
								print("\n--- summary buy price runvolidx,sellprice,buyprice")
								print(runvolidx,sellprice,buyprice)
								
								orderlist=[{"startvalue":strprice,
											"startvolume":str(stepvol),
											"order":orderside,
											"stockname":stockname,
											"referorderno":orderno,
											"stockpin":self.conf_params["stockpin"],
								}]

								ordercontrol={'ordermode':'buybybot','firstbuy':'no'}

								ordertomonitor=self.order(ordercontrol,orderlist,orderfn)

								print("\n@@@ ordertomonitor buy after def order line 447 plugin_fivesteps.py def order")
								print(ordertomonitor)

								self.mycollectqueues["qvalchange"].put({"textout":"ORDER BUY==>>" + strprice + " VOLUME ==>>" + str(stepvol) })
						

						return ordertomonitor	
					elif allvol==100:
						print("\n--- allvol == 100")

					# sellvolume=conf_params["volumestep"]
					# print("\ntotal order to buy after check match is below plugin_fivesteps.py line 347 def checkprocess2matchstatus")
					# print(orderlist)
					
					# 		print(chkresult)
					# print("\nupdate monitor order after check with rt table plugin_fivesteps.py line 299 def checkprocess2matchstatus")
					# print(self.matchedordermonitor)
					# print(chkmatch)
					

					# ordertomonitor=self.order(ordercontrol,orderlist,orderfn)
					
					# print("\n+++ ordertomonitor plugin_fivesteps.py line 439 in def checkprocess2matchstatus")
					# print (ordertomonitor)

					# only single match if more than one match need to add with array
					



					# chkreturn={"orderno":orderno, "matchedtime":matchedtime}

					# return chkreturn


				# chk_params ==> result from check refresh_btn chkresult
				# chkmatch ==> from self.matchedordermonitor
				elif chkresult["orderno"]==chkmatch["orderno"] and chkresult["status"]!= "Matched(M)": 
					# return chk_params
					print("\n+++ Case else with not match but order match plugin_fivesteps.py def checkprocess2matchstatus line 414")
					print(chk_params,self.matchedordermonitor)

					# chkmatch["status"]=chkresult["status"]
					# chkresult["refreorderno"]=chkmatch["referorderno"]

					return chk_params
				# result_order=orderfn(params)
