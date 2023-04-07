from django.db import models

# Create your models here.
class hydrabad(models.Model):
    title=models.CharField(max_length=300)
    qualification=models.CharField(max_length=300)
    address=models.CharField(max_length=300)
    date=models.DateField()
    contact=models.BigIntegerField()

class goa(models.Model):
    title=models.CharField(max_length=300)
    qualification=models.CharField(max_length=300)
    address=models.CharField(max_length=300)
    date=models.DateField()
    contact=models.BigIntegerField()

class noida(models.Model):
    title=models.CharField(max_length=300)
    qualification=models.CharField(max_length=300)
    address=models.CharField(max_length=300)
    date=models.DateField()
    contact=models.BigIntegerField()

class meerut(models.Model):
    title=models.CharField(max_length=300)
    qualification=models.CharField(max_length=300)
    address=models.CharField(max_length=300)
    date=models.DateField()
    contact=models.BigIntegerField()