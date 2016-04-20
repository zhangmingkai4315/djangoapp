from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.contrib.auth.models import UserManager

class User(AbstractBaseUser,PermissionsMixin):
	username = models.CharField('username', max_length=10, unique=True, db_index=True)
	email=models.EmailField('email address',unique=True)
	joined=models.DateTimeField(auto_now_add=True)
	is_active=models.BooleanField(default=True)
	is_admin=models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	USERNAME_FIELD = 'username'
	objects=UserManager()
	REQUIRED_FIELDS = ['email']
	def get_short_name(self):
		return self.username
	def get_full_name(self):
		return self.username
	class Meta:
		db_table='user'
	def __unicode__(self):
		return self.username

class UserFollowers(models.Model):
	user=models.ForeignKey(User,unique=True)
	date=models.DateTimeField(auto_now_add=True)
	count=models.IntegerField(default=1)
	followers=models.ManyToManyField(User,related_name='followers')
	def __str__(self):
		return '%s, %s' % (self.user, self.count)