from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.http.response import HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from buyinglist.models import Item
from .forms import ItemForm

# Create your views here.

# def additem(request):
# 	return render_to_response('additem.html',{'item': "ogurec"})

def tobuy(request):
	return render(request, 'tobuy.html',{'items': Item.objects.all()})

def additem(request):
	return render(request, 'additem.html', {'form':ItemForm})

def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ItemForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            form.save()
            # import pdb; pdb.set_trace()
            return HttpResponse('thanks') # Redirect after POST
    else:
        form = ItemForm() # An unbound form

	return HttpResponse("somth wrong. it's not a post request")
