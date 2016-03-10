from django.contrib import admin

# Register your models here.
from .models import QueryData
from .forms import QueryDataForm

class QueryDataAdmin(admin.ModelAdmin):
	list_display=["__unicode__"]
	form = QueryDataForm

admin.site.register(QueryData, QueryDataAdmin) 