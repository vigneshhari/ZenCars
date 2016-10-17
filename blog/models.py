from __future__ import unicode_literals

from django.db import models

# Create your models here.
class content(models.Model):
	blog_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length = 500)
	category = models.CharField(max_length = 100)
	photo = models.TextField()
	author = models.CharField(max_length = 50)
	date = models.DateTimeField()

class comment(models.Model):
	blog_id = models.IntegerField()
	user_id = models.IntegerField()
	content = models.TextField()
	date = models.DateTimeField()