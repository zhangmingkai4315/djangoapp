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
            return Htmy_viewtpResponseRedirect(reverse('articles:root'))
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


def showTemplate(request):
    content={
    "firstName":"Mike",
    "lastName":"Zhang",
    "date":datetime.datetime.now(),
    "describe":"my favor sport game is football",
    "some_list":[
    "hello","world","my","name","is","mike"
    ]
    }
    return render(request,'template.html',content)


def my_view(request):
    if request.method=='GET':
        return HttpResponse('Result')

from django.views.generic import View
class MyView(View):
    def get(self,request):
        return HttpResponse('Result from class ')

class GreetingView(View):
    greeting='Good day'
    def get(self,request):
        return HttpResponse(self.greeting)


class MyFormView(View):
    form_class=LoginForm
    initial={'info':'please login first'}
    template_name='view-login.html'

    def get(self,request,*args,**kwargs):
        form=self.form_class(initial=self.initial)
        return render(request,self.template_name,{'form':form})
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('articles:root'))
        return render(request,self.template_name,{'form':form})


from django.views.generic import ListView,DetailView
from .models import Publisher,Book

class PublisherList(ListView):
    model=Publisher
    template_name='publisher_list.html'

class PublisherDetail(DetailView):
    model=Publisher
    def get_context_data(self,**kwargs):
        context=super(PublisherDetail,self).get_context_data(**kwargs)
        context['book_list']=Book.objects.all()
        return context



class BookList(ListView):
    queryset=Book.objects.order_by('-publication_date')
    context_object_name='book_list'

class AcmeBookList(ListView):
    queryset=Book.objects.filter(publisher__name='Acme Publishing')
    template_name='Acme_list.html'


class PublisherBookList(ListView):
    template_name='books/books_by_publisher.html'
    def get_queryset(self):
        self.publisher=get_object_or_404(Publisher,name=self.args[0])
        return Book.objects.filter(publisher=self.publisher)
