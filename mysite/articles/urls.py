from django.conf.urls import url
from . import views
from .views import MyView,GreetingView,MyFormView,PublisherList,PublisherBookList,ContactView
# print('include polls-url')
app_name = 'articles'
urlpatterns = [
    url(r'^$',views.root,name='root'),
    url(r'^(?P<year>[0-9]+)/$',views.special_year,name='year'),
    url(r'^random/$',views.my_random_view,name='random'),
    url(r'^date/$',views.current_datetime,name='date'),
    url(r'^upload/$',views.upload_file,name='upload'),
    url(r'^bing/$',views.redirectToBing,name='bing'),
    url(r'^post-comment$',views.post_comment,name='post_comment'),
    url(r'^login$',views.login,name='login'),
    url(r'^view-login$',MyFormView.as_view(),name='view-login'),
    url(r'^logout$',views.logout,name='logout'),
    url(r'^form$',views.formlist,name='form'),
    url(r'^template$',views.showTemplate,name='template'),
    url(r'^view-example$',views.my_view,name='view-example'),
    url(r'^view-example-class$',MyView.as_view(),name='view-example-class'),
    url(r'^view-example-class-greeting-day$',GreetingView.as_view(greeting='hello'),name='view-example-class-greeting-day'),
    url(r'^publishers/$',PublisherList.as_view()),
    url(r'^books/([\w-]+)/$', PublisherBookList.as_view()),
    url(r'^contact/$', ContactView.as_view())
]