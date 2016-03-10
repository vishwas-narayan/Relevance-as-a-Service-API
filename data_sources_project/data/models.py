from django.db import models

# Create your models here.
class QueryData(models.Model):
	query = models.CharField(max_length=120,blank=False)
	start = models.IntegerField(default=0,blank=False)
	rows = models.IntegerField(default=1,blank=False)

	def __unicode__(self):
		return self.query

