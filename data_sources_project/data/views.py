from django.shortcuts import render
from django.http import HttpResponse
import requests
from .forms import ArticleForm, InfluencerForm, QueryDataForm
from .forms import ConversationForm,AutoCompleteForm

def home(request):
	title = "This is the home page.Django server is running successfully"					
	#if request.user.is_authenticated():
	#	title = "My Title %s" %(request.user)
	context_dict = {
		"template_title":title,
	}
	#add a form 
	return render(request,"data/home.html", context_dict)

# this demo function uses model to store the query data
def index(request):
	title = "Query Data API"
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


def articles(request):
	title = "Articles API"
	articleform = ArticleForm(request.POST or None)

	context_dict = {
		'title':title,
		'articleform':articleform,
	}

	if articleform.is_valid():
		query = articleform.cleaned_data.get('query')
		start = articleform.cleaned_data.get('start')
		rows = articleform.cleaned_data.get('rows')
		payload = {'query':query,'start':start,'rows':rows,'access_token':'68a98c9fe9ebfc409d7d46bd9d496561045e9d52372c8896c8f25d1d6e64e1d8'}
		r = requests.get("http://api.rightrelevance.com/v2/articles/search",params=payload)
		return HttpResponse(r)
	return render(request, "data/articles.html",context_dict)

def influencers(request):
	title = "Influencers API"
	influencerform = InfluencerForm(request.POST or None)

	context_dict = {
		'title':title,
		'influencerform':influencerform,
	}

	if influencerform.is_valid():
		query = influencerform.cleaned_data.get('query')
		start = influencerform.cleaned_data.get('start')
		rows = influencerform.cleaned_data.get('rows')
		payload = {'query':query,'start':start,'rows':rows,'access_token':'68a98c9fe9ebfc409d7d46bd9d496561045e9d52372c8896c8f25d1d6e64e1d8'}
		r = requests.get("http://api.rightrelevance.com/v2/experts/search",params=payload)
		return HttpResponse(r)
	return render(request, "data/influencers.html",context_dict)

def conversations(request):
	title = "Conversations API"
	conversationform = ConversationForm(request.POST or None)

	context_dict = {
		'title':title,
		'conversationform':conversationform,
	}

	if conversationform.is_valid():
		query = conversationform.cleaned_data.get('query')
		page = conversationform.cleaned_data.get('page')
		rows = conversationform.cleaned_data.get('rows')

		payload = {'query':query,'page':page,'rows':rows,'access_token':'68a98c9fe9ebfc409d7d46bd9d496561045e9d52372c8896c8f25d1d6e64e1d8'}
		r = requests.get("http://api.rightrelevance.com/v2/conversations/search",params=payload)
		return HttpResponse(r)
	return render(request, "data/conversations.html",context_dict)

def autocomplete(request):
	title = "AutoComplete API"
	autocompleteform = AutoCompleteForm(request.POST or None)

	context_dict = {
		'title':title,
		'autocompleteform':autocompleteform,
	}

	if autocompleteform.is_valid():
		q = autocompleteform.cleaned_data.get('q')
		payload = {'q':q, 'access_token':'68a98c9fe9ebfc409d7d46bd9d496561045e9d52372c8896c8f25d1d6e64e1d8'}
		r = requests.get("http://api.rightrelevance.com/v2/topics/autocomplete",params = payload)
		return HttpResponse(r)
	return render(request, "data/autocomplete.html",context_dict)

