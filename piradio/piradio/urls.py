from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'remote.views.main_page'),
	url(r'^stop/$', 'remote.views.stop'),
	url(r'^volumeUp/$', 'remote.views.volumeUp'),
	url(r'^volumeDown/$', 'remote.views.volumeDown'),
	url(r'^seek/(?P<no>\d+)/$', 'remote.views.seek')
    # Examples:
    # url(r'^$', 'piradio.views.home', name='home'),
    # url(r'^piradio/', include('piradio.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
