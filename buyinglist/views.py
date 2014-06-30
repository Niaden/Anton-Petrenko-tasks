from django.shortcuts import render
from django.http.response import HttpResponse
from buyinglist.models import Item

# Create your views here.

def tobuy(request):
	view = "some text"
	html = "<html><body><h3>%s</h3></html></body>" % view
	return HttpResponse(html)