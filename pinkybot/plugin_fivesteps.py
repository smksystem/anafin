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
		# print(confival)
		# exit()

		self.configval=configval
		# self.log["applog"].debug(self.configval)


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
		self.log["applog"].debug("Finish Prepare in def setlabeldisplay")
		self.txtout=conf_textout
		# str_totalcostbuy=str(runtotalcostbuy)
		# configval["totalcostbuy"].set(str_totalcostbuy)

		# str_totalvolumebuy=str(runtotalvolumebuy)
		# configval["totalvolumebuy"].set(str_totalvolumebuy)

		# str_remaininvest=str(remaininvest)
		# configval["remaininvest"].set(str_remaininvest)
		# print(configval)
		# return self.configval

	########################################################################
	############# Recheck this method carefully..... #######################
	########################################################################
	def putordermonitoring(self,result_order):

		if self.configval["runningmode"].get()=="monitor":
			self.log["applog"].info("Current mode is 'Monitoring only no auto sell or buy' ")
			return None

		tempadd=None
		notAllowTodd=None
		self.log["applog"].debug("Print result_order for def putordermonitoring before process function")
		self.log["applog"].debug(result_order)
		
		for linetable in result_order:
			if linetable["status"] == "Matched(M)":
				self.log["applog"].debug("Found matched detect")
				# self.txtout("Found match","white","yellow")
				# self.mycollectqueues["qvalchange"].put({"textout":"SELL==>>" + strprice + " VOLUME ==>>" + str(stepvol) })
				notAllowTodd=True ### Flag for monitoring each order 





				# break
			elif linetable["status"] != "Matched(M)" and len(self.matchedordermonitor)>0:
				# To check if already existing in matchedordermonitor or not
				for i,matchcheck in enumerate(self.matchedordermonitor):
					# print("\n ### Number of enumberate plugin_fivesteps.py line 246 in def putordermonitoring")
					# print((i+1),len(self.matchedordermonitor))
					self.log["applog"].debug("---Order No of linetable and matchcheck in def putordermonitoring")
					self.log["applog"].debug(linetable["orderno"])
					self.log["applog"].debug(matchcheck["orderno"])
					# compare to existing order
					if linetable["orderno"] == matchcheck["orderno"]:
						notAllowTodd=True
						# print("\n +++Found orderno update status below plugin_fivesteps.py line 251 in def updatematchstatus")
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
					
		# print("\n!!! Now Monitoring data after plugin_fivesteps.py line 254 in def putordermonitoring")
		# print(self.matchedordermonitor)
		self.log["applog"].debug("!!! Now Monitor self.matchedordermonitor and print result_order in def putordermonitoring")
		self.log["applog"].debug(self.matchedordermonitor)


	def order(self,controlorder="",orderdetail={},orderfn=""):
		self.log["applog"].debug("===== def order =====")
		self.log["applog"].debug(controlorder)
		self.log["applog"].debug(self.configval["runningmode"].get())
		if self.configval["runningmode"].get()=="monitor":
			self.log["applog"].info("Current mode is 'Monitoring only no auto sell or buy' ")
			return None

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
			# print("result_order first buy mode plugin_fivesteps.py line 228")
			self.log["applog"].debug(result_order)
			# self.log["applog"].debug(result_order[0])

			# self.txtout(result_order)
			# self.txtout("orderno" + result_order[0]["orderno"]+" with side "+result_order[0]["side"])


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
				self.log["applog"].debug(" == order idx buybybot before orderfn def order")
				self.log["applog"].debug(orderidx)

				result_order=orderfn(orderidx) ### got result from refreshbtn output.
				# [{'orderno': '174766', 'time': '14:03:56', 'symbole': 'WHA', 'side': 'S', 'price': '4.76', 'volume': '100', 'matched': '0', 'balance': '0', 'cancelled': '0', 'status': 'Pending(S)', 'matchedtime': 'matchtime', 'referorderfrom': 'refodfrm'}]
				# self.txtout(result_order)
				
				# assume that result_order with row 0 always the correct order result.


				# print("---Print result_order return from orderfn in for loop of orderdetail line 303 plugin_fivesteps.py line 303 in def order")
				# print(result_order,len(result_order))


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

			self.log["applog"].debug("result_order from sellbybot and firstbuy in def order")
			self.log["applog"].debug(result_order)
			
			return result_order

		
		# else:
			# pass	

	# called by change value
	def checkdownsidebuy(self,stockvalue):
		flstockvalue=float(stockvalue)
		flstartvaluebuy=float(self.configval["startvaluebuy"].get())
		# flcommonvaluestep=float(self.configval["commonvaluestep"].get())
		if flstockvalue<flstartvaluebuy :
			self.log["applog"].debug("check down side buy")
			flcomparediff=round(flstartvaluebuy-flstockvalue,2)
			flcommonvaluestep=float(self.configval["commonvaluestep"].get())
			
			self.log["applog"].debug("commonvaluestep")
			self.log["applog"].debug(flcommonvaluestep)

			if flcomparediff==flcommonvaluestep:
				self.log["applog"].debug("Start follow buy with below 'stockvalue' in def checkdownsidebuy")
				self.log["applog"].debug(stockvalue)	
				
				# resultbuy=self.order({'ordermode':'buybybot','firstbuy':'yes'},{},orderfn)
				orderlist=[{"price":strprice,
											"volume":str(stepvol),
											"order":orderside,
											"monitorstock":monitorstock,
											"referorderno":orderno,
											"stockpin":self.configval["stockpin"].get(),
								}]
				return {'ordermode':'buybybot','firstbuy':'no'}


	def checkprocess2order(self,rt_table,price_change,orderfn=""):
		self.log["applog"].debug("print price_change from checkprocess2order to order next plugin_fivesteps.py line 239")
		self.log["applog"].debug(price_change)
		# params={}
		
		# if table of realtime empty do execute below...

		self.log["applog"].debug("Print rt_table this value should be empty for first time buy")
		self.log["applog"].debug(rt_table)

		# self.log["applog"].debug("Print configval from def checkprocess2order before fist buy order")
		# self.log["applog"].debug(self.configval)

		self.txtout("Order with first buy = " + self.firstbuyflag)
		# self.txtout("")
		if self.configval["runningmode"].get()=="monitor":
			# self.log["applog"].info("Current mode is 'Monitoring only no auto sell or buy' ")
			return None

		if not rt_table and price_change==self.configval["startvaluebuy"].get() and self.firstbuyflag=="YES":
			# print("start first buy plugin_fivesteps.py line 241")

			# params["stockname"]=self.configval["stockname"]
			# params["startvolume"]=self.configval["totalvolumebuy"]
			# params["startvalue"]=self.configval["startvaluebuy"]
			# params["stockpin"]=self.configval["stockpin"]
			# params["order"]="buy"

			# use self.order instead direct call orderfn

			self.log["applog"].debug("Update first time to planname below ##git#")
			self.log["applog"].debug(self.configval["planname"].get())

			resultbuy=self.order({'ordermode':'buybybot','firstbuy':'yes'},{},orderfn)
			# self.txtout(resultbuy)

			self.firstbuyflag="NO"
			# resultbuy=orderfn(params) # return result from refresh for all line.
			

			# move append monitoring to order function.

			PackSelModel.updatefirstorderbuy(self.configval["planname"].get(),"NO")

		elif self.firstbuyflag=="NO":
			#####################################################################################
			# Check process when first buy already done and follow to buy when price is down.
			#####################################################################################
			self.log["applog"].debug("\n self.matchedordermonitor to monitor def checkprocess2order ")
			self.log["applog"].debug(self.matchedordermonitor)

			self.checkdownsidebuy(price_change)

		return self.matchedordermonitor


	def checkprocess2matchstatus(self,chk_params,orderfn=""):

		self.log["applog"].debug("\n=== Print check_params , self.matchedordermonitor in def checkprocess2matchstatus")
		for row in chk_params:
			self.log["applog"].debug(row)

		# self.log["applog"].debug(chk_params)
		
		self.log["applog"].debug("=== Print Matchedordermonitor in def checkprocess2matchstatus")
		# self.log["applog"].debug(self.matchedordermonitor)
		for row in self.matchedordermonitor:
			self.log["applog"].debug(row)
		row=""
		self.log["applog"].debug("#################################")
		######## Case set config = monitor
		if self.configval["runningmode"].get()=="monitor":
			# self.log["applog"].info("Current mode is 'Monitoring only no auto sell or buy' ")
			return None

		return_params=[]
		orderlist=[]
		datenow = datetime.datetime.now().strftime("%Y-%m-%d")
		matchedtime = datetime.datetime.now().strftime("%H:%M:%S")
		# currentdatetime=datenow+"_"+timenow

		# To change as link list later.
		# chk_params ==> result from check refresh_btn
		for chkresult in chk_params:
			for chkmatch in self.matchedordermonitor:
				# case of match found and exactly order.
				if chkresult["orderno"]==chkmatch["orderno"] and chkresult["status"]=="Matched(M)":
					self.txtout("Found Matched for orderno=" + chkresult["orderno"]+" at value="+chkresult["price"],"red","yellow")

					chkresult.update({
									"price": chkresult["price"],
									"matcheddate":datenow,
									"matchedtime":matchedtime,
						})
					if len(chkresult) > 0:
						self.log["applog"].debug("Update database if match with date and matchtime")
						self.log["applog"].debug(chkresult)
						PackSelModel.updatematchstatus(chkresult)
						self.mycollectqueues["qrefresh"].put({"qrefresh":"refreshtk","doupdatetk":[chkresult]})
						self.log["applog"].debug("Match found do remove array matchedordermonitor below data")
						self.log["applog"].debug(self.matchedordermonitor)
						self.matchedordermonitor.remove(chkmatch)
					self.log["applog"].debug("Set commonvaluestep from def checkprocess2matchstatus")
					self.log["applog"].debug(self.configval["commonvaluestep"].get())

					commonvaluestep=float(self.configval["commonvaluestep"].get())
					profitstep=float(self.configval["profitstep"].get())
					startvaluebuy=float(self.configval["startvaluebuy"].get())

					
					allvol=int(chkresult["volume"])
					stepvol=int(self.configval["volumestep"].get())
					floorvaluerange=float(self.configval["floorvaluerange"].get())
					topvaluebuy=float(self.configval["topvaluebuy"].get())
					difvaluerange=round((topvaluebuy - floorvaluerange),2)
					
					self.log["applog"].debug("---Print difvaluerange for topvaluerange - floorvaluerange in def checkprocess2matchstatus")
					self.log["applog"].debug(difvaluerange)

					orderno=chkresult["orderno"]
					monitorstock=chkresult["symbole"]
					sellprice= startvaluebuy
					buyprice= startvaluebuy

					# Get allvol from chkresult["volume"]
					if allvol >100 :
						allvalueidx=int(difvaluerange/commonvaluestep) + 1
						
						self.log["applog"].debug("---Print allvalueidx in case of alvol >100 for step value with difvaluerange/commonvaluestep def checkprocess2matchstatus")
						self.log["applog"].debug(allvalueidx)

						for runvolidx in range(allvalueidx):

							# runvol=
							self.log["applog"].debug("!!! Loop to print allvol volume in def checkprocess2matchstatus")
							self.log["applog"].debug(allvol)

							
							# if runvolidx < halfvolidx:
							# sellprice= startvaluebuy

							if sellprice < topvaluebuy:

								allvol=allvol-stepvol
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

								self.log["applog"].debug("@@@ ordertomonitor sell after def order def order")
								self.log["applog"].debug(ordertomonitor)
								
								# self.mycollectqueues["qrefresh"].put({"qrefresh":"refreshtk",
													# "doupdatetk":ordertomonitor})

								self.mycollectqueues["qvalchange"].put({"textout":"SELL==>>" + strprice + " VOLUME ==>>" + str(stepvol) })


							elif (buyprice >=floorvaluerange) and (allvol==0) :
								# buy price order
								self.log["applog"].debug("print buy value before processing in def checkprocess2matchstatus")
								self.log["applog"].debug (buyprice)


								chkpad=str(buyprice).split(".") 

								if len(chkpad[1])==1:
									tempval=chkpad[1]+"0"
									strprice=chkpad[0]+"." +tempval
								else:
									strprice=str(buyprice)

								orderside="buy"
								self.log["applog"].debug("--- summary buy price runvolidx,sellprice,buyprice")
								self.log["applog"].debug(runvolidx)
								self.log["applog"].debug(sellprice)
								self.log["applog"].debug(buyprice)
								
								orderlist=[{"price":strprice,
											"volume":str(stepvol),
											"order":orderside,
											"monitorstock":monitorstock,
											"referorderno":orderno,
											"stockpin":self.configval["stockpin"].get(),
								}]

								ordercontrol={'ordermode':'buybybot','firstbuy':'no'}

								ordertomonitor=self.order(ordercontrol,orderlist,orderfn)

								self.log["applog"].debug("@@@ ordertomonitor buy after def order def order")
								self.log["applog"].debug(ordertomonitor)

								self.mycollectqueues["qvalchange"].put({"textout":"ORDER BUY==>>" + strprice + " VOLUME ==>>" + str(stepvol) })
						
								buyprice=  round((buyprice - (profitstep * commonvaluestep)),2)

						return ordertomonitor	
					elif allvol==100:
					# Case of order buy by bot and order sell by bybot.
						self.log["applog"].debug("---allvol == 100 to sell or buy by bot def checkprocess2matchstatus")
						self.log["applog"].debug("+++print buy or sell in def checkprocess2matchstatus")
						self.log["applog"].debug(chkresult["side"])
						chkside=chkresult["side"]
						
						if chkside=="B" :
							ordermode="sellbybot"
							orderside="sell"
							botprice=round(float(chkresult["price"])+commonvaluestep,2)
							self.log["applog"].debug("Bot price to order buy with print chkresult[price] and botprice")
							self.log["applog"].debug(chkresult["price"])
							self.log["applog"].debug(botprice)

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

						self.log["applog"].debug("***Prepare ordermode,strprice to order side in def checkprocess2matchstatus")
						self.log["applog"].debug(ordermode)
						self.log["applog"].debug(strprice)

						self.log["applog"].debug("@@@ Print check result in def checkprocess2matchstatus")
						self.log["applog"].debug(chkresult)

						orderlist=[{"price":strprice,
											"volume":chkresult["volume"],
											"order":orderside,
											"monitorstock":chkresult["symbole"],
											"referorderno":chkresult["orderno"],
											"stockpin":self.configval["stockpin"].get(),
								}]					
						self.log["applog"].debug("!!!Print orderlist in def checkprocess2matchstatus")
						self.log["applog"].debug(orderlist)	
						ordercontrol={'ordermode':ordermode,'firstbuy':'no'}

						ordertomonitor=self.order(ordercontrol,orderlist,orderfn)
						self.log["applog"].debug("@@@ ordertomonitor bot order after def order def matchedordermonitor")
						self.log["applog"].debug(ordertomonitor)
					# return ordertomonitor

				# chk_params ==> result from check refresh_btn chkresult
				# chkmatch ==> from self.matchedordermonitor
				elif chkresult["orderno"]==chkmatch["orderno"] and chkresult["status"]!= "Matched(M)": 
					# return chk_params
					self.log["applog"].debug("==>> Enter Case else with not match for matchedordermonitor but found orderno in def checkprocess2matchstatus")
					self.log["applog"].debug("Print chkmatch from matchedordermonitor")
					self.log["applog"].debug(chkmatch)
					self.log["applog"].debug("Print chkresult in parameter chk_params from table")
					self.log["applog"].debug(chkresult)
					self.log["applog"].debug("Print input this def for parameter chk_params from table")
					self.log["applog"].debug(chk_params)
					# self.log["applog"].debug(chk_params)
					self.log["applog"].debug("Print chk_params for each row")
					for row in chk_params:
						self.log["applog"].debug(row)
					self.log["applog"].debug("Print monitor in matchedordermonitor ")
					for row in self.matchedordermonitor:
						self.log["applog"].debug(row)
					# self.log["applog"].debug(self.matchedordermonitor)


					# if not match update status instead.
					if chkmatch["status"]!=chkresult["status"]:
						chkmatch["status"]=chkresult["status"] 
		return chk_params
				# result_order=orderfn(params)
