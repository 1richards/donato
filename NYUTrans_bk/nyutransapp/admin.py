from django.contrib import admin
from nyutransapp.models import Routes
from nyutransapp.models import Stops

admin.autodiscover()
admin.site.register(Routes)
admin.site.register(Stops)

# Register your models here.
