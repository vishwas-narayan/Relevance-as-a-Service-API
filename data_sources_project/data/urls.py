from django.conf.urls import url
from data import views

urlpatterns = [
	url(r'^$','data.views.index',name='index'),
	url(r'^articles/$','data.views.articles',name='articles'),
	url(r'^influencers/$','data.views.influencers',name='influencers'),
	url(r'^conversations/$','data.views.conversations',name='conversations'),
	url(r'^autocomplete/$','data.views.autocomplete',name='autocomplete'),
]