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

		}
		livepath={"valuemonitor":"",
				"xpathlogin":"/html/body/table[4]/tbody/tr/td[2]/table/tbody/tr[2]/td/table[1]/tbody/tr/td[2]/form/table/tbody/tr[3]/td[3]/font/input[2]",
				"xpathrealtime":"//*[@id='trading']/table/tbody/tr[1]/td/a/img",
				"xrtrefresh":"//*[@id='place-order-form']/refresh-ui-component/button/span[1]",
				"xfavorchk":"//*[@id='favourite-0']/ul/li[1]/editable-symbol-input/p",
				"xstockup":"//*[@id='page-0-container']/li[3]/mini-quote/div[1]/mini-quote-overview/div[5]/label",
				"xstockname":"//*[@id='favourite-0']/ul/li[1]/editable-symbol-input/p",
				"xstockvalue":"//*[@id='mini-quote-symbol']/div[2]/div[1]",



		}

		xpath={"xdebug":debugpath,
				"xlive":livepath,
		}
		







		# print (xpath[self.mode]["xpathlogin"])
		# exit()
		return xpath[self.mode][xplace]


	def login(self,loginParams,qvalchange):
		self.qvalchange=qvalchange
		# for i in iter(self.qvalchange.get(),'STOP'):
			
		# for i in iter(self.qvalchange):
		# print( self.qvalchange.display())

		# print (self.qvalchange.get())
		# dataqueue={"textout":"Starting to login ... please wait ... "}

		self.qvalchange.put({"textout":"Starting to login ... please wait ... "})

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

		# stock = driver.find_elements_by_xpath(self.xpathreturn("xstockname"))[0]
		stock = driver.find_elements_by_xpath(self.xpathreturn("xstockname"))[0]
		# print ("stock is below found check login")

		stockname=stock.get_attribute("value")


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
			self.qvalchange.put({"textout":"Login success contiue monitoring : " + stockname,
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

		# add stock value here
		# stockvalue=driver.find_elements_by_xpath("")[0].text


		# wait.close()

		# monitortime = dt.datetime.now()
		# testtimezone=timezone.now()
		# print(testtimezone)

		bidvolumn={}
		bid={}
		offer={}
		offervolumn={}


		timestamp = datetime.utcnow()
		# timerecord = timestamp.strftime('%Y-%m-%d %H:%M:%S')

		try:
			# find the stock value
			stockvalue = driver.find_elements_by_xpath(self.xpathreturn("xstockvalue"))[0].text
			

			# print ("stock value="+stockvalue)
			# print ( "stock compare="+ self.stockcompare)
			if self.stockcompare=="0.00" and stockvalue !="0.00":
				print("first stock compare updated" + stockvalue)
				self.stockcompare=stockvalue
				self.qvalchange.put({"stockvalue":stockvalue})
				PackSelModel.initialupdatestockvalue()

			elif (self.stockcompare!=stockvalue) and (self.stockcompare!="0.00"):
				print("update stock compare"+ stockvalue)
				self.stockcompare=stockvalue
				self.qvalchange.put({"stockvalue":stockvalue})
				PackSelModel.updatestockvalue(1,2)
				print ("stockcompare="+self.stockcompare)

			stockvalue=""


			if not self.qorder.empty(): 
				orderparams=self.qorder.get()
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

		except KeyboardInterrupt:
			pass
		# print("exit program")
		# exit()

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

			elem=driver.switch_to_alert().accept()

			# confirm ok then check refresh 

			elem = driver.find_element_by_xpath(self.xpathreturn("xrtrefresh")).click()

			# wait until data arrive
			wait = WebDriverWait(driver, 10)
			elementClose = wait.until(EC.presence_of_element_located((By.XPATH, self.xpathreturn("xstockup"))))
			print("wait finished")


			# get all table list here


			table_id = driver.find_element_by_xpath(self.xpathreturn("xoutputordertable"))
			# print (table_id)
			
			for row in table_id.find_elements_by_xpath(".//tr"):
				# print (row)

				for col in row.find_elements_by_xpath(".//td"):
					# //*[@id="orderBodyEq"]/tbody/tr[1]/td[4]
					print (col.text)
				# row = table_id.find_elements(By.TAG_NAME, "tr") # get all of the rows in the table
				# print (row)			
			# for row in rows:
			# 	# Get the columns (all the column 2)        
				# col = row.find_elements(By.TAG_NAME, "td")[0] #note: index start from 0, 1 is col 2
				# print (col.text) #prints text from the element










			






		elif orderside=="sell":
			pass