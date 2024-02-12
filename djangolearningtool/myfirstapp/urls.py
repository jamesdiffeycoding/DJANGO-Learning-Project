from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("extras", views.extras, name="extras")

]
# an empty path, "", means we go to the base url of the website.
# views.home connects it to the home function in the views file
# name="home" just gives it a name of "home"
# in summary, when we go to the path specified we call the function specified and receive its response 
