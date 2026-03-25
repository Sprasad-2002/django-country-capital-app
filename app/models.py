from django.db import models

# Create your models here.
class Country(models.Model):
    conid = models.IntegerField( primary_key=True)
    cname= models.CharField(unique=True)

class Capital(models.Model):
    conid=models.OneToOneField (Country,on_delete=models.CASCADE)
    capid=models.IntegerField(primary_key=True)
    capname=models.CharField(unique=True)
