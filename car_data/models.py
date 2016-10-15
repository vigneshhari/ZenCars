from __future__ import unicode_literals

from django.db import models

class Car_data_new(models.Model):
	car_id = models.IntegerField()
	name = models.CharField(max_length = 100) # Name of the Car
	photolinks = models.CharField(max_length=1000)
	videolinks = models.CharField(max_length=100)
	price = models.CharField(max_length = 50) # its a charecter because its a range of values most commonly :)
	features = models.TextField()
	milege = models.CharField(max_length=10) # Vehicle Milege ** Seperatly Stored For Easy Acess
	Body_type = models.CharField(max_length=20) #Sedan ,Suv ,Muv Etc ..
	specifications = models.TextField()
	general_information = models.TextField()
	dealer_number = models.IntegerField()
	dealer_email = models.CharField(max_length=100)

class Car_data_old(models.Model):
	car_id = models.IntegerField()
	name = models.CharField(max_length = 100) # Name of the Car
	photolinks = models.CharField(max_length=1000)
	videolinks = models.CharField(max_length=100)
	price = models.CharField(max_length = 50) # its a charecter because its a range of values most commonly :)
	features = models.TextField()
	milege = models.CharField(max_length=10) # Vehicle Milege ** Seperatly Stored For Easy Acess
	Body_type = models.CharField(max_length=20) #Sedan ,Suv ,Muv Etc ..
	specifications = models.TextField()
	general_information = models.TextField()
	dealer_number = models.IntegerField()
	dealer_email = models.CharField(max_length=100)

class Varient_data(models.Model):
	car_id = models.IntegerField()
	varient_id = models.IntegerField()
	name = models.CharField(max_length = 500)
	price = models.IntegerField()
	features = models.TextField()
	milege = models.CharField(max_length=10) # Vehicle Milege ** Seperatly Stored For Easy Acess
	Body_type = models.CharField(max_length=20) #Sedan ,Suv ,Muv Etc ..
	specifications = models.TextField()
	general_information = models.TextField()

class Car_review(models.Model):
	car_id = models.IntegerField()
	content = models.TextField()
	user_id = models.IntegerField()
	user_name = models.CharField(max_length=500)
	date = models.DateTimeField()

	