from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime

def current_datetime(request):
	now = datetime.datetime.now()
	return render_to_response('index.html',{'current_datetime':now})

def xsck(request):
	return render_to_response('xsck.html')