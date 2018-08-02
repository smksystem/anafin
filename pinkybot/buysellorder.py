from pinkybot.packsel import packselenium
import sys
class buysellorder(packselenium):

	def orderbuy(handlewin):
		print("buysell")
		driver=handlewin
		clickbuy=driver.find_elements_by_xpath("//*[@id='buy-btn']")[0]
		clickbuy.click()


		buystock = driver.find_elements_by_xpath("//*[@id='place-order-symbol']/auto-complete/div/input[2]")[0]
		buystock.clear()

		# put user in key
		buystock.send_keys("BEAUTY") 


		buyvol = driver.find_elements_by_xpath("//*[@id='place-order-volume']/div/volume-input/input")[0]
		buyvol.clear()

		# put user in key
		buyvol.send_keys("100") 


		buyprice = driver.find_elements_by_xpath("//*[@id='place-order-price']/div/price-input/input")[0]
		buyprice.clear()

		# put user in key
		buyprice.send_keys("7.00") 
		buypin = driver.find_elements_by_xpath("//*[@id='place-order-pin']/div/input")[0]
		buypin.clear()

		# put user in key
		# text=input("prompt_pin")
		buypin.send_keys("") 		

		buysubmit = driver.find_elements_by_xpath("//*[@id='place-order-submit']/span")[0]
		
		buysubmit.click()
 	


		submitconfirm=driver.find_elements_by_xpath("/html/body/modal-layer/div/div/div/form/div[2]/div[1]/button")[0]
		submitconfirm.click()





		# main_window_handle = None
		# while not main_window_handle:
		# 	main_window_handle = driver.current_window_handle
		
		# confirm_buy_window_handle = None
		# while not confirm_buy_window_handle:
		# 	for handle in driver.window_handles:
		# 		print (handle)
		# 		if handle != main_window_handle:
		# 			confirm_buy_window_handle = handle
		# 			break
		# driver.switch_to.window(confirm_buy_window_handle)
		# print(confirm_buy_window_handle)









		# stock = driver.find_elements_by_xpath("//*[@id="place-order-symbol"]/auto-complete/div/input[2]")[0].text
		# print(stock)
		while 1:
			pass
	def ordersell(handlewin):
		pass
		