from django.db import models

# Create your models here.
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
	datetime=models.DateTimeField()
	stockvalue=models.CharField(max_length=50,unique=False,default="")
	 