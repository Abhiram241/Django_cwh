from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request,num):
    if num<18:
        return HttpResponse("Dont vote")
    else:
        return HttpResponse('vote')

def printName(request, name):
    return HttpResponse(name)