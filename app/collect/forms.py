from django import forms
from collect.models import *

def getRouteChoices():
	items = list(Route.objects.all().values_list('title', flat=True).distinct())
	return sorted(zip(items, items))

class RouteSelectForm(forms.Form):
	def __init__(self,*args,**kwargs):
		super(RouteSelectForm,self).__init__(*args,**kwargs)

		self.fields['route'] = forms.ChoiceField(
								widget=forms.Select(),
								choices=getRouteChoices(),
								required=False)