import django
import sys
import os
	
sys.path.append('D:\workspace\anafin')	
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'anafin.settings')
django.setup()
	
from pinkybot.rangevalue import rangevalue		
from pinkybot.tkconsole import outputlog
from pinkybot.monitor import pinkybot
# print(__name__)
if __name__=="__main__":	
			
	# print("--- Welcome Main Pinkybot by MML ---") 
	console=outputlog()	
	console.Refresher()	
	console.mainloop()
	
	# console.attributes('-topmost', 'true') #### to make console on top level to other application.
	
	# work ok for hightlight	
	# for eachval,data in myrange.items():console.txtout("|"+eachval+" | Vol="+data["vol"] +  
	# # login= pinkybot()
 	# login.mypinkylogin(LoginParams)		
 
	# console.highlight_text("Vol")