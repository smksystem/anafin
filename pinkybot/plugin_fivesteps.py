import datetime
# import logging
from pinkybot.packsel_model import PackSelModel
# class fivesteps(logging):
class fivesteps():



	############# 3 parameter to configure value of label display , color of label display and text out 
	def __init__(self,applog):
		
		self.log=applog
		self.log["applog"].info("Initialize of plugin_fivesteps")
		# self.waitconfirmfirstorder=""
		self.matchedordermonitor=[]
		# self.firstbuyflag="YES"

		# self.configval=configval
		# print(self.configval)

	def setlabeldisplay(self,configval,conf_labeldisplay,conf_textout):

		############# this method Also calculate totalcostbuy,totoalvolumebuy,....
		self.log["console"].debug(configval)
		# print(confival)
		# exit()
		self.configval=configval
		# configval=PackSelModel.loadparameter("plugin_fivesteps")

		
		# self.consolelog.info("test")
		self.log["applog"].debug("def setparameter print initial All monitorstock Parameter")
		self.log["applog"].debug(configval)
		
		# initinvest=20000

		planname=configval["planname"].get()
		conf_textout("Plan Name = " + planname ,"red","white")

		rangeselect=configval["rangeselect"].get()
		conf_textout("Range Select = " + rangeselect ,"orange","green")

		monitorstock=configval["monitorstock"].get()
		conf_textout("Monitor Stock = " + monitorstock ,"orange","green")

		initinvest=configval["initinvest"].get()
		conf_textout("Set Invest = " + initinvest ,"yellow","gray")

		volumestep	=configval["volumestep"].get()
		conf_textout("Set Volume Step = " + volumestep ,"yellow","gray")

		profitstep=configval["profitstep"].get()
		conf_textout("Set Profit Step = " + profitstep ,"yellow","gray")

		topvaluerange=configval["topvaluerange"].get()
		conf_textout("Set Top Value Range = " + topvaluerange ,"yellow","gray")
		
		topvaluebuy=configval["topvaluebuy"].get()
		conf_textout("Set Top Value Buy = " + topvaluebuy ,"red","white")

		startvaluebuy=configval["startvaluebuy"].get()
		conf_textout("Set Start Value Buy = " + startvaluebuy ,"yellow","gray")


		stopvaluebuy=configval["stopvaluebuy"].get()
		conf_textout("Set Stop Value Buy = " + stopvaluebuy ,"yellow","gray")

		floorvaluebuy=configval["floorvaluebuy"].get()
		conf_textout("Set Floor Value Buy = " + floorvaluebuy ,"yellow","gray")


		floorvaluerange=configval["floorvaluerange"].get()
		conf_textout("Set Floor Value Range = " + floorvaluerange ,"yellow","gray")
		
		commonvaluestep=configval["commonvaluestep"].get()
		conf_textout("Set Common Value Step = " + commonvaluestep ,"red","white")

		self.firstbuyflag=configval["firstbuyflag"].get()
		conf_textout("First Buy Flag = " + self.firstbuyflag,"green","red")


		stockpin=configval["stockpin"].get()

		# self.firstbuyflag=configval["firstbuyflag"].get()
		# self.log["applog"].debug("def setparameter load firstbuyflag value")
		# self.log["applog"].debug(runfirstbuyflag)




		self.log["applog"].debug("Print stock pin value")
		self.log["applog"].debug(stockpin)

		runvalue=float(startvaluebuy) # change text to numbering.
		# runstartvalueragne=float(startvaluerange)
		runstopvaluerange=float(topvaluerange)
		runstopvaluebuy=float(stopvaluebuy)
		runstartvaluebuy=float(startvaluebuy)
		runtopvaluebuy=float(topvaluebuy)
		runfloorvaluebuy=float(floorvaluebuy)
		# runinvest=initinvest
		runinitinvest=float(initinvest)
		runcommonvaluestep=float(commonvaluestep)
		runvolumestep=float(volumestep)
		runfloorvaluerange=float(floorvaluerange)

		runtotalcostbuy=0 #### purpose variable to calculate in below.
		runtotalvolumebuy=0
		# runconfig=floorvaluerange




		###############################################################################
		# diffrange=round( runstopvaluerange-runstartvaluebuy,2)

		# runtotalcostbuy=runtotalvolumebuy * runstartvaluebuy
		###############################################################################

		# print("\n=== Remain cost buy from initial buy value is below plugin_fivesteps.py line 96 in def setparameter")
		# print(remaininvest)
		##################################################
		# To set upper range of initial buy value
		##################################################

		# runtotalvolumebuy=int((diffrange/runcommonvaluestep)*runvolumestep)
		remaininvest=round(runinitinvest,2)
		# return 0
		

		while (runvalue<=runtopvaluebuy):	

			# print(runvalue)				
			if remaininvest > (runvalue*runvolumestep): #### check not to give -294, -xxx
				# print("run value range = " + str(runvalue))
				stepcostdeduct=round((runvalue*runvolumestep),2)
				# print(stepcostdeduct)
				runtotalcostbuy=runtotalcostbuy+stepcostdeduct
				# print("Run total cost buy=")
				# print(runtotalcostbuy)
				# print(runinitinvest)
				# print("remaininvest=")
				runtotalvolumebuy=runtotalvolumebuy+runvolumestep
				# print(runtotalvolumebuy)
				remaininvest= remaininvest-stepcostdeduct
				# print(remaininvest)

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

				# runcostbuy +=runcost ### accume initial cost value to buy
				# print("initial cost to buy =" , str(runcostbuy))
				
				# runvolumebuy+=volumestep
				runvalue+=runcommonvaluestep
				runvalue=round(runvalue,2)

				# runinvest -=runcost #### resul is 293.99999999999999994
				# runinvest=round(runinvest,2)
				# print (runinvest)

			elif remaininvest < (runvalue*runvolumestep):
				self.log["applog"].debug("Round set int runtotalvolumebuy result")
				self.log["applog"].debug(round(int(runtotalvolumebuy),0))

				totalvolumebuy=round(int(runtotalvolumebuy),0)
				configval["totalvolumebuy"].set(totalvolumebuy)
				configval["totalcostbuy"].set(runtotalcostbuy)
				configval["remaininvest"].set(remaininvest)
				conf_textout("Runvalue less than TotalvalueBuy=" + str(runvalue),"red")
				conf_textout("Total Cost Buy = " + str(runtotalcostbuy) ,"red","white")
				conf_textout("Total Volume Buy =" + str(totalvolumebuy),"black","yellow")
				conf_textout("Remain Invest to Buy = " + str(remaininvest) ,"red","white")
				PackSelModel.updateconfigModel(configval,"GetValue")

				# configval["totalcostbuy"].set(totalcostbuy)
				self.log["console"].debug("Case runvalue*runvolumestep > remain invest.")
				break

		####### if case runvalue is not reach to topvaluebuy and not enter remaininvest < (runvalue*runvolumestep)
		####### for example buy at 4.72 top value at 4.80
		# print(runvalue,runtopvaluebuy,runtotalvolumebuy)
		if runvalue>runtopvaluebuy: 

			totalvolumebuy=round(int(runtotalvolumebuy),0)
			configval["totalvolumebuy"].set(totalvolumebuy)
			configval["remaininvest"].set(remaininvest)
			configval["totalcostbuy"].set(runtotalcostbuy)
			conf_textout("Runvalue MORE than TotalvalueBuy=" + str(runvalue),"red")
			conf_textout("Total Cost Buy =" + str(runtotalcostbuy),"green")
			conf_textout("Total Volume Buy ="+str(totalvolumebuy),"red")
			conf_textout("Remain Invest =" + str(remaininvest),"orange")
			PackSelModel.updateconfigModel(configval,"GetValue")

			print(remaininvest)

		conf_labeldisplay[startvaluebuy][startvaluebuy].configure(background="yellow")

		# return 0

		##################################################
		# To set down range of initial buy value
		##################################################
		runvalue=runfloorvaluebuy
		# print(runvalue)
		while (runvalue<=runstartvaluebuy):
			runvalue= round(runvalue,2)
			# print(runvalue)
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
			
			runvalue+=runcommonvaluestep


		
		######################## mark Start value to buy #######################
		# valuelabel=startvaluebuy
		conf_labeldisplay[startvaluebuy][startvaluebuy].configure(background="yellow")
		# conf_labeldisplay[valuelabel][valuelabel].configure(background="yellow")
		##############################################################################

		# str_totalcostbuy=str(runtotalcostbuy)
		# configval["totalcostbuy"].set(str_totalcostbuy)

		# str_totalvolumebuy=str(runtotalvolumebuy)
		# configval["totalvolumebuy"].set(str_totalvolumebuy)

		# str_remaininvest=str(remaininvest)
		# configval["remaininvest"].set(str_remaininvest)
		# print(configval)
		# return self.configval


	def putordermonitoring(self,result_order):

		print("\n!!! Now Monitoring before data plugin_fivesteps.py line 254 in def putordermonitoring")
		print(self.matchedordermonitor)

		print("\n!!! Print result_order in line 235 plugin_fivesteps.py in def putordermonitoring")
		print(result_order)
		tempadd=None
		notAllowTodd=None
		for linetable in result_order:
			if linetable["status"] == "Matched(M)":
				notAllowTodd=True ### Flag for monitoring each order 





				# break
			elif linetable["status"] != "Matched(M)" and len(self.matchedordermonitor)>0:
				# To check if already existing in matchedordermonitor or not
				for i,matchcheck in enumerate(self.matchedordermonitor):
					# print("\n ### Number of enumberate plugin_fivesteps.py line 246 in def putordermonitoring")
					# print((i+1),len(self.matchedordermonitor))
					print("\n---Order No of linetable and matchcheck plugin_fivesteps.py line 248 in def putordermonitoring")
					print(linetable["orderno"],matchcheck["orderno"])

					if linetable["orderno"] == matchcheck["orderno"]:
						notAllowTodd=True
						print("\n +++Found orderno update status below plugin_fivesteps.py line 251 in def updatematchstatus")
						matchcheck["status"]=linetable["status"]

						break

					elif linetable["orderno"] != matchcheck["orderno"]:
					 	notAllowTodd=False
					 	tempadd=linetable
					 	
					 	# break
					# if (i+1)==len(self.matchedordermonitor) and notAllowTodd==False:
					# 	tempadd=linetable
					# 	break

				if notAllowTodd==False :
					self.matchedordermonitor.append({"orderno":tempadd["orderno"],
											"price":tempadd["price"],
												"status":tempadd["status"],
												"referorderno":tempadd["referorderno"],
											})
			elif linetable["status"] != "Matched(M)" and len(self.matchedordermonitor)==0:
				print("\n===Print case linetable != matched[M] and len(self.matchedordermonitor==0) plugin_fivesteps.py line 273 in def putordermonitoring")
				notAllowTodd=False
				tempadd=linetable
				self.matchedordermonitor.append({"orderno":tempadd["orderno"],
												"price":tempadd["price"],
												"status":tempadd["status"],
												"referorderno":tempadd["referorderno"],
											})

			# if notAllowTodd==True or notAllowTodd==False:
			# 	break

					 	# break
		
			# notAllowTodd=False
					# self.matchedordermonitor.append(linetable)
					
		print("\n!!! Now Monitoring data after plugin_fivesteps.py line 254 in def putordermonitoring")
		print(self.matchedordermonitor)


	def order(self,controlorder="",orderdetail={},orderfn=""):


		# print("\naccess order process plugin_fivesteps.py line 159 ")
		# print(controlorder)
		# print(orderdetail)

		self.log["applog"].debug("===== def order =====")
		self.log["applog"].debug(controlorder)


		# if params["buycount"]=="1buy":
		# self.params=params

		if controlorder["ordermode"]=="buybybot" and controlorder["firstbuy"]=="yes":

			orderdetail["monitorstock"]=self.configval["monitorstock"].get()

			orderdetail["volume"]=self.configval["totalvolumebuy"].get()


			orderdetail["price"]=self.configval["startvaluebuy"].get()
			orderdetail["stockpin"]=self.configval["stockpin"].get()
			orderdetail["order"]="buy"
			# self.params[""]

			self.log["applog"].debug("def order: First volume to buy orderdetail in def order")
			# print("\n*** First volume to buy orderdetail plugin_fivesteps.py line 265 in def order")
			self.log["applog"].debug(orderdetail)
			# print(orderdetail)

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
			self.log["applog"].debug("!!! print of orderdetail case sellbybot firstbuy==no before for order idx in def order ")
			self.log["applog"].debug(orderdetail)

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
		self.log["applog"].debug("print price_change from checkprocess2order to order next plugin_fivesteps.py line 239")
		self.log["applog"].debug(price_change)
		# params={}
		
		# if table of realtime empty do execute below...

		self.log["applog"].debug("Print rt_table this value should be empty for first time buy")
		self.log["applog"].debug(rt_table)

		self.log["applog"].debug("Print configval from def checkprocess2order before fist buy order")
		self.log["applog"].debug(self.configval)

		if not rt_table and price_change==self.configval["startvaluebuy"].get() and self.firstbuyflag=="YES":
			# print("start first buy plugin_fivesteps.py line 241")

			# params["stockname"]=self.configval["stockname"]
			# params["startvolume"]=self.configval["totalvolumebuy"]
			# params["startvalue"]=self.configval["startvaluebuy"]
			# params["stockpin"]=self.configval["stockpin"]
			# params["order"]="buy"

			# use self.order instead direct call orderfn

			self.log["applog"].debug("Update first time to planname below ###")
			self.log["applog"].debug(self.configval["planname"].get())

			resultbuy=self.order({'ordermode':'buybybot','firstbuy':'yes'},{},orderfn)
			self.firstbuyflag="NO"
			# resultbuy=orderfn(params) # return result from refresh for all line.
			

			# move append monitoring to order function.

			PackSelModel.updatefirstorderbuy(self.configval["planname"].get(),"NO")

		print("\nprint self.matchedordermonitor to monitor in plugin_fivesteps.py line 309 def checkprocess2order ")
		print(self.matchedordermonitor)
		return self.matchedordermonitor


	def checkprocess2matchstatus(self,chk_params,orderfn=""):

		self.log["applog"].debug("=== Print check_params , self.matchedordermonitor in def checkprocess2matchstatus")
		self.log["applog"].debug(chk_params)
		self.log["applog"].debug("=== Print self.matchedordermonitor , self.matchedordermonitor in def checkprocess2matchstatus")
		self.log["applog"].debug(self.matchedordermonitor)

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

					chkresult.update({
									"price": chkresult["price"],
									"matcheddate":datenow,
									"matchedtime":matchedtime,
						})

					# print("\n @@@ Check Matched chkmatch=chkresult before put into database ")
					# print(chkmatch)
					
					PackSelModel.updatematchstatus(chkresult)

					# remove match index after add into database


					self.mycollectqueues["qrefresh"].put({"qrefresh":"refreshtk",
												"doupdatetk":[chkresult]})

					self.log["applog"].debug("Match found do remove matchedordermonitor below data")
					self.log["applog"].debug(self.matchedordermonitor)

					self.matchedordermonitor.remove(chkmatch)

					self.log["applog"].debug("Set commonvaluestep from def checkprocess2matchstatus")
					self.log["applog"].debug(self.configval["commonvaluestep"].get())


					commonvaluestep=float(self.configval["commonvaluestep"].get())
					profitstep=float(self.configval["profitstep"].get())
					startvaluebuy=float(self.configval["startvaluebuy"].get())

					
					allvol=int(chkresult["volume"])

					print("\n!!!Print allvol to order in line 450 file plugin_fivesteps.py in def checkprocess2matchstatus")
					print (allvol)

					stepvol=int(self.configval["volumestep"].get())
					floorvaluerange=float(self.configval["floorvaluerange"].get())
					topvaluerange=float(self.configval["topvaluerange"].get())

					difvaluerange=round((topvaluerange - floorvaluerange),2)
					
					print("\n---Print difvaluerange for topvaluerange - floorvaluerange in plugin_fivesteps.py line 445 def checkprocess2matchstatus")
					print(difvaluerange)
					# halfvolidx=int((((allvol/stepvol)/2)))

					


					# print(allvolidx)


					orderno=chkresult["orderno"]
					monitorstock=chkresult["symbole"]
					sellprice= startvaluebuy
					buyprice= startvaluebuy

					
					# for runvolidx in range(allvolidx):

					print("!!! Check chkresult,chkmatch buy or sell in case elif allvol==100 line 563 plugin_fivesteps.py in def checkprocess2matchstatus")
					print(chkresult)
					print(chkmatch)


					if allvol >100 :
						allvalueidx=int(difvaluerange/commonvaluestep) + 1
						
						print("\n---Print allvalueidx in case of alvol >100 for step value with difvaluerange/commonvaluestep in plugin_fivesteps.py line 449 def checkprocess2matchstatus")
						print(allvalueidx)

						for runvolidx in range(allvalueidx):

							# runvol=
							print("\n!!! Loop to print allvol volume plugin_fivesteps.py line 448 in def checkprocess2matchstatus")
							print(allvol)

							
							# if runvolidx < halfvolidx:
							if sellprice < topvaluerange:

								allvol= allvol-stepvol
								# sell price order
								# define profit step is step of price to get profit
								# such as 0.2 *1 or 0.2 *2
								sellprice=  round(((profitstep * commonvaluestep) + sellprice),2)
								chkpad=str(sellprice).split(".") 

								if len(chkpad[1])==1:
									tempval=chkpad[1]+"0"
									strprice=chkpad[0]+"." +tempval

								else:
									strprice=str(sellprice)
								
								orderside="sell"
								self.log["applog"].debug("--- summary sell price runvolidx,sellprice,buyprice,allvol,strprice")
								self.log["applog"].debug(runvolidx)
								self.log["applog"].debug(sellprice)
								self.log["applog"].debug(buyprice)
								self.log["applog"].debug(allvol)
								self.log["applog"].debug(strprice)
								
								orderlist=[{"price":strprice,
											"volume":str(stepvol),
											"order":orderside,
											"monitorstock":monitorstock,
											"referorderno":orderno,
											"stockpin":self.configval["stockpin"].get(),
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
								# buyprice=  round((buyprice),2)


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
								
								orderlist=[{"price":strprice,
											"volume":str(stepvol),
											"order":orderside,
											"monitorstock":monitorstock,
											"referorderno":orderno,
											"stockpin":self.configval["stockpin"].get(),
								}]

								ordercontrol={'ordermode':'buybybot','firstbuy':'no'}

								ordertomonitor=self.order(ordercontrol,orderlist,orderfn)

								print("\n@@@ ordertomonitor buy after def order line 447 plugin_fivesteps.py def order")
								print(ordertomonitor)

								self.mycollectqueues["qvalchange"].put({"textout":"ORDER BUY==>>" + strprice + " VOLUME ==>>" + str(stepvol) })
						
								buyprice=  round((buyprice - (profitstep * commonvaluestep)),2)

						return ordertomonitor	
					elif allvol==100:
						print("\n---allvol == 100 to sell or buy by bot plugin_fivesteps.py line 610 def checkprocess2matchstatus")
						print("\n+++print buy or sell in plugin_fivesteps.py line 611 def checkprocess2matchstatus")
						print(chkresult["side"])
						chkside=chkresult["side"]
						if chkside=="B" :
							ordermode="sellbybot"
							orderside="sell"
							self.log["applog"].debug("Bot price to order buy and chkresult[price]")
							self.log["applog"].debug(botprice,chkresult["price"])
							botprice=round(float(chkresult["price"])+commonvaluestep,2)

						elif chkside=="S":
							ordermode="buybybot"
							orderside="buy"
							
							botprice=round(float(chkresult["price"])-commonvaluestep,2)
							self.log["applog"].debug("Bot price to order sell")
							self.log["applog"].debug(botprice)

						chkpad=str(botprice).split(".") 

						if len(chkpad[1])==1:
							tempval=chkpad[1]+"0"
							strprice=chkpad[0]+"." +tempval

						else:
							strprice=str(botprice)

						print("\n***Prepare to order side in plugin_fivesteps.py line 618 in def checkprocess2matchstatus")
						print(ordermode,strprice)

						print("\n@@@ Print check result in plugin_fivesteps.py line 621 in def checkprocess2matchstatus")
						print(chkresult)

						orderlist=[{"price":strprice,
											"volume":chkresult["volume"],
											"order":orderside,
											"monitorstock":chkresult["symbole"],
											"referorderno":chkresult["orderno"],
											"stockpin":self.configval["stockpin"].get(),
								}]					
						print("\n!!!Print orderlist in line 644 plugin_fivesteps.py in def checkprocess2matchstatus")
						print(orderlist)	
						ordercontrol={'ordermode':ordermode,'firstbuy':'no'}

						ordertomonitor=self.order(ordercontrol,orderlist,orderfn)
						print("\n@@@ ordertomonitor bot order after def order line 447 plugin_fivesteps.py def matchedordermonitor")
						print(ordertomonitor)
					# return ordertomonitor

				# chk_params ==> result from check refresh_btn chkresult
				# chkmatch ==> from self.matchedordermonitor
				elif chkresult["orderno"]==chkmatch["orderno"] and chkresult["status"]!= "Matched(M)": 
					# return chk_params
					print("\n+++ Case else with not match but order match plugin_fivesteps.py def checkprocess2matchstatus line 414")
					print(chk_params)
					print(self.matchedordermonitor)


					# if not match update status instead.
					chkmatch["status"]=chkresult["status"] 
					# chkresult["refreorderno"]=chkmatch["referorderno"]

					return chk_params
				# result_order=orderfn(params)
