from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app4_first(request):
    return HttpResponse('this is python with django')