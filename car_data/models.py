from __future__ import unicode_literals

from django.db import models

class Car_data_new(models.Model):
	car_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length = 100) # Name of the Car
	photolinks = models.TextField()
	videolinks = models.CharField(max_length=100)
	price = models.IntegerField() # its a charecter because its a range of values most commonly :)
	milege = models.CharField(max_length=10) # Vehicle Milege ** Seperatly Stored For Easy Acess
	body_type = models.CharField(max_length=20) #Sedan ,Suv ,Muv Etc ..
	specifications = models.TextField()
	general_information = models.TextField()
	dealer_number = models.IntegerField()
	dealer_email = models.CharField(max_length=100)
	hits = models.IntegerField() # Count Number of People Viewed this car
	date = models.DateTimeField() # Model Introduction Time

class Car_data_old(models.Model):
	user_id = models.IntegerField() #person posting the add
	car_id = models.AutoField(primary_key=True);
	brand = models.CharField(max_length=100)
	name = models.CharField(max_length = 100) # Name of the Car
	year = models.IntegerField(null=True)
	photolinks = models.FileField(upload_to = 'carsell/', default = 'carsell/nocar.jpg')
	videolink = models.CharField(max_length=100 , null=True)
	price = models.CharField(max_length = 50, null=True) # its a charecter because its a range of values most commonly :)
	features = models.TextField(null=True)
	fuel = models.CharField(max_length=10)
	transmission = models.CharField(max_length=10)
	reading = models.CharField(max_length=10)
	milege = models.CharField(max_length=10) # Vehicle Milege ** Seperatly Stored For Easy Acess
	body_type = models.CharField(max_length=20) #Sedan ,Suv ,Muv Etc ..
	general_information = models.TextField(null=True)
	Location = models.CharField(max_length = 200,null=True)
	hits = models.IntegerField(null=True) # Count Number of People Viewing Car 
	status = models.CharField(max_length=20,null=True) # sale means its not sold .. sold means its sold
	date = models.DateTimeField(null=True) # Added Date the sale gets auto sold after 30 days of inactivity
	confirmed = models.IntegerField() #Upon Confirming Data Confirmed Becomes 1

class Varient_data(models.Model):
	car_id = models.IntegerField()
	varient_id = models.AutoField(primary_key=True);
	name = models.CharField(max_length = 500)
	photolinks = models.TextField()
	videolink = models.CharField(max_length =100)
	main_car = models.CharField(max_length = 500)
	price = models.IntegerField()
	features = models.TextField()
	body_type = models.CharField(max_length=20) #Sedan ,Suv ,Muv Etc ..
	specifications = models.TextField()
	general_information = models.TextField()
	hits = models.IntegerField(null=True) # Count Number of People Viewing Car 


class Car_review(models.Model):
	car_id = models.IntegerField()
	car_type = models.CharField(max_length = 10)
	content = models.TextField()
	user_id = models.IntegerField()
	date = models.DateTimeField()

	