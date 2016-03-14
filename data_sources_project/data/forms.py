from django import forms
from .models import QueryData


class QueryDataForm(forms.ModelForm):
	class Meta:
		model = QueryData
		fields = ['query','start','rows']

	# overriding the validation of the form 
	def clean_query(self):
		query = self.cleaned_data.get('query')
		return query

class ArticleForm(forms.Form):
	query = forms.CharField(required = True)
	start = forms.IntegerField(required = True)
	rows = forms.IntegerField(required = True)

class InfluencerForm(forms.Form):
	query = forms.CharField(required = True)
	start = forms.IntegerField(required = True)
	rows = forms.IntegerField(required = True)

class ConversationForm(forms.Form):
	query = forms.CharField(required = True)
	page = forms.IntegerField(required = True)
	rows = forms.IntegerField(required = True)
	# orderby = forms.CharField(default = Relevance, blank = True) 
class AutoCompleteForm(forms.Form):
	q = forms.CharField(required = True)
	