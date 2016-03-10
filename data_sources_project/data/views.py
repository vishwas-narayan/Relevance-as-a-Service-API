from django.shortcuts import render
from django.http import HttpResponse
import requests

from .forms import QueryDataForm

def home(request):
	title = "Welcome"
	#if request.user.is_authenticated():
	#	title = "My Title %s" %(request.user)
	context_dict = {
		"template_title":title,
	}
	#add a form 
	return render(request,"data/home.html", context_dict)

def index(request):
	title = "Welcome"
	form = QueryDataForm(request.POST or None)
	context_dict={
	'title':title,
	'form':form,
	}
	if form.is_valid():
		instance = form.save()
		print instance.query,instance.start,instance.rows
		query = instance.query
		start = instance.start
		rows = instance.rows
		payload = {'query':query,'start':start,'rows':rows,'access_token':'68a98c9fe9ebfc409d7d46bd9d496561045e9d52372c8896c8f25d1d6e64e1d8'}
		r = requests.get("http://api.rightrelevance.com/v2/articles/search",params=payload)
		return HttpResponse(r)
	return render(request, 'data/index.html', context_dict)
	# if request.method == 'POST':
	# 	print request.POST
	# if form.is_valid():
	# 	instance = form.save(commit=False)
	# 	#adding a default value in the database
	# 	instance.save()