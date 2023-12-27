from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def my_view(request):
    return HttpResponse("<h1>This is a demo view in Django!<h1/>")
