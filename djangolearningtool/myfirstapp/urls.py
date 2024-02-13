from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # path("todos", views.todos, name="todos"),
    # path("extras", views.extras, name="extras"),
    path("pythonoverview", views.pythonoverview, name="pythonoverview"),
    path("djangovaluepurpose", views.djangovaluepurpose, name="extra2"),
    path("djangoprojectsfileapps", views.djangoprojectsfileapps, name="djangoprojectsfileapps"),
    path("djangomigrations", views.djangomigrations, name="djangomigrations"),
    path("djangoadvanced", views.djangoadvanced, name="djangoadvanced"),
]
# an empty path, "", means we go to the base url of the website.
# views.home connects it to the home function in the views file
# name="home" just gives it a name of "home"
# in summary, when we go to the path specified we call the function specified and receive its response 
