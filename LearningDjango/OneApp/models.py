from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Person(models.Model):
    """
    Description: Model Description
    """
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    SHIRT_SIZES=(
    	('s','Small'),
    	('m','Medium'),
    	('l','Large')
    	)
    shirt_size=models.CharField(max_length=1,choices=SHIRT_SIZES,default='s')
    
class Manufacturer(models.Model):
	pass

class Car(models.Model):
	manufacturer=models.ForeignKey(Manufacturer,on_delete=models.CASCADE)

class Reporter(models.Model):
	name=models.CharField(max_length=120)
	email=models.EmailField()
	def __str__(self):
		return '%s %s' %(self.name,self.email)

class Article(models.Model):
	headline=models.CharField(max_length=100)
	pub_date=models.DateField()
	reporter=models.ForeignKey(Reporter,on_delete=models.CASCADE)
	def __str__(self):
		return self.headline
	class Meta:
		ordering=('headline',)