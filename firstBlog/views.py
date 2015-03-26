from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from models import book
import datetime

# Create your views here.
def blog(request):
    return HttpResponse('<h1>Hello Alfred, it is now: %s</h1>' % datetime.datetime.now())

def latest_book(request):
    book_list = book.objects.order_by('-pub_data')[:10]
    return render_to_response('latest_books.html', {'book_list': book_list})

def hours_ahead(request, offset):
    # offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body><h1>In %s hour(s), it will be %s.</h1></body></html>" % (offset, dt)
    return HttpResponse(html)