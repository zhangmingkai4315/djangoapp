from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.views.generic import View
from .models import Tweet
from user_profile.models import User


# def index(request):
# 	if request.method == 'GET':
# 		return HttpResponse('I am called from a get request')
# 	elif request.method == 'POST':
# 		return HttpResponse('I am called from a post request')


class Index(View):
	def get(self,request):
		params={}
		params['name']='Mike'
		return render(request,'base.html',params)
	def post(self,request):
		return HttpResponse('I am called from a post request')

class Profile(View):
	def get(self,request,username):
		params=dict()
		user=User.objects.get(username=username)
		tweets=Tweet.objects.filter(user=user)
		params['tweets']=tweets
		params['user']=user
		return render(request,'profile.html',params)