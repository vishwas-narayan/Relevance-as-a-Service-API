from django.conf.urls import url
from data import views

urlpatterns = [
	url(r'^$',views.index,name='index'),
]