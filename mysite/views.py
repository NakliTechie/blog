from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse, Http404
from django.shortcuts import render
import datetime

def hello(request):
    return HttpResponse("Hello world")

def index(request):
    return HttpResponse("home")

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date' : now})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "In %s hours time will be %s" % (offset, dt)
    return render(request, 'hours_ahead.html', {'next_time' : dt, 'hours' : offset})


