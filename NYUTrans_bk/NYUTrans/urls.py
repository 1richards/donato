from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
      url(r'^$', 'NYUTrans.views.home', name='home'),
    # url(r'^blog/', include('admin.site.urls')),
      url(r'^admin/', include(admin.sites.urls)),
)
