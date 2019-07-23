from django.db import models
from datetime import datetime
# Create your models here.


class valuechange(models.Model):

	datefield=models.DateField(0)	
	timestamp = models.TimeField(0) 

	stockname=models.CharField(max_length=10)
	stockvalue=models.CharField(max_length=5,unique=False,default="")
	totalvolume=models.CharField(max_length=15,unique=False,default="")
	totalvolue=models.CharField(max_length=15,unique=False,default="")

	# to check if this value should send order to buy or sell.
	orderstate=models.CharField(max_length=10,unique=False,default="") 

class monitorbidoffer(models.Model):

	mastershare=models.CharField(max_length=50,unique=False,default="")
	timestamp = models.DateTimeField(0) 

	bid1 = models.FloatField(unique=False) 
	offer1 = models.FloatField(unique=False)
	bidvolumn1 = models.FloatField(unique=False)
	offervolumn1 = models.FloatField(unique=False)

	bid2 = models.FloatField(unique=False)
	offer2 = models.FloatField(unique=False)
	bidvolumn2 = models.FloatField(unique=False)
	offervolumn2 = models.FloatField(unique=False)

	bid3 = models.FloatField(unique=False)
	offer3 = models.FloatField(unique=False)
	bidvolumn3 = models.FloatField(unique=False)
	offervolumn3 = models.FloatField(unique=False)

	bid4 = models.FloatField(unique=False)
	offer4 = models.FloatField(unique=False)
	bidvolumn4 = models.FloatField(unique=False)
	offervolumn4 = models.FloatField(unique=False)

	bid5 = models.FloatField(unique=False)
	offer5 = models.FloatField(unique=False)
	bidvolumn5 = models.FloatField(unique=False)
	offervolumn5 = models.FloatField(unique=False)

class keeplogin(models.Model):

	profileId=models.CharField(max_length=15,unique=True,default="")
	brokeId=models.CharField(max_length=3,unique=False)
	loginId=models.CharField(max_length=10,unique=False,default="")
	passwordId=models.CharField(max_length=15,unique=False,default="")
	pinId=models.CharField(max_length=12,unique=False,default="")
	currentuseId=models.CharField(max_length=5,unique=False,default="")

class keepconfig(models.Model):

	# initinvest=20000
	# 	volumestep	=100
	# 	profitstep=1
	# 	topvaluerange=4.80
	# 	startvaluebuy=4.72
	# 	floorvaluerange=4.60
	# 	stopvaluerange=4.70
	# stockname=
	planname=models.CharField(max_length=30,unique=True,default="")
	rangeselect=models.CharField(max_length=5,unique=False,default="")
	monitorstock=models.CharField(max_length=10,unique=False,default="")
	initinvest=models.CharField(max_length=10,unique=False,default="")
	volumestep=models.CharField(max_length=5,unique=False,default="")
	profitstep=models.CharField(max_length=10,unique=False,default="")
	topvaluebuy=models.CharField(max_length=5,unique=False,default="")
	startvaluebuy=models.CharField(max_length=5,unique=False,default="")
	stopvaluebuy=models.CharField(max_length=5,unique=False,default="")
	floorvaluebuy=models.CharField(max_length=5,unique=False,default="")
	firstbuyflag=models.CharField(max_length=3,unique=False,default="YES")
	currentuseId=models.CharField(max_length=5,unique=False,default="")
	pluginfile=	models.CharField(max_length=30,unique=False,default="")
	runningmode=models.CharField(max_length=8,unique=False,default="auto")


# class buysellrecord(models.Model):
# 	orderno=models.CharField(max_length=10,unique=False,default="")
# 	side=models.CharField(max_length=10,unique=False,default="")


	 
class updaterefresh(models.Model):
	orderno=models.CharField(max_length=10,unique=False,default="")

	time=models.CharField(max_length=10,unique=False,default="")
	symbole=models.CharField(max_length=10,unique=False,default="")
	side=models.CharField(max_length=3,unique=False,default="")
	price=models.CharField(max_length=10,unique=False,default="")
	volume=models.CharField(max_length=10,unique=False,default="")
	matched=models.CharField(max_length=10,unique=False,default="")

	balance=models.CharField(max_length=10,unique=False,default="")
	cancelled=models.CharField(max_length=10,unique=False,default="")
	status=models.CharField(max_length=20,unique=False,default="")
	date=models.DateField(auto_now_add=True)
	matchedtime=models.CharField(max_length=20,unique=False,default="-")
	referorderno=models.CharField(max_length=15,unique=False,default="-")




