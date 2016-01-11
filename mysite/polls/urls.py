from django.conf.urls import url
from . import views
print('include polls-url')
urlpatterns = [
    url(r'^$', views.index, name='index'),
]