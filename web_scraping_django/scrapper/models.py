from pyexpat import model
from django.db import models

# Create your models here.


class Bilbasen_data(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    Phone = models.CharField(max_length=200)
    Fax = models.CharField(max_length=200)
    Number_of_listings = models.IntegerField()
    Web_Link = models.URLField(max_length=200)


class Biltorvet_data(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    zipAndCity = models.CharField(max_length=200)
    website = models.URLField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    adCount = models.IntegerField()
