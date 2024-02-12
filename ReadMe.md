# Django Learning Tool

## Inspiration
As a new developer, it is easy to get stuck in a bubble learning just one programming language and never daring to venture outside of it. **So I wondered, what would it be like to step outside of that bubble for myself?**?

I recently stepped out of my bubble into the world of Ruby on Rails. Now I'm stepping into Python and Django, in part due hearing about some incredible roles that use them..

<!-- ## What it does -->
<!-- Description of the project  -->

<!-- ## How we built it -->
<!--  -->

<!-- ## Challenges we ran into -->
<!--  -->

<!-- ## Accomplishments that we're proud of -->

## What I learned
Q/ Which package manager is used with python?
pip

Q/ Which well-known websites use django? 
Instagram, Spotify, Dropbox.

Q/ Any other notes
Django is compatible with many different databases. 

Q/ How to setup a django project?
- install django package: in the terminal, enter "pip install django", or "pip3 ..." on mac/linux
- start django project: restart your terminal, and enter "django-admin startproject djangolearningtool". This will create two folders called "djangolearningtool" with some scaffolded files.
    - within the parent "djangolearningtool" folder, we have one file "manage.py" that we run commands from like running a python server, making database migrations or creating users for the django admin panel.
    - within the child "djangolearningtoolfolder", we have...
        - "init.py" tells python to treat this directory like a python package.
        - "asgi.py" and "wsgi.py" are configuration files that allow django to communicate with the web server. 
        - "settings.py" is used when we install different apps, install plugins, change middleware, modify database engines and more.
        - "urls.py" allows us to configure different url routes that we can direct to different django apps
- make an app: in the parent "djangolearningtool" folder, enter the command "python manage.py startapp myfirstapp". This creates a folder within the project called "myfirstapp", and scaffolds some boilerplate code.
    - within the folder, we find...
        - a folder called "migrations"
        - "init.py"
        - "admin.py"
        - "apps.py"
        - "models.py"
        - "tests.py"
        - "views.py" 


Q/ What are django apps?
- django apps are standalone applications you can plug and play. In theory, you can take it out of this django project and put it in another one. 
- These apps contain different things including database models, different views or routes, templates, and more.


Q/ How to configure URLs
Q/ How to create database models
Q/ How to render dynamic data with templates
Q/ How to use the Django admin panel


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
