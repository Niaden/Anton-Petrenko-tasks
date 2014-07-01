from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from buyinglist.models import Item

# Create your views here.

def additem(request):
	return render_to_response('additem.html',{'item': "ogurec"})

def tobuy(request):
	return render_to_response('tobuy.html',{'items': Item.objects.all()})