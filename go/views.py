from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Person

def setResponse(request):
    persons = Person.objects.all().values()
    template = loader.get_template('persons.html')
    context ={
        'persons':persons
    }
    return HttpResponse(template.render(context,request))

# Create your views here.
