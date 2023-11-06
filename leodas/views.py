from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
from .models import leodas

def index(request):
    return HttpResponse("hello World")

def html(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())

def lcu(request):
    mymembers=leodas.objects.all().values()
    output=""
    for x in mymembers:
        output+= x['firstname']+x['lastname']
    return HttpResponse(output)
def lcu1(request):
    mymembers=leodas.objects.all().values()
    template=loader.get_template('lcu.html')
    context={
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context,request))