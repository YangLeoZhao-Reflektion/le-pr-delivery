import json
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.messages.api import get_messages
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from social_auth import __version__ as version
from delivery.lib.model_related.restaurant_functions import search_restaurants

from delivery.lib.model_related.user_functions import get_users_entry


def index(request):
	return render_to_response('le_pr_delivery/index.html')


@csrf_exempt
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


@csrf_exempt
def search(request):
	print "bk1"
	if request.method == 'POST':
		query = request.POST.get('query')
		response_data = []
		print query
		if query:
			restaurants = search_restaurants(query)
			for restaurant in restaurants:
				response_data.append({"id": restaurant.id, "name": restaurant.__names__()})

		return HttpResponse(
			json.dumps(response_data),
			content_type="application/json"
		)
	else:
		return HttpResponse(
			json.dumps({"nothing to see": "this isn't happening"}),
			content_type="application/json"
		)
