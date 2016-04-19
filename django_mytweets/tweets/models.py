from __future__ import unicode_literals

from django.db import models

# Create your models here.
from user_profile.models import User

class Tweet(models.Model):
	user=models.ForeignKey(User)
	text=models.CharField(max_length=160)
	created_date=models.DateTimeField(auto_now_add=True)
	country=models.CharField(max_length=30)
	is_active=models.BooleanField(default=True)
	def __unicode__(self):
		return self.text
