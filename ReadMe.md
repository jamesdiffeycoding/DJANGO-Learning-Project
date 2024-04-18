# Django Learning Tool
![DjangoShotBanner](https://github.com/jamesdiffeycoding/DJANGO-Learning-Project/assets/139918141/46dc3496-376d-453d-aa35-fb6764e98f00)

## Inspiration
I wanted to learn more about Python and Django after hearing about some great projects that use them.
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

### Q/ How do you run the server?
 - inside the parent "djangolearningtools" folder, enter "python manage.py runserver"

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
        - "extends "base.html"" means we import all the code from base.html, for instance styling or meta info
        - block title is overridden with "Home Page"
        - block content is overridden with just a p tag
- to render the template return to the "views.py" file inside the "myfirstapp" folder, and tweak a return to be "render(request, "home.html").
    - this will search for a file called "home.html" inside the "templates" folder.

### Q/ What is Object Relational Mapping ORM?
- django provides object relational mapping (ORM). This means we can use python code to create database models, and then django will make these compatible with other database scheme like SQLLite3 or MongoDB (or whatever other backend database engine we are using).
- 'migrations' in django are a function that make corresponding models of our code in other schemas.

### Q/ How to create database models? What about migrations?
- inside the "myfirstapp" folder you'll see the "models.py" file, add to it "class TodoItem(models.Model):
    title=models.CharField(max_length=200)
    completed=models.BooleanField(default=False)"
- to register this database, go to "admin.py" in the "myfirstapp" folder. Import the TodoItem with "from .models import TodoItem", followed by a registering it with "admin.site.register(TodoItem)".
    - Now when we go to our site's admin panel we will be able to view this model

- Any time you change your database models, you need to do a migration (automated code which applies to the database which allows you to change your models and update them while maintaining that data and ensuring it won't be removed when you make changes to the database schema)
- In the terminal in your child "djangolearningtool" folder, enter "python manage.py makemigrations".
- To create a template to view all the todo items we have, create a file called "todos.html" in the "templates" folder. Use the code below to create a view
    - {% extends "base.html" %} {% block content %}
        <h1>Todo list</h1>
        <ul>
            <!-- a for loop to map the todos -->
            {% for todo in todos %}
            <!-- variables can be rendered using two sets of curly braces -->
            <!-- if statement allows a return if true and a return if false -->
            <li>{{ todo.title }}: {% if todo.completed %}Completed{% else %}Not completed {% endif %}</li>
            {% endfor %}
        </ul>
        {% endblock %}
    - as you can see, there is a for loop to map the todos, curly braces allow access to the 'python variable dictionary', and if statements can handle returns if a variable is true or false.
- Now create a view that returns that template.
    - In "myfirstapp" folder's "views.py" file write the import statement "from .models import TodoItem",
    - then write "def todos(request): items = TodoItem.objects.all() return render(request, "todos.html", {"todos": items })"
    - Then add the url "path("todos", views.todos, name="todos")" inside the "myfirstapp" folder's "urls.py" file.
- You now have a SQLLite database on your computer connected to the project. You can choose to edit the data in the django admin panel, or set it up with an online database.

### Q/ How to use the Django admin panel
- To use the django admin panel, you need to create a user. To do this, cd to the parent "djangolearningtool" folder and enter in the terminal "python manage.py createsuperuser". You may need to run "python manage.py migrate" first.
- enter a username/email (optional) and a password.
- then go to your localhost 8000 / admin for a prebuilt admin dashboard where you can sign in. It is quite useful and requires minimal configuration. 
- you should then be able to see your databases and edit their values.

### Q/ Any other notes
Django is compatible with many different databases.

## Built with
Python, Django, HTML, CSS

<!-- ## Try it out -->

