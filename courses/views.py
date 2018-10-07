
from django.http import HttpResponse
from django.shortcuts import render

def hello_word_view(request, name):
    print int(name)
    # print request
    return HttpResponse("Hello %s!!!" % name)

def index(request):
    return render(request, 'index.html')

def contacts(request):
    return render(request, 'contact.html')