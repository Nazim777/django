1. create project = django-admin startproject [project name]
2. run the server = python manage.py runserver
3. python manage.py migrate
4. create super user => python manage.py createsuperuser
5. create models => python manage.py startapp service
6. after creating models and fields =>
a. python manage.py makemigrations
b. python manage.py migrate
7. implement text editor 
a. install=> pip install django-tinymce
b. add to tinymce in the settings.py
c. look at the official docs