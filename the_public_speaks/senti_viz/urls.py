from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^display/$', views.display, name='display'),
	url(r'^search/(?P<query>.*)/$', views.search, name='search'),
]
