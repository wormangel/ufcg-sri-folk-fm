from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'folk_fm.views.home', name='home'),
    # url(r'^folk_fm/', include('folk_fm.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^folkapp/$', 'folkapp.views.index'),
    url(r'^folkapp/user/(?P<id_user>\d+)/$', 'folkapp.views.user_profile'),
    url(r'^folkapp/band/(?P<id_band>\d+)/$', 'folkapp.views.band_profile'),
    url(r'^folkapp/tag/(?P<id_tag>\d+)/$', 'folkapp.views.bands_by_tag'),
    url(r'^folkapp/recommendations/$', 'folkapp.views.recommendations'),
    url(r'^folkapp/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
)
