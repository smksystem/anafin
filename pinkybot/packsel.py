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


from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options 

# mydriver=0
class packselenium(PackSelModel):
	"""docstring for packselenium"""
	def __init__(self,mode):
		self.starttime=time.time()
		self.mode=mode
		self.log["applog"].info('Running Mode = '+mode)
		super().__init__() # configure xdebug or xlive
		# print ("running mode=" + mode)

	def putconfigval(self,configval):
		self.configval=configval

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
				"xsellradio":"//*[@id='placeEq']/div[1]/input[2]", 

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
				"xsellradio":"//*[@id='sell-btn']",

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




###################### Head Less Chrome ##################
		# chrome_options = Options()  
		# chrome_options.add_argument("--headless")  
		# driver = webdriver.Chrome(chrome_options=chrome_options)

###################### Head Show ##########################
		driver = webdriver.Chrome()

##################### Firefox #############################
		# # cap = DesiredCapabilities().FIREFOX
		# # cap["marionette"] = False

		# # binary = FirefoxBinary(r'C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe')
		# driver = webdriver.Firefox(capabilities=cap,firefox_binary=binary)
#############################################################
		# put url here
		# exit()

		if self.mode=="xdebug":
			driver.get("http://localhost:8000/dummy/")
		elif self.mode=="xlive":
			driver.get("http://wen060.settrade.com/login.jsp?txtBrokerId="+loginParams["brokeId"])





		wait = WebDriverWait(driver, 10)

		# element = wait.until(EC.presence_of_element_located((By.XPATH, "")))

		element = wait.until(EC.presence_of_element_located((By.XPATH, self.xpathreturn("xpathlogin"))))


		print("super selenium class is called")
		driver.maximize_window()

		elem = driver.find_element_by_name("txtLogin")
		elem.clear()
		# put user in key
		elem.send_keys(loginParams["loginId"]) 

		elem = driver.find_element_by_name("txtPassword")
		elem.clear()
		# put password in key
		elem.send_keys(loginParams["passwordId"])

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

		self.log["applog"].debug("Web load success")

		# stock = driver.find_elements_by_xpath("//*[@id='favourite-0']/ul/li[1]/editable-symbol-input/p")[0].text

		stock = driver.find_elements_by_xpath(self.xpathreturn("xstockname"))[0]
		
		# print ("stock is below found check login")
		if self.mode=="xdebug":
			stockname=stock.get_attribute('value')
		elif self.mode=="xlive":
			stockname=stock.text
		
		# self.log["applog"].debug("debug: packsel.py line 203 def login ")
		# print ("stockname found is " + stockname)
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

		if (stockname):
			print("enter to if confirm login packsel.py line 223 def login !!!!!!!!!!")
			# pr3int (element)
			self.mycollectqueues["qvalchange"].put({"textout":"Login success contiue monitoring : " + stockname,
				"stockname":stockname,
				})
			self.stockcompare="0.00"
		# print(self.stockdata)
		# exit()
		self.mydriver=driver
		return self.stockdata , driver


############################################################
# Main def to monitor infinity loop
############################################################
	def monitoring(self,handlewin,return_login):


		driver=handlewin

		bidvolumn={}
		bid={}
		offer={}
		offervolumn={}

		self.stockdata["updatedate"]= datetime.now().strftime("%Y-%m-%d")
		self.stockdata["timestamp"] = datetime.now().strftime("%H:%M:%S")
		self.currenttime=time.time()


		# print(self.stockdata["timestamp"])

		# timerecord = timestamp.strftime('%Y-%m-%d %H:%M:%S')
		# print("time stamp=" + str(timestamp))
		
		# try:

		# find the stock value
		# stockname=driver.find_elements_by_xpath(self.xpathreturn("xstockname"))[0].text
		self.stockdata["stockvalue"] = driver.find_elements_by_xpath(self.xpathreturn("xstockvalue"))[0].text
		stockvalue=self.stockdata["stockvalue"]
		# print ("stock value now =" + stockvalue)	

#########################///////////////////////////////
######################### Time out check use 
######################### when there's no change value 
######################### and clikc refresh every 3 seconds.
#########################/////////////////////////////// 
		# print("time elapse now packsel.py line 281 def monitoring " )
		# # print(self.currenttime-self.starttime)


		# if not self.mycollectqueues["qtimerefresh"].empty(): 		
		# 	refreshtime = self.mycollectqueues["qtimerefresh"].get()			
		# 	print("refresh time packsel.py line 284 def monitoring")



			# if refreshtime=="refresh":
			# 	resultvaluechange=self.refreshbtn(driver,"partial")
				
		# elapsedtime=(self.currenttime - self.starttime)
		# if elapsedtime >= 3 :

		# 	print("refresh time more than 3 seconds packsel.py line 281 def monitoring")
			
		# 	self.starttime=time.time()
		# 	print(self.stockdata["timestamp"])

#########################/////////////////////////////// 
#########################  Value Change ////////////////
#########################///////////////////////////////
	


		if (self.stockcompare=="0.00" and stockvalue !="0.00") or (self.stockcompare!=stockvalue) and (self.stockcompare!="0.00"):


			self.log["applog"].debug("Print configvalue")
			self.log["applog"].debug("StartValuebuy")
			# self.log["applog"].debug(self.configval)
			self.log["applog"].debug(self.configval["startvaluebuy"].get())

			flstartvaluebuy=float(self.configval["startvaluebuy"].get())
			flcommonvaluestep=float(self.configval["commonvaluestep"].get())
			flstockvalue=float(stockvalue)

			if flstockvalue<flstartvaluebuy :
				self.log["applog"].debug("found value less than stockvalue")
				self.log["applog"].debug(stockvalue)

				self.log["applog"].debug("Common Value Step")
				self.log["applog"].debug(str(flcommonvaluestep))
				self.myplugins.checkdownsidebuy(flstockvalue,flstartvaluebuy)

			# print("first stockvalue updated=" + stockvalue)
			# print("first stockcompare updated=" + self.stockcompare)
			# self.mycollectqueues["qvalchange"].put({"stockvalue":stockvalue})
			# if stockvalue =="0.00":

			#########################################################
			############ Check time refresh every 3 seconds.
			#########################################################

			# if not self.mycollectqueues["qtimerefresh"].empty(): 
			# 	timechkstart = self.mycollectqueues["qtimerefresh"].get()
			# 	if timechkstart["command"]!="monitoring":
			# 		self.mycollectqueues["qtimerefresh"].put({"command":"starttime"}) 
			# 	else:
			# 		self.mycollectqueues["qtimerefresh"].put(timechkstart) 

			##########################################################


			PackSelModel.updatestockvaluechange(self.stockdata)
			# print("\nstart to refersh partial from packsel.py line 315 def monitoring")
			resultvaluechange=self.refreshbtn(driver,"partial")
			# print("\nstart to check process to order packsel.py line 317 def monitoring")
			
			resultvaluemonitor=self.myplugins.checkprocess2order(resultvaluechange,stockvalue,self.order)
			self.log["applog"].debug("*** result from value of resultvaluemonitor def monitoring")
			self.log["applog"].debug(resultvaluemonitor)


			# To send to tkconsole.py update status of value change.			# continue refresh TKInter
			self.mycollectqueues["qvalchange"].put({"stockvalue":stockvalue})   # to send blink at value.
			# self.mycollectqueues["qrefresh"].put({"qrefresh":"refreshdb",
												# "refreshtype":"all"}) 

			# self.mycollectqueues["qtimerefresh"].put({"command":"monitoring"})			

			##################################################################################
			# Do check order base on  value
			##################################################################################

			self.stockcompare=stockvalue
			# print(self.stockdata)
			# starttime=self.stockdata["timestamp"]		
			# self.resettime=0

			# result_refreshbtn=self.refreshbtn(driver)

		stockvalue=""	
		


		if not self.mycollectqueues["qrefresh"].empty(): 

			refreshparams = self.mycollectqueues["qrefresh"].get()
			self.log["applog"].debug("Qrefresh is not empty")
			self.log["applog"].debug(refreshparams)
			# print ("Print refreshparams packsel.py line 291")
			# print(refreshparams)
			# print(refreshparams["refreshtype"])
			# # To continue re arrange below.
			if refreshparams["qrefresh"]=="refreshdb":
				if refreshparams["refreshtype"]=="all":
					# print("+++++++++++Begin start to refresh all order")
					# result_refreshbtn,result_chkprocess =self.refreshbtn(driver,"all")
					result_refreshbtn =self.refreshbtn(driver,"all")

					# print(result_refreshbtn)
					# print(result_chkprocess)

				elif refreshparams["refreshtype"]=="partial":

					result_refreshbtn=self.refreshbtn(driver,"partial")
					self.log["applog"].debug ("\n--- Partial refresh result from refreshbtn packsel.py line 363 def monitoring")
					self.log["applog"].debug(result_refreshbtn)
				
				resultMatch =self.myplugins.checkprocess2matchstatus(result_refreshbtn,self.order)


				

				# print("\n+++ result after checkprocess2matchstatus in plugin_fivesteps.py line 367 packsel.py def refreshbtn")
				# print(resultMatch)
				# if resultMatch!=None:
					# for eachMatch in resultMatch:

							# print("\nresultMatch output from checkprocess2matchstatus def monitoring")
							# print (eachMatch)

							# result_refreshbtn=resultMatch


						# for myMatch in eachMatch:
							# if myMatch["status"]=="Matched(M)" and myMatch["orderno"]== resultMatch["orderno"]:
								# myMatch["matchedtime"]=resultMatch["matchedtime"]
								# elif myMatch["status"]!="Matched(M)" :
								# 	pass
								# 	result_refreshbtn["referorderfrom"]=resultMatch["referorderfrom"]


						# 	for chkmatch in resultMatch: ### return as arry with dictionary.
						# 		if chkmatch["status"]=="Matched(M)":
						# 			print("Found match status packsel.py line 368")
									
						# 	### update resultmatch to result_refreshbtn to tkinter here ( profit target ...etc)

						# self.myplugins.checkparams(result_refreshbtn)	



				print("\n+++ Check result match status packsel.py line 376 in def monitoring")
				print (result_refreshbtn)


				# if resultMatch != None and result_refreshbtn!=None :
					# result_refreshbtn["matchedtime"]=resultMatch["matchedtime"]



				# self.mycollectqueues["qrefresh"].put({"qrefresh":"refreshtk","doupdatetk":result_refreshbtn}) # continue refresh TKInter

			elif refreshparams["qrefresh"]=="refreshtk":
				self.mycollectqueues["qrefresh"].put(refreshparams)
			# # 	print (" ================= refresh result packsel.py line 303 ================= ")
			# # 	print (result_refreshbtn)

			# # 	# print ("put queue refreshtk packsel.py line 273")

			
		# if not self.mycollectqueues["qorder"].empty(): 

		# 	orderparams=self.mycollectqueues["qorder"].get()
		# 	print("\ngot order to buy from qorder queue packsel.py line 384 def monitoring")
		# 	self.myplugins.order(orderparams,self.order)
		
		# self.mycollectqueues["qtimerefresh"].put({"command":"monitoring"})			
		
				

	def order(self,orderparams):
		self.log["applog"].debug("Order params def order")
		self.log["applog"].debug(orderparams)
		# stockvalue = driver.find_elements_by_xpath(self.xpathreturn("xbuyradio"))[0].text
		# print(self.mydriver)
		driver=self.mydriver
		orderside=orderparams["order"]
		# orderparams["stockpin"]=self.mypin

		if orderside=="buy":

			chkstock=driver.find_elements_by_xpath(self.xpathreturn("xbuyradio"))[0].click()

		elif orderside=="sell":

			chkstock=driver.find_elements_by_xpath(self.xpathreturn("xsellradio"))[0].click()

		elem = driver.find_element_by_xpath(self.xpathreturn("xstockorder"))
		elem.clear()
		# put user in key
		elem.send_keys(orderparams["monitorstock"]) 

		elem = driver.find_element_by_xpath(self.xpathreturn("xstockvolumnorder"))
		elem.clear()
		# put user in key
		elem.send_keys(orderparams["volume"]) 

		elem = driver.find_element_by_xpath(self.xpathreturn("xstockvalueorder"))
		elem.clear()
		# put user in key
		elem.send_keys(orderparams["price"]) 

		elem = driver.find_element_by_xpath(self.xpathreturn("xstockpinorder"))
		elem.clear()
		# put user in key
		elem.send_keys(orderparams["stockpin"]) 

		elem = driver.find_element_by_xpath(self.xpathreturn("xstocksubmitorder")).click()

		if self.mode=="xlive":

			elem = driver.find_element_by_xpath(self.xpathreturn("xstockconfirmorder")).click()				

		elif self.mode=="xdebug":
			elem = driver.switch_to_alert().accept()


		if "referorderno" in orderparams:

			result_refreshbtn=self.refreshbtn(driver,"partial",orderparams["referorderno"]) # with the update database 
		else:

			result_refreshbtn=self.refreshbtn(driver,"partial") # with the update database 



		print("\nreturn result_refreshbtn order packsel.py line 368 def order")
		print(result_refreshbtn)

		return result_refreshbtn

	def refreshbtn(self,driver,allorpartial="partial",*params_referorderno):

		chkreferorderno="None"
		# print("Number of params_referorderno is below packsel.py line 492 in def refreshbtn")
		# print(len(params_referorderno))


		if len(params_referorderno) != 0 : 
				# print("\nRefer order no is sent in refreshbtn packsel.py line 488")
				# print(params_referorderno)
				# print(params_referorderno[0])

				chkreferorderno=params_referorderno[0]
				# chkreferorderno=referorderno


		# try:
		# print ("\nrefresh botton press in function refresh btn packsel.py line 406 in def refreshbtn")

		elem = driver.find_element_by_xpath(self.xpathreturn("xrtrefresh")).click()

		wait = WebDriverWait(driver, 10)
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

			if len(tablerow) > 2 : # default will include 2 blank line 

				for row in tablerow:
					# print ("total rows=" + str(len(roworder)))
					print ("row=" + row.text)
					if row.text:
						myrow=row.text.split(" ")
						
						mytable.append(myrow)

				# ['', '71911327', '14:42:59', 'WHA', 'B', '4.08', '700', '0', '0', '700', 'Cancel(X)', '', 'Detail', '']
				# [['71911327', '14:42:59', 'WHA', 'B', '4.08', '700', '0', '0', '700', 'Cancel(X)', 'Detail']]

				print("\n--- update refresh to mytable packsel.py line 495 def refreshbtn ")
				print(mytable)



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


			# //*[@id="orderBodyEq"]/tbody/tr[1]
			# //*[@id="orderBodyEq"]/tbody/tr[2]
			# //*[@id="orderBodyEq"]/tbody/tr[12]

			mytable=[]
			realtable={}
			self.log["applog"].debug("Print tablerow before loop")
			# self.log["applog"].debug(tablerow) print raw selenium output
			# exit()
			# return None
			for row in tablerow:
				# self.log["applog"].debug(row.text)
				self.log["applog"].debug(row.get_attribute('innerText'))

				if row.get_attribute('innerText'):
					myrow = row.get_attribute('innerText').split("\t")
					self.log["applog"].debug("output from split with space")
					self.log["applog"].debug(myrow)
					myrow = myrow[1:]		
					realtable[myrow[0]]={
								"time":myrow[1],
								"stockname":myrow[2],
								"orderside":myrow[3],
								"price":myrow[4],
								"volume":myrow[5],
								"matched":myrow[6],
								"balance":myrow[7], 
								"cancelled":myrow[8],
								"status":myrow[9],

								}
					self.log["applog"].debug("new real table to be format")
					self.log["applog"].debug(realtable)
					mytable.append(myrow)
			# self.log["applog"].info("Number rows of Table Track = " + str(len(tablerow)))
			# self.log["applog"].debug(realtable["998158"]["status"])
			# for testing purpose....
			# for tr_id in range(len(tablerow)):
			# 	trout = driver.find_element_by_xpath("//*[@id='orderBodyEq']/tbody/tr["+str(tr_id+1)+"]/td[11]")
			# 	self.log["applog"].debug("Test print trid no " + str(tr_id+1))
			# 	self.log["applog"].debug(trout.get_attribute('innerText'))
				
			# for ele_trid in tr_id:
			# 	self.log["applog"].debug(ele_trid.text)
			# tr_row=table_id

			#remove first element of array to be the same as xlive
			# ['', '71911327', '14:42:59', 'WHA', 'B', '4.08', '700', '0', '0', '700', 'Cancel(X)', '', 'Detail', '']
			# ['', '', '232558', '23:19:57', 'WHA', 'B', '0.00', '000', '0', '0', '0', 'Pending(S)']	
			# ['', '324276', '14:02:31', 'WHA', 'B', '4.90', '500', '0', '0', '0', 'Pending(S)']				
			# print ("=========================")
			# print(mytable)
			# print ("=========================")

			self.log["applog"].debug("raw data for mytable before update to database in def refreshbtn")
			self.log["applog"].debug(mytable)			
			# exit()

			# if chkreferorderno != None:
				# mytable.append({"referorderno":chkreferorderno})
				# chkreferorderno=None

			if allorpartial=="partial":
				# print ("partial update refresh packsel.py line 427")
				rowupdaterefresh=self.updaterefresh(mytable,"partial",chkreferorderno)
				self.log["applog"].debug("Do partial update refresh with below data in var mytable")
				self.log["applog"].debug(rowupdaterefresh)

			elif allorpartial=="all":
				###### In case of restart, will retrieve all data from database include putordermonitoring

				# rowupdaterefresh,notmatchmonitoring=self.updaterefresh(mytable,"all")	
				rowupdaterefresh=self.updaterefresh(mytable,"all")	
				self.log["applog"].debug("Do ALL full update refresh ALL before putordermonitoring")
				self.log["applog"].debug(rowupdaterefresh)
				self.myplugins.putordermonitoring(rowupdaterefresh)
				
				# self.log["applog"].debug("Print monitoring not match in var notmatchmonitoring")
				# self.log["applog"].debug(notmatchmonitoring)
				
			mytable=[]

		# this is ok to work like this check process nad then send to update data
		# rowupdaterefresh=self.myplugins.checkprocess2matchstatus(rowupdaterefresh)
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