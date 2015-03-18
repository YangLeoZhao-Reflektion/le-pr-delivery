from django.http import HttpResponseRedirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.messages.api import get_messages
from django.template import RequestContext
from django.shortcuts import render_to_response
from social_auth import __version__ as version
from delivery.lib.model_related.restaurant_functions import search_restaurants

from delivery.lib.model_related.user_functions import get_users_entry


def index(request):
	return render_to_response('le_pr_delivery/index.html')


def mainPage(request):
	return render_to_response('le_pr_delivery/main_page.html')


def bootstrap_css(request):
	return render_to_response('le_pr_delivery/bootstrap.css')


def home(request):
	"""Home view, displays login mechanism"""
	if request.user.is_authenticated():
		return HttpResponseRedirect('done')
	else:
		return render_to_response('le_pr_delivery/home.html', {'version': version}, RequestContext(request))


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
	return render_to_response(
		'le_pr_delivery/error.html',
		{'version': version, 'messages': messages},
		RequestContext(request)
	)


def logout(request):
	"""Logs out user"""
	auth_logout(request)
	return HttpResponseRedirect('/')


def search(request):
	query = request.GET['query']
	if query:
		results = search_restaurants(query)
		for result in results:
			print result.__names__()
	return HttpResponseRedirect('/')
