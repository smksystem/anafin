import django
import sys
import os

sys.path.append('D:\workspace\anafin')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'anafin.settings')
django.setup()

from pinkybot.rangevalue import rangevalue
from pinkybot.tkconsole import outputlog
from pinkybot.monitor import pinkybot

if __name__=="__main__":
	
	print("Welcome Main Pinkybot by MML") 

	# chooserange=rangevalue("C")
	# myrange=chooserange.getRangeSeries()
	console=outputlog("B")
	
	


	# work ok for hightlight
	# for eachval,data in myrange.items():console.txtout("|"+eachval+" | Vol="+data["vol"] +  
	# 													   " | Order=" +data["order"] + 
	# 													   " | State=" + data["state"]
	# 												)
	# # login= pinkybot()
 #    login.mypinkylogin(LoginParams)
 
	# console.highlight_text("Vol")
	# console.highlight_text("Order")
	# console.highlight_text("State")
	# console.highlight_text("7.05")


	console.Refresher()

	console.mainloop()