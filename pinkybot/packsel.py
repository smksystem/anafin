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

# mydriver=0
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
				"xoutputordertable":"/html/body/app-controller/div/ul/li[3]/order/div[2]/order-status/div/div/div/ul",
									# /html/body/app-controller/div/ul/li[3]/order/div[2]/order-status/div/div/div/ul
				# "xoutputordertable":"",
				"xrtrefresh":"//*[@id='place-order-form']/refresh-ui-component/button/span[1]",
			
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


	# def login(self,loginParams,qvalchange):
	def login(self,loginParams):

		updatedate=datetime.now().strftime("%Y-%m-%d")
		timestamp=datetime.now().strftime("%H:%M:%S")
		stockname=""
		stockvalue=""

		self.stockdata={ 
			"datefield":updatedate,
			"timestamp":timestamp,
			"stockname":stockname,
			"stockvalue":stockvalue,

		}

		# self.mycollectqueues["qvalchange"]=qvalchange
		
		# for i in iter(self.qvalchange.get(),'STOP'):
			
		# for i in iter(self.qvalchange):
		# print( self.qvalchange.display())

		# print (self.qvalchange.get())
		# dataqueue={"textout":"Starting to login ... please wait ... "}

		# self.mycollectqueues["qvalchange"].put({"textout":"Starting to login ... please wait ... "})

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


		element = wait.until(EC.presence_of_element_located((By.XPATH, self.xpathreturn("xpathrealtime"))))

		# myclick=driver.find_elements_by_xpath(self.xpathreturn("xpathrealtime"))
		element.click()


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
		self.stockdata["stockname"]=stockname
		self.stockdata["stockvalue"] = driver.find_elements_by_xpath(self.xpathreturn("xstockvalue"))[0].text

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
			# pr3int (element)
			self.mycollectqueues["qvalchange"].put({"textout":"Login success contiue monitoring : " + stockname,
				"stockname":stockname,
				})
			self.stockcompare="0.00"
		# print(self.stockdata)
		# exit()
		self.mydriver=driver
		return self.stockdata , driver

	def monitoring(self,handlewin,return_login):

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

	
		# print("return login in monitoring pacsel.py line 239")
		# print(return_login)

		driver=handlewin

		bidvolumn={}
		bid={}
		offer={}
		offervolumn={}

		self.stockdata["updatedate"]= datetime.now().strftime("%Y-%m-%d")
		self.stockdata["timestamp"] = datetime.now().strftime("%H:%M:%S")

		# timerecord = timestamp.strftime('%Y-%m-%d %H:%M:%S')
		# print("time stamp=" + str(timestamp))
		
		# try:

		# find the stock value
		# stockname=driver.find_elements_by_xpath(self.xpathreturn("xstockname"))[0].text
		self.stockdata["stockvalue"] = driver.find_elements_by_xpath(self.xpathreturn("xstockvalue"))[0].text
		stockvalue=self.stockdata["stockvalue"]
		# print ("stock value now =" + stockvalue)	
		
		


		if (self.stockcompare=="0.00" and stockvalue !="0.00") or (self.stockcompare!=stockvalue) and (self.stockcompare!="0.00"):
			# print("first stockvalue updated=" + stockvalue)
			# print("first stockcompare updated=" + self.stockcompare)
			# self.mycollectqueues["qvalchange"].put({"stockvalue":stockvalue})
			PackSelModel.updatestockvaluechange(self.stockdata)
			
			# result_refreshbtn=self.refreshbtn(driver,"partial")

			self.mycollectqueues["qvalchange"].put({"stockvalue":stockvalue})
		
			self.mycollectqueues["qrefresh"].put({"qrefresh":"refreshdb",
												"refreshtype":"partial"}) # continue refresh TKInter
			self.stockcompare=stockvalue
			# print(self.stockdata)
		


			# result_refreshbtn=self.refreshbtn(driver)

		stockvalue=""	
		


		if not self.mycollectqueues["qrefresh"].empty(): 

			refreshparams = self.mycollectqueues["qrefresh"].get()
			# print ("Print refreshparams packsel.py line 291")
			# print(refreshparams)
			# print(refreshparams["refreshtype"])
			# # To continue re arrange below.
			if refreshparams["qrefresh"]=="refreshdb":
				if refreshparams["refreshtype"]=="all":
					print("+++++++++++Begin start to refresh all order")
					# result_refreshbtn,result_chkprocess =self.refreshbtn(driver,"all")
					result_refreshbtn =self.refreshbtn(driver,"all")

					print(result_refreshbtn)
					print(result_chkprocess)

				elif refreshparams["refreshtype"]=="partial":

					result_refreshbtn=self.refreshbtn(driver,"partial")

				# self.myplugins.checkparams(result_refreshbtn)	
				self.mycollectqueues["qrefresh"].put({"qrefresh":"refreshtk","doupdatetk":result_refreshbtn}) # continue refresh TKInter

			elif refreshparams["qrefresh"]=="refreshtk":
				self.mycollectqueues["qrefresh"].put(refreshparams)
			# # 	print (" ================= refresh result packsel.py line 303 ================= ")
			# # 	print (result_refreshbtn)

			# # 	# print ("put queue refreshtk packsel.py line 273")

			
		if not self.mycollectqueues["qorder"].empty(): 

			orderparams=self.mycollectqueues["qorder"].get()
			# if orderparams["order"]=="buy":
				# self.order(driver,orderparams)
			orderparams["driver"]=self.mydriver
			self.myplugins.order(orderparams,self.order)
				

	def order(self,orderparams):
		print (orderparams)
		# stockvalue = driver.find_elements_by_xpath(self.xpathreturn("xbuyradio"))[0].text
		print(self.mydriver)
		driver=self.mydriver
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
			print ("=========>>> confirm order to tkinter after order buy packsel.py line 366 ")
			result_refreshbtn=self.refreshbtn(driver,"partial") # with the update database 
			print("return result_refreshbtn by buy order packsel.py line 368")
			
			print(result_refreshbtn)
			# print(result_chkprocess)
			
		elif orderside=="sell":
			pass

		return result_refreshbtn
	def refreshbtn(self,driver,allorpartial="partial"):


		# try:
		print ("refresh botton press in function refresh btn packsel.py line 373")

		elem = driver.find_element_by_xpath(self.xpathreturn("xrtrefresh")).click()

		wait = WebDriverWait(driver, 30)
		WebElement = wait.until(EC.presence_of_element_located((By.XPATH, self.xpathreturn("xoutputderivordertable"))));

		time.sleep(0.5)

		# print("wait finished packsel.py line 372")
		doupdatetk=""
		if self.mode=="xlive":

			# !!!!! already work well !!!!!
			
			#############################################################################
			# special case with no work if put into above for xoutputordertable
			tablerow = driver.find_elements_by_xpath("/html/body/app-controller/div/ul/li[3]/order/div[2]/order-status/div/div/div/ul/*")
			#############################################################################

			mytable=[]

			if len(tablerow) > 2 : #default will include 2 blank line 

				for row in tablerow:
					# print ("total rows=" + str(len(roworder)))
					print ("row=" + row.text)
					if row.text:
						myrow=row.text.split(" ")
						
						mytable.append(myrow)

				# ['', '71911327', '14:42:59', 'WHA', 'B', '4.08', '700', '0', '0', '700', 'Cancel(X)', '', 'Detail', '']
				# [['71911327', '14:42:59', 'WHA', 'B', '4.08', '700', '0', '0', '700', 'Cancel(X)', 'Detail']]
				
				if allorpartial=="partial":
				# print ("partial update refresh packsel.py line 427")
					rowupdaterefresh=PackSelModel.updaterefresh(mytable,"partial")
				elif allorpartial=="all":
				# print("full update refresh packsel.py line 430")
					rowupdaterefresh=PackSelModel.updaterefresh(mytable,"all")					
				# print (mytable)
				# PackSelModel.updaterefresh(mytable)

				mytable=[]
				



				# col_dict=[]
			else:
				print("=========No found any row of order to record=========")
				rowupdaterefresh=""
			# already got this result
			# row=71906069 23:20:08 WHA B 4.18 500 0 0 0 Cancelled(CS) Detail
			# row=71906056 22:38:04 WHA B 4.16 500 0 0 0 Cancelled(CS) Detail

		elif self.mode=="xdebug":
			table_id = driver.find_element_by_xpath( self.xpathreturn("xoutputordertable"))
			tablerow = table_id.find_elements_by_xpath(".//tr")

			mytable=[]
			for row in tablerow:
				# print(row.text)
				if row.text:
					myrow = row.text.split(" ")
					myrow = myrow[2:]		
					mytable.append(myrow)

					# print(myrow)
			# print (mytable)
			#remove first element of array to be the same as xlive
			# ['', '71911327', '14:42:59', 'WHA', 'B', '4.08', '700', '0', '0', '700', 'Cancel(X)', '', 'Detail', '']
			# ['', '', '232558', '23:19:57', 'WHA', 'B', '0.00', '000', '0', '0', '0', 'Pending(S)']	
			# ['', '324276', '14:02:31', 'WHA', 'B', '4.90', '500', '0', '0', '0', 'Pending(S)']				
			# print ("=========================")
			# print(mytable)
			# print ("=========================")




			
			if allorpartial=="partial":
				# print ("partial update refresh packsel.py line 427")
				rowupdaterefresh=PackSelModel.updaterefresh(mytable,"partial")
			elif allorpartial=="all":
				# print("full update refresh packsel.py line 430")
				rowupdaterefresh=PackSelModel.updaterefresh(mytable,"all")	

			# print ("show update refresh packsel.py line 432")
				# print(rowupdaterefresh)
				# exit()
			mytable=[]
		rowupdaterefresh=self.myplugins.checkprocess2order(rowupdaterefresh)

		self.mycollectqueues["qrefresh"].put({"qrefresh":"refreshtk",
												"doupdatetk":rowupdaterefresh}) # continue refresh TKInter
			# print (rowupdaterefresh)
		# if result_chk	!="NOUPDATE" :
			# print("check result update !!!! packsel.py line 477")
			# print(result_chk)
			# rowupdaterefresh.append(result_chk) 

		return rowupdaterefresh
			# print("end for")
		# print("end of packsel.py")