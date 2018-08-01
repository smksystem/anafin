from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
# put url here
driver.get("")

assert "CLICK2WIN" in driver.title
elem = driver.find_element_by_name("txtLogin")
elem.clear()
# put user in key
elem.send_keys("") 

elem = driver.find_element_by_name("txtPassword")
elem.clear()
# put password in key
elem.send_keys("")

elem.send_keys(Keys.RETURN)

memberid=driver.find_elements_by_xpath("/html/body/div[2]/h1")[0].text
print ("memberid=" + memberid)
if memberid=='7399347':
	print("detect found memberid")
	python_button = driver.find_elements_by_xpath("/html/body/div[3]/form/button")[0]
	python_button.click()

	python_stream = driver.find_elements_by_xpath("//*[@id='sidebar-wrapper']/div/div/div/div/ul/li[1]/div/a/div")[0]
	python_stream.click()
# /html/body/div[3]/form/button
# /html/body/div[3]/form/button

assert "No results found." not in driver.page_source
# driver.close()

