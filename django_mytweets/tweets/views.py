from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect

from django.views.generic import View
from .models import Tweet,HashTag
from user_profile.models import User,UserFollowers

from .forms import TweetForm,SearchForm

from  django.template import Context
from django.template.loader import render_to_string,get_template
import json
# def index(request):
# 	if request.method == 'GET':
# 		return HttpResponse('I am called from a get request')
# 	elif request.method == 'POST':
# 		return HttpResponse('I am called from a post request')
from django.core.paginator import Paginator,PageNotAnInteger, EmptyPage

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
		userProfile=User.objects.get(username=username)
		userFollower=UserFollowers.objects.get(user=userProfile)
		if userFollower.followers.filter(username = request.user.username).exists():
			params['following']=True
		else:
			params['following']=False
		form = TweetForm(initial={'country': 'Global'})
		search_form=SearchForm()
		params['search']=search_form
		tweets=Tweet.objects.filter(user=userProfile).order_by('-created_date')
		paginator=Paginator(tweets,2)
		page=request.GET.get('page')

		try:
			tweets=paginator.page(page)

		except PageNotAnInteger:
			tweets=paginator.page(1)
		except EmptyPage:
			tweets=paginator.page(paginator.num_pages)

		params['tweets']=tweets
		params['profile']=userProfile
		return render(request,'profile.html',params)


from django.contrib.auth import authenticate, login, logout
class Login(View):
	def post(self,request):
	    username = request.POST['username']
	    password = request.POST['password']
	    print username,password
	    user = authenticate(username=username, password=password)
	    if user is not None:
	    	login(request, user)
	    	return redirect('/profile')
	    else:
	        return redirect('/login')
	def get(self,request):
		return render(request,'registration/login.html')

class Logout(View):
	def get(self,request):
		logout(request)
		return redirect('/login')

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


class UserRedirect(View):
	def get(self,request):
		return HttpResponseRedirect('/user/'+request.user.username)



class Invite(View):
	def get(self,request):
		params=dict()
		success=request.GET.get('success')
		email=request.GET.get('email')
		invite=InvitationForm()
		params['invite']=invite
		params['success']=email
		params['email']=email
		return render(request,'invite.html',params)
	def post(self,request):
		form=InvitationForm(request.POST)
		if form.is_valid():
			email=form.cleaned_data['email']
			subject='Invite to join MyTweet app '
			sender_name = request.user.username
			sender_name = request.user.email
			invite_code=Invite.gen_code(email)
			link = 'http://%s/invite/accept/%s/' % (settings.SITE_HOST,invite_code)
			context = Context({"sender_name": sender_name,
         "sender_email": sender_email, "email": email, "link": link})
			invite_email_template =
			render_to_string('partials/_invite_email_template.html',context)
			msg = EmailMultiAlternatives(subject, invite_email_template,
			settings.EMAIL_HOST_USER, [email],cc=[settings.EMAIL_HOST_USER])
			user = User.objects.get(username=request.user.username)
			invitation = Invitation()
			invitation.email = email
			invitation.code = invite_code
			invitation.sender = user
			invitation.save()
			success = msg.send()
			return HttpResponseRedirect('/invite?success='+str(success)+'&email='+email)
	@staticmethod
	def gen_code(email):
		secrect=settings.SECRECT_KEY
		if isinstance(email,unicode):
			email=email.encode('utf-8')
			activation_key=hashlib.sha1(secrect+email).hexdigest()
			return activation_key














