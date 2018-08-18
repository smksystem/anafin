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
	def __init__(self):
		pass
		

	def login(self,loginParams,myqueue):
		self.myqueue=myqueue
		# for i in iter(self.myqueue.get(),'STOP'):
			
		# for i in iter(self.myqueue):
		# print( self.myqueue.display())

		# print (self.myqueue.get())
		self.myqueue.put("monitoring")

		# for job in iter(self.myqueue.get, None):
			# print (job)
		
		exit()


		driver = webdriver.Chrome()
		# put url here
		# exit()
		driver.get("http://wen060.settrade.com/login.jsp?txtBrokerId="+loginParams["mybrokeId"])
		wait = WebDriverWait(driver, 10)
		element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/table[4]/tbody/tr/td[2]/table/tbody/tr[2]/td/table[1]/tbody/tr/td[2]/form/table/tbody/tr[3]/td[3]/font/input[2]")))

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


		myclick=driver.find_elements_by_xpath("//*[@id='trading']/table/tbody/tr[1]/td/a/img")[0]
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
		print(signin_window_handle)
		
		# wait until second pop up is complete loaded
		wait = WebDriverWait(driver, 30)
		element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='place-order-form']/refresh-ui-component/button/span[1]")))
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
		chkstock=driver.find_elements_by_xpath("//*[@id='favourite-"+fav_no+"']/ul/li[1]/editable-symbol-input/p")[0]
												# //*[@id="favourite-1"]/ul/li[1]/editable-symbol-input/p
		chkstock.click()
		stock = driver.find_elements_by_xpath("//*[@id='favourite-"+fav_no+"']/ul/li[1]/editable-symbol-input/p")[0].text
		print(stock)

		wait = WebDriverWait(driver, 10)
		elementClose = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='page-0-container']/li[3]/mini-quote/div[1]/mini-quote-overview/div[5]/label")))
		print("wait finished")
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
			# while True:
				# delta=datetime.utcnow()-timestamp
				# if delta.seconds >= 5:
				for line in range(1,6):
						test=driver.find_elements_by_xpath("//*[@id='bid-"+str(line)+"']")[0].text.replace(",","")
						print(test)
						bid["bid"+str(line)]=float(driver.find_elements_by_xpath("//*[@id='bid-"+str(line)+"']")[0].text.replace(",",""))
						offer["offer"+str(line)]=float(driver.find_elements_by_xpath("//*[@id='offer-"+str(line)+"']")[0].text.replace(",",""))
						bidvolumn["bidvolumn"+ str(line)]=float(driver.find_elements_by_xpath("//*[@id='bid-volume-"+str(line)+"']")[0].text.replace(",",""))
						offervolumn["offervolumn"+str(line)]=float(driver.find_elements_by_xpath("//*[@id='offer-volume-"+str(line)+"']")[0].text.replace(",",""))
				# timestamp = timezone.now()
				timestamp = datetime.utcnow()
				timestampELS = timestamp.isoformat(' ','seconds')
				print("Time record is =" + timestampELS)
				# exit()
				PackSelModel.InsertMonitorBidOffer(stock,timestampELS,bid,offer,bidvolumn,offervolumn)

				bidvolumn.clear()
				bid.clear()
				offer.clear()
				offervolumn.clear()

		except KeyboardInterrupt:
			pass
		# print("exit program")
		# exit()

