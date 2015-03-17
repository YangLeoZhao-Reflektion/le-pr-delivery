from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response

def index(request):
	return render_to_response('le_pr_delivery/index.html')

def mainPage(request):
	return render_to_response('le_pr_delivery/main_page.html')

def bootstrap_css(request):
	return render_to_response('le_pr_delivery/bootstrap.css')
