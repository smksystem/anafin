######Package of selenium class.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC   
from selenium.webdriver.common.by import By
import datetime as dt
from pinkybot.packsel_model import PackSelModel
from django.utils import timezone
from datetime import datetime
import time 

class packselenium():
	"""docstring for packselenium"""
	def __init__(self,mode):
		self.mode=mode
		print ("running mode=" + mode)
	def xpathreturn(self,xplace=""):

		debugpath={
				# "xpathvaluemonitor":"//*[@id='instInfoEq']/tbody/tr[1]/td[2]/h2/span",
				"xpathlogin" : "/html/body/table[4]/tbody/tr/td[2]/table/tbody/tr[2]/td/table[1]/tbody/tr/td[2]/form/table/tbody/tr[3]/td[3]/font/input[2]",
				"xpathrealtime":"//*[@id='trading']/table/tbody/tr[1]/td/a/img",

				"xrtrefresh":"//*[@id='order_ctrl']/input[3]",




				"xfavorchk":"//*[@id='favourite-0']/ul/li[1]",
				"xstockup":"//*[@id='instInfoEq']/tbody/tr[1]/td[2]/h2/span",
				"xstockname":"//*[@id='eqQuoteSymbol']",
				"xstockvalue":"//*[@id='instInfoEq']/tbody/tr[1]/td[2]/h2/span",
				"xbuyradio":"//*[@id='placeEq']/div[1]/input[1]",
				"xstockorder":"//*[@id='eqSymbol']",
				"xstockvolumnorder":"//*[@id='placeEq']/div[2]/input",
				"xstockvalueorder":"//*[@id='placeEq']/div[3]/input[1]",
				"xstockpinorder":"//*[@id='placeEq']/div[3]/span/input",
				"xstocksubmitorder":"//*[@id='placeEq']/div[4]/input[1]",
				"xoutputordertable":"//*[@id='orderBodyEq']",
				"xoutputderivordertable":"//*[@id='orderDeriv']",

		}
		livepath={"valuemonitor":"",
				"xpathlogin":"/html/body/table[4]/tbody/tr/td[2]/table/tbody/tr[2]/td/table[1]/tbody/tr/td[2]/form/table/tbody/tr[3]/td[3]/font/input[2]",
				"xpathrealtime":"//*[@id='trading']/table/tbody/tr[1]/td/a/img",
				"xrtrefresh":"//*[@id='place-order-form']/refresh-ui-component/button/span[1]",
				"xfavorchk":"//*[@id='favourite-0']/ul/li[1]/editable-symbol-input/p",
				"xstockup":"//*[@id='page-0-container']/li[3]/mini-quote/div[1]/mini-quote-overview/div[5]/label",
				"xstockname":"//*[@id='favourite-0']/ul/li[1]/editable-symbol-input/p",
				"xstockvalue":"//*[@id='mini-quote-symbol']/div[2]/div[1]",
				"xbuyradio":"//*[@id='buy-btn']",
				"xstockorder":"//*[@id='place-order-symbol']/auto-complete/div/input[2]",
				"xstockvolumnorder":"//*[@id='place-order-volume']/div/volume-input/input",
				"xstockvalueorder":"//*[@id='place-order-price']/div/price-input/input",
				"xstockpinorder":"//*[@id='place-order-pin']/div/input",
				"xstocksubmitorder":"//*[@id='place-order-submit']",
				"xoutputordertable":"/html/body/app-controller/div/ul/li[3]/order/div[2]/order-status/div/div/div/ul/equity-order-status-row[2]/ul",
				# "xoutputordertable":"",
			
				"xoutputderivordertable":"//*[@id='fb-root']",
				"xstockconfirmorder":"/html/body/modal-layer/div/div/div/form/div[2]/div[1]/button",
			

# test

				# xpath for number of row 
				# /html/body/app-controller/div/ul/li[3]/order/div[2]/order-status/div/div/div/ul/equity-order-status-row[2]

				# /html/body/app-controller/div/ul/li[3]/order/div[2]/order-status/div/div/div/ul/equity-order-status-row[2]/ul/li[2]/a
				# /html/body/app-controller/div/ul/li[3]/order/div[2]/order-status/div/div/div/ul/equity-order-status-row[3]/ul/li[2]/a

				# /html/body/app-controller/div/ul/li[3]/order/div[2]/order-status/div/div/div/ul/equity-order-status-row[2]/ul/li[3]
				# /html/body/app-controller/div/ul/li[3]/order/div[2]/order-status/div/div/div/ul/equity-order-status-row[3]/ul/li[3]

		}

		xpath={"xdebug":debugpath,
				"xlive":livepath,
		}
		







		# print (xpath[self.mode]["xpathlogin"])
		# exit()
		return xpath[self.mode][xplace]


	def login(self,loginParams,qvalchange):

		self.mycollectqueues["qvalchange"]=qvalchange
		
		# for i in iter(self.qvalchange.get(),'STOP'):
			
		# for i in iter(self.qvalchange):
		# print( self.qvalchange.display())

		# print (self.qvalchange.get())
		# dataqueue={"textout":"Starting to login ... please wait ... "}

		self.mycollectqueues["qvalchange"].put({"textout":"Starting to login ... please wait ... "})

		# for job in iter(self.qvalchange.get, None):
			# print (job)
		

		# exit()

		driver = webdriver.Chrome()
		# put url here
		# exit()

		if self.mode=="xdebug":
			driver.get("http://localhost:8000/dummy/")
		elif self.mode=="xlive":
			driver.get("http://wen060.settrade.com/login.jsp?txtBrokerId="+loginParams["mybrokeId"])

		wait = WebDriverWait(driver, 10)

		# element = wait.until(EC.presence_of_element_located((By.XPATH, "")))

		element = wait.until(EC.presence_of_element_located((By.XPATH, self.xpathreturn("xpathlogin"))))


		print("super selenium class is called")



		elem = driver.find_element_by_name("txtLogin")
		elem.clear()
		# put user in key
		elem.send_keys(loginParams["myuser"]) 

		elem = driver.find_element_by_name("txtPassword")
		elem.clear()
		# put password in key
		elem.send_keys(loginParams["mypassword"])

		elem.send_keys(Keys.RETURN)


		myclick=driver.find_elements_by_xpath(self.xpathreturn("xpathrealtime"))[0]
		myclick.click()


		# driver.switch_to_alert()
		main_window_handle = None
		while not main_window_handle:
			main_window_handle = driver.current_window_handle
		
		signin_window_handle = None
		while not signin_window_handle:
			for handle in driver.window_handles:
				if handle != main_window_handle:
					signin_window_handle = handle
					break
		driver.switch_to.window(signin_window_handle)
		# print(signin_window_handle)
		
		# wait until second pop up is complete loaded
		wait = WebDriverWait(driver, 30)



		# detect refresh button

		# element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='place-order-form']/refresh-ui-component/button/span[1]")))
		element = wait.until(EC.presence_of_element_located((By.XPATH, self.xpathreturn("xrtrefresh")))) 

		print("detect web load success")




		# stock = driver.find_elements_by_xpath("//*[@id='favourite-0']/ul/li[1]/editable-symbol-input/p")[0].text

		stock = driver.find_elements_by_xpath(self.xpathreturn("xstockname"))[0]
		
		# print ("stock is below found check login")
		if self.mode=="xdebug":
			stockname=stock.get_attribute('value')
		elif self.mode=="xlive":
			stockname=stock.text
		print ("stockname found is " + stockname)
		# exit()
		# stockname=stock.get_attribute("value")


		# one click to the first of favorite stock then wait
		# chkstock=driver.find_elements_by_xpath("//*[@id='favourite-0']/ul/li[1]/editable-symbol-input/p")[0]
		chkstock=driver.find_elements_by_xpath(self.xpathreturn("xfavorchk"))[0]
		chkstock.click()

		wait = WebDriverWait(driver, 10)

		# wait until value of stock is up and could see
		# elementClose = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='page-0-container']/li[3]/mini-quote/div[1]/mini-quote-overview/div[5]/label")))
		elementClose = wait.until(EC.presence_of_element_located((By.XPATH, self.xpathreturn("xstockup"))))
		print("wait finished")







		if (stock):
			# print("element is below")
			# print (element)
			self.mycollectqueues["qvalchange"].put({"textout":"Login success contiue monitoring : " + stockname,
				"stockname":stockname,
				})
			self.stockcompare="0.00"

		return driver

	def monitoring(self,handlewin,fav_no):

		# for test data
		# stock='TEST'
		# timestamp= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		# bid={'bid1':1,'bid2':2,'bid3':3,'bid4':4,'bid5':5}
		# offer={'offer1':6,'offer2':7,'offer3':8,'offer4':9,'offer10':10}
		# offervolumn={'offervolumn1':11,'offervolumn2':12,'offervolumn3':13,'offervolumn4':14,'offervolumn5':15}
		# bidvolumn={'bidvolumn1':16,'bidvolumn2':17,'bidvolumn3':18,'bidvolumn4':19,'bidvolumn5':20}

		# bidvolumn={}
		# for line in range(1,6):
			# bidvolumn["bidvolumn"+str(line)]="00004"

		# print(bidvolumn)
		# exit()		
		# PackSelModel.InsertMonitorBidOffer(stock,timestamp,bid,offer,bidvolumn,offervolumn)
		# exit()


		driver=handlewin

		bidvolumn={}
		bid={}
		offer={}
		offervolumn={}


		timestamp = datetime.utcnow()
		# timerecord = timestamp.strftime('%Y-%m-%d %H:%M:%S')
		# print("time stamp=" + str(timestamp))
		
		# try:

		# find the stock value
		stockvalue = driver.find_elements_by_xpath(self.xpathreturn("xstockvalue"))[0].text
		# print ("stock value now =" + stockvalue)	
		
		if self.stockcompare=="0.00" and stockvalue !="0.00":
			print("first stockvalue updated=" + stockvalue)
			print("first stockcompare updated=" + self.stockcompare)
			self.refreshbtn(driver)
			self.stockcompare=stockvalue
			self.mycollectqueues["qvalchange"].put({"stockvalue":stockvalue})
			PackSelModel.initialupdatestockvalue()
			

		elif (self.stockcompare!=stockvalue) and (self.stockcompare!="0.00"):
			print("update stock compare"+ stockvalue)
			self.refreshbtn(driver)
			self.stockcompare=stockvalue
			self.mycollectqueues["qvalchange"].put({"stockvalue":stockvalue})
			PackSelModel.updatestockvalue(1,2)
			print ("stockcompare="+self.stockcompare)

		# print ("reset stockvalue")
		stockvalue=""


		if not self.mycollectqueues["qorder"].empty(): 
			orderparams=self.mycollectqueues["qorder"].get()
			self.order(driver,orderparams)
		

			# for line in range(1,6):
					# test=driver.find_elements_by_xpath("//*[@id='bid-"+str(line)+"']")[0].text.replace(",","")
					# print(test)

					# bid["bid"+str(line)]=float(driver.find_elements_by_xpath("//*[@id='bid-"+str(line)+"']")[0].text.replace(",",""))
					# offer["offer"+str(line)]=float(driver.find_elements_by_xpath("//*[@id='offer-"+str(line)+"']")[0].text.replace(",",""))
					# bidvolumn["bidvolumn"+ str(line)]=float(driver.find_elements_by_xpath("//*[@id='bid-volume-"+str(line)+"']")[0].text.replace(",",""))
					# offervolumn["offervolumn"+str(line)]=float(driver.find_elements_by_xpath("//*[@id='offer-volume-"+str(line)+"']")[0].text.replace(",",""))

			# timestamp = timezone.now()
			# timestamp = datetime.utcnow()
			# timestampELS = timestamp.isoformat(' ','seconds')
			
			# print("Time record is =" + timestampELS)
			# exit()
			#

			# face to problem with float to string while ATO,ATC
			# PackSelModel.InsertMonitorBidOffer(stock,timestampELS,bid,offer,bidvolumn,offervolumn)

			# bidvolumn.clear()
			# bid.clear()
			# offer.clear()
			# offervolumn.clear()

		# except:
		# 	stockvalue=""
		# 	pass

	def order(self,driver,orderparams):
		print (orderparams)
		# stockvalue = driver.find_elements_by_xpath(self.xpathreturn("xbuyradio"))[0].text
		orderside=orderparams["order"]
		if orderside=="buy":
			print("order buy now")
			chkstock=driver.find_elements_by_xpath(self.xpathreturn("xbuyradio"))[0].click()
			print(chkstock)

			elem = driver.find_element_by_xpath(self.xpathreturn("xstockorder"))
			elem.clear()
			# put user in key
			elem.send_keys(orderparams["stockname"]) 

			elem = driver.find_element_by_xpath(self.xpathreturn("xstockvolumnorder"))
			elem.clear()
			# put user in key
			elem.send_keys(orderparams["startvolume"]) 

			elem = driver.find_element_by_xpath(self.xpathreturn("xstockvalueorder"))
			elem.clear()
			# put user in key
			elem.send_keys(orderparams["startvalue"]) 

			elem = driver.find_element_by_xpath(self.xpathreturn("xstockpinorder"))
			elem.clear()
			# put user in key
			elem.send_keys(orderparams["stockpin"]) 

			elem = driver.find_element_by_xpath(self.xpathreturn("xstocksubmitorder")).click()

			if self.mode=="xlive":

				elem = driver.find_element_by_xpath(self.xpathreturn("xstockconfirmorder")).click()				

			elif self.mode=="xdebug":
				elem = driver.switch_to_alert().accept()


			# confirm ok then check refresh 
			self.refreshbtn(driver)



		elif orderside=="sell":
			pass

	def refreshbtn(self,driver):


		# try:
		print ("refresh botton press")
		# elem = driver.find_element_by_xpath(self.xpathreturn("xrtrefresh")).click()
		elem = driver.find_element_by_xpath("//*[@id='order_ctrl']/input[3]").click()
		# exit()

		wait = WebDriverWait(driver, 30)
		WebElement = wait.until(EC.presence_of_element_located((By.XPATH, self.xpathreturn("xoutputderivordertable"))));

		time.sleep(0.5)

		print("wait finished")

		if self.mode=="xlive":

			# /html/body/app-controller/div/ul/li[3]/order/div[2]/order-status/div/div/div/ul/equity-order-status-row[2]

			# /html/body/app-controller/div/ul/li[3]/order/div[2]/order-status/div/div/div/ul/equity-order-status-row[2]
			roworder = driver.find_elements_by_xpath("/html/body/app-controller/div/ul/li[3]/order/div[2]/order-status/div/div/div/ul/*")
			print ( roworder)
			print(len(roworder))
			# print ( roworder.text)
			# test=roworder.find_elements_by_xpath("./")

			# print (test.text)
			# print (test)
			for myrow in roworder:
				print ("total rows=" + str(len(roworder)))
				print ("row=" + myrow.text)
				print ("lenght of text=" + str(len(myrow.text)))
				if len(myrow.text) != 0:
					print("enter loop find column")
					columes=myrow.find_elements_by_tag_name("li")
					for mycolume in columes:
						print (mycolume)
						print (mycolume.text)
						col_dict.append(mycolume.text)
				
				row_dict.append(col_dict)
		elif self.mode=="xdebug":
			table_id = driver.find_element_by_xpath( self.xpathreturn("xoutputordertable"))
			tablerow=table_id.find_elements_by_xpath(".//tr")
			col_dict=[]
			row_dict=[]
			for row in tablerow:

				tablecollume=row.find_elements_by_xpath(".//td")
				for col in tablecollume:
					# print (col.text)
					col_dict.append(col.text)
				# print (col_dict)
				row_dict.append(col_dict)
				col_dict=[]
				# print (row_dict)
		print (row_dict)
		self.mycollectqueues["qdatarefresh"].put(row_dict)

		# print(row_dict[0])
		# except:
		# 	pass				