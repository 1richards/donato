from django.conf.urls import patterns, url

from nyutransapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
