	
''' setup django first to avoid AppRegistryNotReady 
'''
import django
import sys
import os

sys.path.append('D:\workspace\anafin')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'anafin.settings')

django.setup()



'''
this is main
'''
from getsetdata.rawdata_process import getrawdata


mytest= getrawdata()


# ####### the following line work#######
# /******
#    Use file or online  
# *******/
# mytest.loadAllComSet("online")
# exit()

# To debug per stock just fill in name of stock below function 
### TEST #######
# mytest.loadFinHighLight('TAPAC','file') ### to test

# exit()	
#######################################


allsymbole=mytest.getCompSet('all')

for symbole in allsymbole:
	mytest.loadFinHighLight(symbole,'file')
	
	



    
#mytest.InsertCompSet()
