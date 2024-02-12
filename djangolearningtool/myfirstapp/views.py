# imports. Default import includes render only, not HttpResponse which needed to be added.
from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request): 
    return HttpResponse("Simple Http Response")
# def creates a function
# home is the name of the function
# the request object allows us to take in query parameters and the body of requests sent to this function
# we can return either some rendered templates, or an Http response

def extras(request): 
    return HttpResponse("Extra info")