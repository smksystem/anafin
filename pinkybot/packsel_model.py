from pinkybot.models import monitorbidoffer,updaterefresh,valuechange,keepconfig,keeplogin
# from elasticsearch import Elasticsearch
import tkinter as tk
import pytz
class PackSelModel:

	
	createdFlag=""
	def __init__(self):
		# self.log=applog
		self.log["applog"].info("Initialize log of packsel_model")
	# def initialupdatestockvalue():
		

	# 	print ( "initial update stock value")
	def loadparameter(source=""):
		# log["applog"].info("Initialize log of packsel_model")
		# print("\nStart Load parameter packsel_model.py line 15 in def PackSelModel")
		currentconfig=keepconfig.objects.filter(pluginfile=source)

		# tochk=currentconfig.values()
		if currentconfig.exists():
			
			# print(currentconfig.values())
			loadparams=currentconfig.values()
			return loadparams[0]
			# for params,params_value in loadparams[0].items():
			# 	print(params,params_value)


		else:
			print("**************")
			print("\nError: with no any parameter configured please check database !!!")
			print("**************")
			exit()
	def getloginDefault():
		def_loginparams=keeplogin.objects.filter(currentuseId="YES").values()
		# print(def_loginparams[0])
		return def_loginparams[0]

	def getloginModel(myprofileId=""):
		
		if myprofileId!="all":
			loginparams=keeplogin.objects.filter(profileId=myprofileId).values()
		else:
			loginparams=keeplogin.objects.all().values()
		return loginparams
	def getDefaultConfig():
		# if myconfigId!="all":
		def_configparams=keepconfig.objects.filter(currentuseId="YES").values()

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
		# print(def_configparams)
		myrange=def_configparams[0]["rangeselect"]
		# print(myrange)

		# return_def_configparams=def_configparams[0]

		# return_def_configparams['floorvaluerange']=rangeData[myrange][0]
		# return_def_configparams['topvaluerange']=rangeData[myrange][1]
		# return_def_configparams['commonvaluestep']=rangeData[myrange][2]

		#################################################################################
		############ Initial value of configuration here from database + config value
		#################################################################################

		configval={
			"planname":tk.StringVar(value=def_configparams[0]["planname"]),
			"rangeselect":tk.StringVar(value=def_configparams[0]["rangeselect"]),
			"monitorstock":tk.StringVar(value=def_configparams[0]["monitorstock"]),
			"initinvest":tk.StringVar(value=def_configparams[0]["initinvest"]),

			"volumestep":tk.StringVar(value=def_configparams[0]["volumestep"]),
			"profitstep":tk.StringVar(value=def_configparams[0]["profitstep"]),
			"topvaluebuy":tk.StringVar(value=def_configparams[0]["topvaluebuy"]),
			"startvaluebuy":tk.StringVar(value=def_configparams[0]["startvaluebuy"]),
			"stopvaluebuy":tk.StringVar(value=def_configparams[0]["stopvaluebuy"]),
			"floorvaluebuy":tk.StringVar(value=def_configparams[0]["floorvaluebuy"]),
			"firstbuyflag":tk.StringVar(value=def_configparams[0]["firstbuyflag"]),
			"pluginfile":tk.StringVar(value=def_configparams[0]["pluginfile"]),
			"currentuseId":tk.StringVar(value=def_configparams[0]["currentuseId"]),

			"floorvaluerange":tk.StringVar(value=rangeData[myrange][0]),
			"topvaluerange":tk.StringVar(value=rangeData[myrange][1]),
			"commonvaluestep":tk.StringVar(value=rangeData[myrange][2]),
			
			"runningmode":tk.StringVar(value=def_configparams[0]["runningmode"]),
			"totalcostbuy":tk.StringVar(value=def_configparams[0]["totalcostbuy"]),
			"totalvolumebuy":tk.StringVar(value=def_configparams[0]["totalvolumebuy"]),
			# "totalvolumebuy":tk.StringVar(value="pluginvalue"),

			# commonstep=tk.StringVar(value=configparams["step"])  # step from range calculation
			
			"stockpin":tk.StringVar(),

			"remaininvest":tk.StringVar(value=def_configparams[0]["remaininvest"]),
		}




		# print(return_def_configparams)
		return configval

	def getConfigModel(myconfigId=""):
		if myconfigId!="all":
			configparams=keepconfig.objects.filter(planname=myconfigId).values()
		else:
			configparams=keepconfig.objects.all().values()
		return configparams
	def deleteconfigModel(planname):
		deleteresult=keepconfig.objects.filter(planname=planname).delete()
		return deleteresult[0]

	def deleteloginModel(profileId):
		print("Delete Profile Login")
		# instance = keeplogin.objects.get(brokeId=brokeId)
		profileresult=keeplogin.objects.filter(profileId=profileId).delete()
		print("\n\n")
		print(profileresult)
		print("\n\n")
		if profileresult[0]==1:
			print("delete succeded one record")
		elif profileresult[0]==0:
			print("not found any record to delete")
		elif profileresult[0]>1:
			print("delete error please check")
			# print(brokeresult)
		# if instance.exists():
		# 	instance.delete()
		# else:
		# 	print("No record found to delete")
	def	updateconfigModel(configparams,mode="Dict"):
		if mode=="GetValue":
			print("Get value with mode = GetValue")
			obj, created = keepconfig.objects.update_or_create(
			    		planname=configparams["planname"].get(),
			    defaults={

			    		'rangeselect':configparams["rangeselect"].get(),
			    		'monitorstock':configparams["monitorstock"].get(),

	   					"initinvest":configparams["initinvest"].get(),
						"volumestep":configparams["volumestep"].get(),
						"profitstep":configparams["profitstep"].get(),
						"topvaluebuy":configparams["topvaluebuy"].get(),
						"startvaluebuy":configparams["startvaluebuy"].get(),
						"stopvaluebuy":configparams["stopvaluebuy"].get(),
						"floorvaluebuy":configparams["floorvaluebuy"].get(),
						"pluginfile":configparams["pluginfile"].get(),
						"firstbuyflag":configparams["firstbuyflag"].get(),
						"currentuseId":configparams["currentuseId"].get(),
						"totalvolumebuy":configparams["totalvolumebuy"].get(),
						"totalcostbuy":configparams["totalcostbuy"].get(),
						"remaininvest":configparams["remaininvest"].get(),

			    		},	##### if found from above search, Update to which field that need to be updated.
			)
		elif mode=="Dict":
			
			obj, created = keepconfig.objects.update_or_create(
			    		planname=configparams["planname"],
			    defaults={

			    		'rangeselect':configparams["rangeselect"],
			    		'monitorstock':configparams["monitorstock"],

	   					"initinvest":configparams["initinvest"],
						"volumestep":configparams["volumestep"],
						"profitstep":configparams["profitstep"],
						"topvaluebuy":configparams["topvaluebuy"],
						"startvaluebuy":configparams["startvaluebuy"],
						"stopvaluebuy":configparams["stopvaluebuy"],
						"floorvaluebuy":configparams["floorvaluebuy"],
						"pluginfile":configparams["pluginfile"],
						"firstbuyflag":configparams["firstbuyflag"],
						"currentuseId":configparams["currentuseId"],
						"runningmode":configparams["runningmode"],
						# "totalvolumebuy":configparams["totalvolumebuy"],
						# "totalcostbuy":configparams["totalcostbuy"],
						# "remaininvest":configparams["remaininvest"],

			    		},	##### if found from above search, Update to which field that need to be updated.
			)
		print(obj,created)
		if created==True:
			# print("New record has been created")
			# print(obj.planname)
			return obj.planname
		else:
			return "__UpDated__"


	def updateloginModel(loginparams):
		
		print("Access to update packsel_model.py")
		print(loginparams)

		obj, created = keeplogin.objects.update_or_create(
		    		profileId=loginparams["profileId"],
		    defaults={

		    		'brokeId':loginparams["brokeId"],      													    ##### Search & insert if not found.
		    		'loginId':loginparams["loginId"],
		    		'passwordId':loginparams["passwordId"],
		    		'pinId':loginparams["pinId"],
		    		# 'profileId':loginparams["profileId"],
		    		'currentuseId':loginparams["currentuseId"],
		    		},	##### if found from above search, Update to which field that need to be updated.
		)
		if created==True:
			print("New record has been created")
			return loginparams["profileId"]
		else:
			print("Update record")
			return "UPDATED"

	def updatefirstorderbuy(planname,dataupdate="NO"):

		# self.log("applog")
		# self.log["applog"].debug("PlanName to update is below")
		# self.log["applog"].debug(planname)
		# print("Planname to update is below")
		# print(planname)

		updatekeepconfig=keepconfig.objects.filter(planname=planname).update(firstbuyflag=dataupdate)
		# print(updatekeepconfig)
		# updatefirstbuyflag=keepconfig(
		# 		firstbuyflag=dataupdate

		# 	)
		# updatefirstbuyflag.save()
	def updatestockvaluechange(stockdata):

		# print("model of update value is called packsel_model.py line 16")
		# print (stockdata)
		updaterow=valuechange(
				datefield=stockdata["datefield"],
				timestamp=stockdata["timestamp"],
				stockname=stockdata["stockname"],
				stockvalue=stockdata["stockvalue"]

			)
		updaterow.save()
		# newrow=updaterefresh(orderno=myrow[2],
		# 							time=myrow[3],
		# 							symbole=myrow[4],
		# 							side=myrow[5],
		# 							price=myrow[6],
		# 							volume=myrow[7],
		# 							matched=myrow[8],
		# 							balance=myrow[9],
		# 							cancelled=myrow[10],
		# 							status=myrow[11],
		# 							)
		# 		newrow.save()

	# def tkrefreshdb():

	# 	print("call packsel_model.py line 41")
		# chkorderno=updaterefresh.objects.filter(orderno=myrow[0])

	def InsertMonitorBidOffer(stock,timestamp,bid,offer,bidvolumn,offervolumn):
		# print ("Insert value into els system")
		
		es = Elasticsearch()
		
		
		doc_mappping = {

			"mappings": {
	    		"doc": {
			        "properties": {  
			            "timestamp": {  
			                "type":"date",
			                "format" : "yyyy-MM-dd HH:mm:ss",
			                
			                # "format":"dd/MM/yyy HH:mm:ss"
			            },
			        },
				},
			},
			# 'stock':stock,
			# 'timestamp': timestamp,
				
		}
		# timestamp='2015-01-01T12:10:30Z'
		print ( timestamp)
		doc = {

			'stock':stock,
			'timestamp': timestamp,
				
		}
		doc.update(bid)
		doc.update(offer)
		doc.update(bidvolumn)
		doc.update(offervolumn)

		print (doc)
		res=es.indices.create(index='monitorbidoffer',body=doc_mappping, ignore=400)
		# print (createdFlag)
		print(res)
		# print(res['error']['root_cause']['type'])
		# skipcreate=res['error']['root_cause']['type']
		# if (skipcreate=="resource_already_exists_exception"):
		# 		print("found index has been created set flag to created")
		# 		createdFlag="CREATED"

		res = es.index(index="monitorbidoffer", doc_type='doc', body=doc)
		print(res['result'])

		# exit()



# [['71913646', '17:09:57', 'WHA', 'B', '4.10', '600', '0', '600', '0', 'Pending(OF)', 'Detail', 'Cancel'], 
# ['71911327', '14:42:59', 'WHA', 'B', '4.08', '700', '0', '0', '700', 'Cancel(X)', 'Detail']]
	def updatematchstatus(resultMatch):
		updatecolumnval=updaterefresh.objects.filter(orderno=resultMatch["orderno"]).update(matchedtime= resultMatch["matchedtime"])

		
	def updaterefresh(self,mytable,fullrefresh="partial",*params_referorderno):
		# self.log("applog").warning("Notice this is updaterefresh")
		# compare logic here to update table or not 
		referorderno="None"
		if len(params_referorderno) != 0 : 
				# print("\nRefer order no is sent in refreshbtn packsel_model.py line 113 in def updaterefresh")
				# print(params_referorderno[0])

				referorderno=params_referorderno[0]

		
		result_updaterefresh=[]
		notmatchmonitoring=[]

		for myrow in mytable:
			myrow.append("matchtime")
			myrow.append(referorderno)
			dataparams={
					"orderno": myrow[0],
					"time":myrow[1],
					"symbole" :myrow[2],
					"side":myrow[3],
					"price":myrow[4],
					"volume":myrow[5],
					"matched":myrow[6],
					"balance":myrow[7],
					"cancelled":myrow[8],
					"status":myrow[9],
					"matchedtime":myrow[10],

					"referorderno":myrow[11],


			}
			# print("\n---Print myrow line 126 packsel_model.py def updaterefresh")
			# print(myrow)
			chkorderno=updaterefresh.objects.filter(orderno=myrow[0]) # SQL filter for order no to find existing record.
			self.log["applog"].debug("Result from query database filter by orderno")
			self.log["applog"].debug(chkorderno.values())
			# No check for refresh type it's all refresh at the first time to sync all db and rt


			if fullrefresh=="all": 
				# self.log["applog"].info("Refresh all database case ")
				# print("fullrefresh each row packsel_model.py line 112")
				if not chkorderno.exists():
					
					
					newrow=updaterefresh(**dataparams)
					newrow.save()
					result_updaterefresh.append(dataparams)




				elif chkorderno.exists():

					refreshrow=chkorderno.values()


					self.log["applog"].debug ("Refresh each row case chkorderno already existing in database and status")
					self.log["applog"].debug (refreshrow)
					self.log["applog"].debug (refreshrow[0]["status"])
					result_updaterefresh.append(refreshrow[0])
					
					# if refreshrow[0]["status"] != "Matched(M)": notmatchmonitoring.append(refreshrow[0])


			# for case new row when buy or sell 
			elif not chkorderno.exists() and fullrefresh=="partial":
				# print("Insert new row with chkorderno.exists and partial refresh of order below packsel_model.py line 144 ")
				
				# print(myrow)
				# [['71911327', '14:42:59', 'WHA', 'B', '4.08', '700', '0', '0', '700', 'Cancel(X)', 'Detail']]
				newrow=updaterefresh(**dataparams)
				newrow.save()
				result_updaterefresh.append(dataparams)


			elif chkorderno.exists() and fullrefresh=="partial":

				# print ("\n===Order already existing and fullrefresh = partial packsel_model.py line 158")
				tochk=chkorderno.values()
				

				# to check if database and rt table has the same data or not ?

				for index, (column,myvalue) in enumerate(tochk[0].items()):
					# index-=index
					# to exclude check below column
					if column != "id" and column != "date" and column !="matchedtime" and column != "referorderno":
						# print("--- index of myrow packsel_model.py line 170")
						# print (index,myvalue,myrow[index-1])
						updaterow=True if (myvalue != myrow[index-1]) else False
						# print (index,column,myvalue,myrow[index-1],updaterow)
						# print(dataparams["orderno"])
						if updaterow==True:
							# print("///////// data params in result updaterefresh packsel_model.py line 169")
							# print (dataparams in result_updaterefresh)
							updatecolumnval=updaterefresh.objects.filter(orderno=myrow[0]).update(**{column:myrow[index-1]})
							result_updaterefresh.append(dataparams) if (dataparams not in result_updaterefresh) else False
							updaterow=False
						# else:
						# 	updaterow=False
							# print ("--------------update row into table with existing and partial packsel_model.py line 172")
							# print(dataparams)
							# print (index,column,myvalue,myrow[index-1],updaterow)
		# print ("\nprint mytable packsel_model.py line 103 def updaterefresh")
		# print (mytable)
		# 
		
		# print("=!= result updaterefresh from realtime before return out from function packsel_model.py line 180")
		# print(result_updaterefresh)
		# return result_updaterefresh,notmatchmonitoring
		return result_updaterefresh


	def test_mysql():
		# pass
		print("insert a row")
		print(timestamp)
		
		print (stock)
		print (bid)
		print (bidvolumn)
		print(offer)
		print (offervolumn)
		bidoffertable=monitorbidoffer(mastershare=stock,
								timestamp=timestamp,

								bid1=float(bid[0]),
								offer1=float(offer[0]),
								bidvolumn1=float(bidvolumn[0]),
								offervolumn1=float(offer[0]),

								bid2=float(bid[1]),
								offer2=float(offer[1]),
								bidvolumn2=float(bidvolumn[1]),
								offervolumn2=float(offer[1]),

								bid3=float(bid[2]),
								offer3=float(offer[2]),
								bidvolumn3=float(bidvolumn[2]),
								offervolumn3=float(offer[2]),

								bid4=float(bid[3]),
								offer4=float(offer[3]),
								bidvolumn4=float(bidvolumn[3]),
								offervolumn4=float(offer[3]),

								bid5=float(bid[4]),
								offer5=float(offer[4]),
								bidvolumn5=float(bidvolumn[4]),
								offervolumn5=float(offer[4]),



							)
		bidoffertable.save()