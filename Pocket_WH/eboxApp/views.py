from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from eboxApp.models import *
from eboxApp.forms import *

def index(request):
    return render (request, 'eboxApp/index.html')