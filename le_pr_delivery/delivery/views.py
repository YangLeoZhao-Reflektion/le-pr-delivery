from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response
import json
from models import Restaurants

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
