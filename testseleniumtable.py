from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC   
from selenium.webdriver.common.by import By
import datetime as dt
from django.utils import timezone
from datetime import datetime
import time 






def refreshbtn(driver):


	try:
		elem = driver.find_element_by_xpath(xrtrefresh).click()

	except:
		pass

	# wait until data arrive
	wait = WebDriverWait(driver, 30)
	# WebElement = wait.until(EC.invisibility_of_element_located((By.ID, 'ajax_loader')));


	# wait = WebDriverWait(driver, 30)
	try:
		WebElement = wait.until(EC.presence_of_element_located((By.XPATH, xoutputderivordertable)));

	# elementClose = wait.until(EC.presence_of_element_located((By.XPATH, xoutputordertable)))
	# print (elementClose.text)
	except:
		pass

	time.sleep(0.5)

	print("wait finished")


	# get all table list here

	# try:
 #    	WebElement date = driver.findElement(By.linkText(Utility.getSheetData(path, 7, 1, 2)));
 #    date.click();
	# }
	# catch(org.openqa.selenium.StaleElementReferenceException ex)
	# {
 #    	WebElement date = driver.findElement(By.linkText(Utility.getSheetData(path, 7, 1, 2)));
 #    	date.click();
	# }
	try:
		table_id = driver.find_element_by_xpath(xoutputordertable)
		# result = True
		# break
	except:
		pass

	
	# print (table_id.text)
	# exit()
	try:
		tablerow=table_id.find_elements_by_xpath(".//tr")
	except:
		pass

		# print (row)
		# print (row.text)
	try:

		for row in tablerow:

			tablecollume=row.find_elements_by_xpath(".//td")
			# print ("len of colume is" + str(len(tablecollume)))
			# print (tablecollume)
			# if len(tablecollume) > 0:
			for col in tablecollume:
				# //*[@id="orderBodyEq"]/tbody/tr[1]/td[4]
				# if col.text != "":
				print (col.text)

	except:
		pass				
		



# print("load table finish")


if __name__=="__main__":
# "xpathvaluemonitor":"//*[@id='instInfoEq']/tbody/tr[1]/td[2]/h2/span",
	xpathlogin= "/html/body/table[4]/tbody/tr/td[2]/table/tbody/tr[2]/td/table[1]/tbody/tr/td[2]/form/table/tbody/tr[3]/td[3]/font/input[2]"
	xpathrealtime="//*[@id='trading']/table/tbody/tr[1]/td/a/img"
	xrtrefresh="//*[@id='order_ctrl']/input[3]"
	xfavorchk="//*[@id='favourite-0']/ul/li[1]"
	xstockup="//*[@id='instInfoEq']/tbody/tr[1]/td[2]/h2/span"
	xstockname="//*[@id='eqQuoteSymbol']"
	xstockvalue="//*[@id='instInfoEq']/tbody/tr[1]/td[2]/h2/span"
	xbuyradio="//*[@id='placeEq']/div[1]/input[1]"
	xstockorder="//*[@id='eqSymbol']"
	xstockvolumnorder="//*[@id='placeEq']/div[2]/input"
	xstockvalueorder="//*[@id='placeEq']/div[3]/input[1]"
	xstockpinorder="//*[@id='placeEq']/div[3]/span/input"
	xstocksubmitorder="//*[@id='placeEq']/div[4]/input[1]"
	xoutputordertable="//*[@id='orderBodyEq']"
	xoutputderivordertable="//*[@id='orderDeriv']"
	xtabletest="//*[@id='orderBodyEq']"



	driver = webdriver.Chrome()
	driver.get("http://localhost:8000/dummyrt/")



	wait = WebDriverWait(driver, 20)
	elementClose = wait.until(EC.presence_of_element_located((By.XPATH, xoutputordertable)))


	print ( "finish wait")



	while 1:
		refreshbtn(driver)

		# time.sleep(1)

	# refreshbtn(driver)

	# time.sleep(5)

	# refreshbtn(driver)

	# time.sleep(5)

	# refreshbtn(driver)

	# time.sleep(5)

	# refreshbtn(driver)

