# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import Property
import json

def index(request):
	return HttpResponse("Success")
	
def viewMap(request): 	
	d={}
	props = Property.objects.all()
	
	for i in props:
		cleanProp_ID = str(i.prop_id)
		d[cleanProp_ID]=[i.lat,i.lng]
	
	json_dict = json.dumps(d)

	return render(request, "multiple.html", {"test_list":json_dict})


		


	
	
	
			