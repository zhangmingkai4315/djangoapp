from __future__ import unicode_literals

from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class Question(models.Model):
	"""docstring for Question"""
	# def __init__(self, arg):
	# 	super(Question, self).__init__()
	# 	self.arg = arg
	question_text=models.CharField(max_length=200)
	pub_date=models.DateTimeField('data published')
	def __str__(self):
		return self.question_text
	def was_published_recently(self):
		now=timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'
	

class Choice(models.Model):
	"""docstring for Choice"""
	question=models.ForeignKey(Question,on_delete=models.CASCADE)
	choice_text=models.CharField(max_length=200)
	votes=models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text
