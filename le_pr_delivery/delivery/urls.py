from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'le_pr_delivery.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^main_page/$', views.mainPage),
    url(r'^restaurant/$', views.restaurant),
	url(r'^$', views.index)
)
