from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^kols/$', 'koldb.views.index'),
    url(r'^kols/(?P<poll_id>\d+)/$', 'koldb.views.detail'),
    url(r'^kols/(?P<poll_id>\d+)/results/$', 'koldb.views.results'),
    url(r'^kols/(?P<poll_id>\d+)/vote/$', 'koldb.views.vote'),
    





    # Examples:
    # url(r'^$', 'helloheroku.views.home', name='home'),
    # url(r'^helloheroku/', include('helloheroku.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
