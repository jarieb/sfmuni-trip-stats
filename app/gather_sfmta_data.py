import argparse
import requests
import json
import datetime
import ast
import pdb
import logging
import inspect
import sys, os, django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
django.setup()

from collect.models import *

class restbus_api:
	def __init__(self):
		'''The RestBus API setup'''
		self.base_url = 'http://restbus.info/api/agencies/sf-muni/'
		self.routes_url = 'routes/'
		self.vehicles_url = 'vehicles/'
		self.headers = {'Content-Type': 'application/json'}

	def get_json(self,content_url):

		s = requests.Session()
		s.headers.update(self.headers)
		url = self.base_url+content_url

		status = s.get(url).json()

		s.close()

		return status


if __name__ == "__main__":
	'''Script to read data via the RESTFUL API. '''
	parser = argparse.ArgumentParser(description='Read the RestBus API')

	args = parser.parse_args()

	api1 = restbus_api()

	# Go grab the latest routes

	routes = api1.get_json('routes/')

	for route in routes:
		rid = route['id']
		title = route['title']
		r1 = Route.objects.filter(rid=rid).first()

		if not r1:
			r2 = Route(rid=rid,title=title)
			r2.save()
