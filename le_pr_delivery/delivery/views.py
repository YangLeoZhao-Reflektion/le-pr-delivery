from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.messages.api import get_messages
from django.views.generic import View

from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from models import Restaurants
from social_auth import __version__ as version
from delivery.lib.user_functions import get_users_entry


def index(request):
	return render_to_response('le_pr_delivery/index.html')


def mainPage(request):
	return render_to_response('le_pr_delivery/main_page.html')


def restaurant(request):
	return_list = []
	all_restaurants = Restaurants.objects.all()
	for restaurant in all_restaurants:
		return_list.append(restaurant.__names__())
		return_list.append(',')
	#object = (data=models(Foo.objects.get(pk=object_id)))
	return_list.append('hi')
	print return_list
	return HttpResponse(return_list)
	#return render_to_response({'data': models.Restaurants.__name__})
	# return render_to_response('le_pr_delivery/main_page.html', {'data': str(models.Restaurants.__name__)})


def home(request):
	"""Home view, displays login mechanism"""
	if request.user.is_authenticated():
		return HttpResponseRedirect('done')
	else:
		return render_to_response('le_pr_delivery/home.html', {'version': version},
								  RequestContext(request))


@login_required
def done(request):
	"""Login complete view, displays user data"""
	get_users_entry(request);
	ctx = {
		'version': version,
		'last_login': request.session.get('social_auth_last_login_backend')
	}
	return render_to_response('le_pr_delivery/done.html', ctx, RequestContext(request))


def error(request):
	"""Error view"""
	messages = get_messages(request)
	return render_to_response('le_pr_delivery/error.html', {'version': version,
											 'messages': messages},
							  RequestContext(request))


def logout(request):
	"""Logs out user"""
	auth_logout(request)
	return HttpResponseRedirect('/')
