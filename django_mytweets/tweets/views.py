from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect

from django.views.generic import View
from .models import Tweet,HashTag
from user_profile.models import User

from .forms import TweetForm,SearchForm

from  django.template import Context
from django.template.loader import render_to_string,get_template
import json
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
		params['form']=TweetForm()
		return render(request,'profile.html',params)


# class PostTweet(View):
# 	def post(self,request,username):
# 		form=TweetForm(request.POST)
# 		user=User.objects.get(username)
# 		if form.is_valid():
# 			tweet=Tweet(text=form.cleaned_data['text'])
# 			user=user
# 			# country=form.cleaned_data['country']
# 			tweet.save()
# 			words=form.cleaned_data['text'].split(' ')
# 			for word in words:
# 				if word[0] == '#':
# 					hashtag,created=HashTag.objects.get_or_create(name=word[1:])
# 					hashtag.tweet.add(tweet)
			
# 		return HttpResponseRedirect('/user/'+username)



class PostTweet(View):
	def post(self, request, username):
	 	form = TweetForm(request.POST)
	 	if form.is_valid():
	 		user = User.objects.get(username=username)
	 		tweet = Tweet(text=form.cleaned_data['text'],
			user=user,
			country=form.cleaned_data['country'])
			tweet.save()
			words = form.cleaned_data['text'].split(" ")
			for word in words:
				if word[0] == "#":
					hashtag, created =HashTag.objects.get_or_create(name=word[1:])
					hashtag.tweet.add(tweet)
			return HttpResponseRedirect('/user/'+username)
		else:
			print form
			return HttpResponseRedirect('/user/'+username)

class Search(View):
	def get(self,request):
		form=SearchForm()
		params=dict()
		params['search']=form
		return render(request,'search.html',params)
	def post(self,request):
		form=SearchForm(request.POST)
		if form.is_valid():
			query=form.cleaned_data['query']
			tweets=Tweet.objects.filter(text__icontains=query)
			context=dict({'query':query,'tweets':tweets})
			template=get_template('partials/_tweet_search.html')
			return_str=template.render(context)
			return HttpResponse(json.dumps(return_str),content_type="application/json")
		else:
			HttpResponseRedirect('/search')
























