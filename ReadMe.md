# Django Learning Tool

## Inspiration
As a new developer, it is easy to get stuck in a bubble learning just one programming language and never daring to venture outside of it. **So I wondered, what would it be like to step outside of that bubble for myself?**

I recently stepped out of my bubble into the world of Ruby on Rails. Now I'm stepping into Python and Django, in part due hearing about some incredible roles that use them..

<!-- ## What it does -->
<!-- Description of the project  -->

<!-- ## How we built it -->
<!--  -->

<!-- ## Challenges we ran into -->
<!--  -->

<!-- ## Accomplishments that we're proud of -->

## What I learned
### Q/ Which package manager is used with python?
pip

### Q/ Which well-known websites use django?
Instagram, Spotify, Dropbox.


### Q/ What are django apps?
- django apps are standalone applications you can plug and play. In theory, you can take it out of this django project and put it in another one.
- These apps contain different things including database models, different views or routes, templates, and more.
- We can separate different logics into different applications. For instance, you may have one app for authentication, one for specific user types (e.g. admins/moderators), one that displays the main content of the website, etc.


### Q/ How can you setup a django project?
- install django package: in the terminal, enter "pip install django", or "pip3 ..." on mac/linux
- start django project: restart your terminal, and enter "django-admin startproject djangolearningtool". This will create two folders called "djangolearningtool" with some scaffolded files.
    - within the parent "djangolearningtool" folder, we have one file "manage.py" that we run commands from like running a python server, making database migrations or creating users for the django admin panel.
    - within the child "djangolearningtoolfolder", we have...
        - "_init__.py" tells python to treat this directory like a python package.
        - "asgi.py" and "wsgi.py" are configuration files that allow django to communicate with the web server.
        - "settings.py" is used when we install different apps, install plugins, change middleware, modify database engines and more.
        - "urls.py" allows us to configure different url routes that we can direct to different django apps

### Q/ How can you make and link an app in your project? How to configure URLs?
- make an app: in the parent "djangolearningtool" folder, enter the command "python manage.py startapp myfirstapp". This creates a folder within the project called "myfirstapp", and scaffolds some boilerplate code.
    - within the folder, we find...
        - a folder called "migrations"
        - "_init__.py" tells python to treat this directory like a python package.
        - "admin.py" allows us to register database models so we can view them on our admin panel.
        - "apps.py" ...
        - "models.py" is where we place database models
        - "tests.py" is where we can write automated test cases
        - "views.py" is where we create different views or routes that we can access on our website.
- add a "urls.py" file to the newly created app: create a "urls.py" file inside "myfirstapp".
    - This is where we will create different url routes and then we'll connect them to our views.
    - write "from django.urls import path"
    - write "from . import views"
    - write "url patterns = [
        path("", views.home, name="home")
    ]"
- create an example view (part 1): add ", HttpResponse" to the imports from "django.shortcuts"
- create an example view (part 2): create a function by adding "def home(request): return HttpResponse("SimpleHttpResponse")"
    - def creates the function, home is the name of the function,
    - the parameter "request" is an object that has access to query parameters and request bodies.
    - the return can be a rendered template or a simple HttpResponse
    - note: you can create multiple functions here. I made one called "extras" that returned a different HttpResponse
- link newly made app to django project (part 1): in the child "djangolearningtool" folder, add ", 'myfirstapp'" to the "INSTALLED_APPS" list in the "settings.py" file.
- link newly made app to django project (part 2): in the child "djangolearningtool" folder, add the import for ", include" from "django.urls", then add "urlpatterns = [path("", include(myfirstapp.urls))"]"
    - whenever we go to the empty string "", we forward all the different urls into "myfirstapp/urls.py" where they will then be handled
    - the same thing happens if we got to the url bar and add "/anotherexample"
    - if we add "/extras" we will go to the "/extras" path specified in the "myfirstapp/urls.py" file

- run the server to check it is all working: inside the parent "djangolearningtools" folder, enter "python manage.py runserver"
    - note: the unapplied migrations error will appear but can be ignored for now
    - you will be linked to local host 8000 and you should receive the desired response.
    - in my project, I created an "extras" path too, which could be accessed by going to "/extras"

### Q/ What are blocks?
- Blocks are overridable pieces of content used in templates
- For example, we may have "<title> {% block title %} Django App {% endblock %}</title>" in our HTML file
    - This title can be overridden in another template.
- Alternatively, we can have "<div class="container"> {% block content %} {% block endblock %} </div>"


### Q/ How to use templates to display dynamic data?
- create a "templates" folder inside your application folder "myfirstapp". It must be called "templates"
- in the "templates" folder, create a file called "base.html"
    - inside "base.html" we can use the "Jinja templating engine" to help us display dynamic data.
    - for this app, we paste in a template from online.
- in the "templates" folder, create a file called "home.html"
    - write ... "{% extends "base.html" %} {% block title %} Home Page {% endblock %}
                    {% block content %} <p> this is the home page</p>
                    {% endblock %}"
        - extends "base.html" means we import all the code from base.html, for instance styling or meta info
        - block title is overridden with "Home Page"
        - block content is overridden with just a p tag



### Q/ How to create database models
### Q/ How to render dynamic data with templates
### Q/ How to use the Django admin panel


### Q/ Any other notes
Django is compatible with many different databases.

## Built with
Python, Django, HTML, CSS

<!-- ## Try it out -->
<!-- [Ruby on Rails Pokedex Deployment](https://rubyonrails-pokedex.onrender.com/pokemonsters) -->


______________________________________________________________________

# Guidance for any other JavaScript developers wanting to try making a clone of the project - an A to Z guide:
I suggest breaking this up into chunks.

## Installations
* Install Python. This may be easier on Windows and Linux rathre than Apple devices.

## Project scaffolding and setup
* ...

## Styling
...

## Deployment
...

## An extra challenge
...
