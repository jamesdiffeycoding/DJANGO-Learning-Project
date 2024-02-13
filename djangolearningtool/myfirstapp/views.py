# imports. Default import includes render only, not HttpResponse which needed to be added.
from django.shortcuts import render, HttpResponse
from .models import TodoItem

# Create your views here.
def home(request): 
    # return HttpResponse("Simple Http Response")
# def creates a function
# home is the name of the function
# the request object allows us to take in query parameters and the body of requests sent to this function
# we can return either some rendered templates, or an Http response
    return render(request, "home.html")
# this return uses django's template functionality


def extras(request): 
    return HttpResponse("Extra info")


def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", { "todos": items })


def pythonoverview(request):
    return render(request, "pythonoverview.html")


def djangovaluepurpose(request):
    items = TodoItem.objects.all()
    return render(request, "djangovaluepurpose.html")


def djangoprojectsfileapps(request):
    items = TodoItem.objects.all()
    return render(request, "djangoprojectsfileapps.html")


def djangomigrations (request):
    items = TodoItem.objects.all()
    return render(request, "djangomigrations.html")


def djangoadvanced(request):
    items = TodoItem.objects.all()
    return render(request, "djangoadvanced.html")
