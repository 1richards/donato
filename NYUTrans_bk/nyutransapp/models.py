from django.db import models

class Routes (models.Model) :
	
	Route = models.CharField(max_length=50)	
	def __unicode__(self):
		return self.Route

class Stops (models.Model) :
	name = models.CharField(max_length=50)
	latitude = models.DecimalField(max_digits=19, decimal_places=10)
	longitude = models.DecimalField(max_digits=19, decimal_places=10)
        routes = models.ManyToManyField(Routes)

# Create your models here.
