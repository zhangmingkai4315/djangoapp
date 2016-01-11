from __future__ import unicode_literals

from django.db import models
import datetime
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
		return self.pub_date>=timezone.now()-datetime.timedelta(days=1)

class Choice(models.Model):
	"""docstring for Choice"""
	question=models.ForeignKey(Question,on_delete=models.CASCADE)
	choice_text=models.CharField(max_length=200)
	votes=models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text


		
