from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views
from delivery.views import *

urlpatterns = patterns('',
	url(r'^main_page/$', views.mainPage),
	url(r'^$', home, name='home'),
	url(r'^done/$', done, name='done'),
	url(r'^login-error/$', error, name='error'),
	url(r'^logout/$', logout, name='logout'),
	url(r'^search/$', search, name='search'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'', include('social_auth.urls')),
)
