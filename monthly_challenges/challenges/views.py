from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(req):
    return HttpResponse("This works!")

def secondIndex(req):
    return HttpResponse("This also works!")