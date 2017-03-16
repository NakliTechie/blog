from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.

def display_met(request):
    values = request.META.items()
    sorted(values)
    html = []
    for k, v in values:
        html.append('<tr><td>{0}</td></tr>'.format(k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def search_form(request):
    return render(request, 'search_form.html')

def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %s' % request.GET['q']
    else:
        message = 'You submitted an empty string'
    return HttpResponse(message)
