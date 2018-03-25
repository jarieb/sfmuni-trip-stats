from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from collect.forms import *

# Create your views here.
def index(request):
	template = loader.get_template('collect/index.html')
	start_time = ""

	if request.method == "GET":
		name = request.GET.get('route', "")
	else:
		name = request.POST.get('route', "")

	if not name:
		name = getRouteChoices()[0][0]
		
	initial_form = {
		"route": name,
	}
	
	saved_form = request.session.get('frmRoute', initial_form)
	frmRoute = RouteSelectForm(saved_form)

	if request.method == "POST":
		frmRoute = RouteSelectForm(request.POST)

	if frmRoute.is_valid():
		request.session['frmRoute'] = frmRoute.cleaned_data

	route = frmRoute['route'].data
	
	context = {
		"frmRoute": frmRoute,
		}
	return HttpResponse(template.render(context,request))

def geo_location(request):
	template = loader.get_template('collect/geo_location.html')
	
	context = {

	}
	return HttpResponse(template.render(context,request))