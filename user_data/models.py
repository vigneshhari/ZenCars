
from django.db import models

class User(models.Model):
	user_id = models.IntegerField()
	email = models.CharField(max_length = 500)
	name = models.CharField(max_length = 500)
	password = models.CharField(max_length = 500)
	phone_number = models.IntegerField()
	creationdate = models.DateTimeField()
	

