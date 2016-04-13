from django.core.urlresolvers import reverse
from django.shortcuts import render,get_object_or_404,redirect
import random,datetime
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
from django.utils import timezone
from django.views.decorators.http import require_http_methods
from django.forms import formset_factory
from .forms import UploadFileForm,LoginForm,NameForm,ArticleForm
def handle_uploaded_file(f):
    print f
    # change the save path
    with open('somefile','wb+') as distination:
        for chunk in f.chunks():
            distination.write(chunk)

# Create your views here.
def special_year(request,year):
    return HttpResponse('hello world')
def root(request):
    year=2016
    return HttpResponseRedirect(reverse('articles:year',args=(year,)))

@require_http_methods(['GET'])
def current_datetime(request):
    now=datetime.datetime.now()
    html='<html><body>It is now %s </body></html>' % now
    return HttpResponse(html)

def my_random_view(request):
    foo= True if random.random()>0.5 else False
    if foo:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    else:
        return HttpResponse('<h1>Page was found</h1>')

def upload_file(request):
    if request.method == 'POST':
        form=UploadFileForm(request.POST,request.FILES)
        print form.is_valid()
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect(reverse('articles:root'))
    else:
        form=UploadFileForm()
    return render(request,'upload.html',{'form':form})

def redirectToBing(request):
    return redirect('http://bing.com')

def post_comment(request):
    if request.session.get('has_commented',False):
        return HttpResponse('You have already commented')
    request.session['has_commented']=True
    return HttpResponse('Thanks for your comment')

def login(request):
    if request.method=='POST':
        if request.POST['username'] and request.POST['password']:
            if request.POST['username']==request.POST['password']:
                request.session['user']=request.POST['username']
                return HttpResponse('You are login')
            else:
                return HttpResponse('Your infomation is not right')
    else:
        if request.session.get('user',False):
            redirect('articles:root')
        else:
            loginform=LoginForm()
            return render(request,'login.html',{'form':loginform})

def logout(request):
    try:
        del request.session['user']
    except Exception, e:
        pass
    return redirect('articles:login')

def formlist(request):
    nameForm=NameForm()
    if request.method == 'POST':
        form=NameForm(request.POST)
        if form.is_valid():
            subject=form.cleaned_data['subject']
            message=form.cleaned_data['message']
            return HttpResponse('form is right')
        else:
            return render(request,'form.html',{'form':form})
    ArticleFormSet = formset_factory(ArticleForm, can_order=True)
    formSet=ArticleFormSet(initial=[{'title':'Art1','pub_date': datetime.date(2008, 5, 10)},{'title':'Art1','pub_date': datetime.date(2008, 1, 10)}])
    return render(request,'form.html',{'form':nameForm,'article':formSet})
