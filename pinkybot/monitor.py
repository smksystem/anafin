# this is monitoring buy  sell 

from pinkybot.packsel import packselenium
from pinkybot.buysellorder import buysellorder
class pinkybot(packselenium):
	"""docstring for firstlogin"""
	def __init__(self):
		pass


		




	def mypinkylogin(self,loginParams):
		# self.monitoring("test")
		# print (username)
		print (loginParams)
		# exit()

		handlewin=self.login(loginParams)
		buysellorder.orderbuy(handlewin)
		

		# test here to pass thrue the handlewin


		exit()
		# handlewin="test"
		print("login is called")
		self.monitoring(handlewin)
