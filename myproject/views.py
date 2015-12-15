from django.shortcuts import render
from django.template import RequestContext 


def index(request):
	context = {}
	template = "index.html"
	return render(request, template, context)