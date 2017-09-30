from django.conf.urls import url

from . import views

urlpatterns = [
	##localhost8000
    url(r'^$', views.index, name='index'),
	##localhost8000/map
	url(r'^map/$', views.viewMap, name='viewMap'),
]