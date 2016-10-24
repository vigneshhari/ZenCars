
from django.db import models

class User_Account(models.Model):
	user_id = models.IntegerField()
	name = models.CharField(max_length = 500)
	password = models.CharField(max_length = 100)
	email = models.CharField(max_length = 100)
	photo = models.FileField(upload_to = 'auth/user', default = 'carsell/nouser.jpg')
	phone_no = models.IntegerField()
	vericode = models.CharField(max_length = 100)
	verified = models.IntegerField()
	

