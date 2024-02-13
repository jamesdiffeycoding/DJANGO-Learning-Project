"""
URL configuration for djangolearningtool project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# the include import is not included by default, I added it below
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("myfirstapp.urls")),
    path("anotherexample/", include("myfirstapp.urls"))
]

# whenever we go to the empty string "", we forward all the different urls into "myfirstapp/urls.py" where they will then be handled
# the same thing happens if we got to the url bar and add "/anotherexample"
# if we add "/extras" we will go to the "/extras" path specified in the "myfirstapp/urls.py" file