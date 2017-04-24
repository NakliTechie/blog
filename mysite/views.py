from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
import datetime
from mysite.forms import ContactForm
from django.core.mail import send_mail

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

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'), ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
            form = ContactForm(initial = {'subject': 'I Love your site'})
    return render(request, 'contact_form.html', {'form': form})


'''
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'), ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})
'''