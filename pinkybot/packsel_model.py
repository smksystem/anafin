from pinkybot.models import monitorbidoffer,updaterefresh,valuechange,keepconfig,keeplogin
# from elasticsearch import Elasticsearch

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
		print("\nStart Load parameter packsel_model.py line 15 in def PackSelModel")
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
	def getloginModel(mybrokeId=""):
		loginparams=keeplogin.objects.filter(brokeId=mybrokeId).values()
		return loginparams[0]
	def updateloginModel(loginparams):
		
		print("Access to update packsel_model.py")
		print(loginparams)

		obj, created = keeplogin.objects.update_or_create(
		    brokeId=loginparams["brokeId"],      													    ##### Search & insert if not found.
		    defaults={'loginId':loginparams["loginId"],
		    		'passwordId':loginparams["passwordId"],
		    		'pinId':loginparams["pinId"]},	##### if found from above search, Update to which field that need to be updated.
		)
		if created==True:
			print("New record has been created")
		else:
			print("Update record")
		# print (obj,created)

		# chklogin=keeplogin.objects.filter(brokeId=loginconfigparams[0]) # SQL filter for order no to find existing record.



		# if not chkorderno.exists():
		# 	newrow=updaterefresh(**dataparams)
		# 	newrow.save()
		
		# updatekeepconfig=keeploginconfig.objects.filter(planname="test").update(firstbuyflag=dataupdate)
	def updatefirstorderbuy(dataupdate="NO"):

		# self.log("applog")
		updatekeepconfig=keepconfig.objects.filter(planname="test").update(firstbuyflag=dataupdate)

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
				print("\nRefer order no is sent in refreshbtn packsel_model.py line 113 in def updaterefresh")
				print(params_referorderno[0])

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
			print("\n---Print myrow line 126 packsel_model.py def updaterefresh")
			print(myrow)
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