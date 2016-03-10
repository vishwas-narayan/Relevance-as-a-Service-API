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