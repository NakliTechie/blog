from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse, Http404
import datetime

def hello(request):
    return HttpResponse("Hello world")

def index(request):
    return HttpResponse("home")

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "In %s hours time will be %s" % (offset, dt)
    return HttpResponse(html)
