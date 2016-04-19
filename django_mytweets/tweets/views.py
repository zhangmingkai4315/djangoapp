from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.views.generic import View

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