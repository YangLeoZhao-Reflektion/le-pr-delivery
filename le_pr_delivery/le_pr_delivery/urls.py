from django.conf.urls import patterns, include, url
from django.contrib import admin
from delivery import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'le_pr_delivery.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	#url(r'^homepage/', 'le_pr_delivery.templates')
	url(r'^', include('delivery.urls')),
	#url(r'^admin/', include(admin.site.urls)),
)
