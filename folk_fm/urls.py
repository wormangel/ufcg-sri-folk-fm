from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView
from folkapp.models import UserProfile

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

    url(r'^$', 'folkapp.views.index'),
    url(r'^user/$', ListView.as_view(queryset=UserProfile.objects.all(), context_object_name='users', template_name='user_list.html')),
    url(r'^user/(?P<pk>\d+)/$', DetailView.as_view(model=UserProfile, template_name='user_profile.html')),
    url(r'^band/(?P<id_band>\d+)/$', 'folkapp.views.band_profile'),
    url(r'^tag/(?P<id_tag>\d+)/$', 'folkapp.views.bands_by_tag'),
    url(r'^recommendations/$', 'folkapp.views.recommendations'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login'),
    url(r'^start/$', 'folkapp.views.populate_test_db'),
)
