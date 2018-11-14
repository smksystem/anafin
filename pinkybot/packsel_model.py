from pinkybot.models import monitorbidoffer,updaterefresh,valuechange
from elasticsearch import Elasticsearch

import pytz
class PackSelModel:
	"""docstring for ClassName"""
	createdFlag=""
	def __init__(self):
		pass
	# def initialupdatestockvalue():
		

	# 	print ( "initial update stock value")
	def updatestockvaluechange(stockdata):

		print("model of update value is called")
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

	def InsertMonitorBidOffer(stock,timestamp,bid,offer,bidvolumn,offervolumn):
		print ("Insert value into els system")
		
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

	def updaterefresh(mytable):
		# compare logic here to update table or not 
		print ("hello update refresh table databases packsel_model.py line 93")
		print (mytable)
		for myrow in mytable:
			print (myrow[2])
			chkorderno=updaterefresh.objects.filter(orderno=myrow[2])
			if not chkorderno.exists():
				print("Insert new row of order")
				newrow=updaterefresh(orderno=myrow[2],
									time=myrow[3],
									symbole=myrow[4],
									side=myrow[5],
									price=myrow[6],
									volume=myrow[7],
									matched=myrow[8],
									balance=myrow[9],
									cancelled=myrow[10],
									status=myrow[11],
									)
				newrow.save()
			else:
				print ("Order already existing")
				# Blog.objects.values('id', 'name')
				tochk=chkorderno.values()
				print (tochk[0]["orderno"])
				
				# a = 2 if i in [1, 3, 6] else 7


				# print (updaterow)
				# exit()
				print (myrow)
				for index, (column,myvalue) in enumerate(tochk[0].items()):
					if column != "id" and column != "date":
						updaterow=True if (myvalue != myrow[index+1]) else False
						# print (index,column,value,myrow[index+1],updaterow)
						
						if updaterow==True:

							
							
							updatecolumnval=updaterefresh.objects.filter(orderno=myrow[2]).update(**{column:myrow[index+1]})
							
							
							print (index,column,myvalue,myrow[index+1],updaterow)
							# updaterow=chkorderno	

							# UPDATE books_publisher
							# SET name = 'Apress Publishing'
							# WHERE id = 1;
							# updaterow.save()

							print ("update row into table")

		
		return 0

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