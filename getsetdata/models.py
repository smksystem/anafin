import django
from django.db import models
'''
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
'''
# from unittest.util import _MAX_LENGTH
# from MySQLdb.constants.ER import ALTER_OPERATION_NOT_SUPPORTED
class ComSetName(models.Model):
    comp_id = models.IntegerField(unique=True) 
    symbol = models.CharField(unique=True, max_length=10)
    fullname = models.TextField(blank=True, null=True)
    market = models.CharField(max_length=5)


class HLFinPeriodasof(models.Model):
    mastershare=models.CharField(max_length=50,unique=True,default="") # reference to table company name aav.year
    
    assets = models.FloatField(unique=False,default=0)
    liabilities = models.FloatField(unique=False)
    equity = models.FloatField(unique=False)
    paidcapital = models.FloatField(unique=False)
    revenue= models.FloatField(unique=False)
    netprofit = models.FloatField(unique=False)
    epsbath =  models.FloatField(unique=False)
    roa = models.FloatField(unique=False)
    roe = models.FloatField(unique=False)
    netprofitmargin = models.FloatField(unique=False)
    
class HLFinStatisticasof(models.Model):
    mastershare=models.CharField(max_length=50,unique=True,default="") # reference to table company name
    
    lastprice =models.FloatField(unique=False)
    marketcap=models.FloatField(unique=False)
    fsperiodasof=models.CharField(max_length=50,unique=False)
    p_e=models.FloatField(unique=False,default=0)
    p_bv=models.FloatField(unique=False,default=0)
    p_nav=models.FloatField(unique=False,default=0)
    nav=models.FloatField(unique=False,default=0)
    bookvaluepershare=models.FloatField(unique=False,default=0)
    dvdyield=models.FloatField(unique=False,default=0)
    
    
           
              