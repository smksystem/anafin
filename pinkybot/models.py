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

class udpatestockvalue(models.Model):
	
	valuefield=models.CharField(max_length=10,unique=False,default="")
	datefield=models.DateTimeField(0)
	timefield=models.DateTimeField(0)
	orderfield=models.CharField(max_length=5,unique=False,default="")
	statusfield=models.CharField(max_length=20,unique=False,default="")
	volumnfield=models.CharField(max_length=10,unique=False,default="")
	buyfield=models.CharField(max_length=5,unique=False,default="")
	sellfield=models.CharField(max_length=5,unique=False,default="")
	cancelfield=models.CharField(max_length=5,unique=False,default="")
	targetvalue=models.CharField(max_length=10,unique=False,default="")
	profitfield=models.CharField(max_length=10,unique=False,default="")
	 
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