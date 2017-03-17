from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book
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
    error = False
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        if not q:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html', {'books': books, 'query': q})
#        message = 'You searched for: %s' % request.GET['q']
    else:
        return render(request, 'search_form.html', {'error': error})
    return HttpResponse(message)
