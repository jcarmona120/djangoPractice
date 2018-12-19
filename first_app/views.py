from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    my_dictionary = {'insert_me': "Gotcha!!"}
    return render(request, 'first_app/index.html', context=my_dictionary)


def whatawebsite(request):
    return HttpResponse('<h1>What a Website</h1>')
