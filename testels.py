
import django
import sys
import os
from django.utils import timezone
from datetime import datetime

sys.path.append('D:\workspace\anafin')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'anafin.settings')

django.setup()

from pinkybot.packsel_model import PackSelModel


timestamp = timezone.now()
timestampELS = timestamp.strftime('%Y-%m-%d %H:%M:%S')
stock="UTEST"
# timestamp= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# timestamp = timezone.utcnow()
timestamp = datetime.utcnow()
# timestampELS = timestamp.isoformat(' ','seconds')
timestampELS = timestamp.isoformat(' ','seconds')
print(timestampELS)
# timestampELS=2018-07-24T14:19:58Z
# exit()
bid={'bid1':1,'bid2':2,'bid3':4445,'bid4':4,'bid5':5}
offer={'offer1':6,'offer2':7,'offer3':8,'offer4':9,'offer10':10}
offervolumn={'offervolumn1':11,'offervolumn2':12,'offervolumn3':13,'offervolumn4':14,'offervolumn5':15}
bidvolumn={'bidvolumn1':12,'bidvolumn2':17,'bidvolumn3':18,'bidvolumn4':19,'bidvolumn5':20}

PackSelModel.InsertMonitorBidOffer(stock,timestampELS,bid,offer,bidvolumn,offervolumn)