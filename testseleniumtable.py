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



	elem = driver.find_element_by_xpath(xrtrefresh).click()

	# wait until data arrive
	wait = WebDriverWait(driver, 30)
	WebElement = wait.until(EC.invisibility_of_element_located((By.ID, 'ajax_loader')));

	time.sleep(0.5)

	# wait = WebDriverWait(driver, 30)
	# WebElement = wait.until(EC.visibility_of_element_located((By.XPATH, xoutputordertable)));
	# elementClose = wait.until(EC.presence_of_element_located((By.XPATH, xoutputordertable)))
	# print (elementClose.text)
	print("wait finished")


	# get all table list here


	table_id = driver.find_element_by_xpath(xoutputordertable)
	# print (table_id.text)
	# exit()
	for row in table_id.find_elements_by_xpath(".//tr"):
		# print (row)
		# print (row.text)

		for col in row.find_elements_by_xpath(".//td"):
			# //*[@id="orderBodyEq"]/tbody/tr[1]/td[4]
			print (col.text)



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

	xtabletest="//*[@id='orderBodyEq']"



	driver = webdriver.Chrome()
	driver.get("http://localhost:8000/dummyrt/")



	wait = WebDriverWait(driver, 20)
	elementClose = wait.until(EC.presence_of_element_located((By.XPATH, xoutputordertable)))


	print ( "finish wait")



	# while 1:
	refreshbtn(driver)

	time.sleep(5)

	refreshbtn(driver)

	time.sleep(5)

	refreshbtn(driver)

	time.sleep(5)

	refreshbtn(driver)

	time.sleep(5)

	refreshbtn(driver)

