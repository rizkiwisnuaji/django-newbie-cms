# django-newbie-cms
Very simple CMS built with Django Framework

###Installations (Manual):
1. Unzip project
2. cd to folder
3. install virtualenv (recommended) ``[sudo] pip install virtualenv``
4. activate virtualenv
5. ``pip install -r requirements.txt``
6. ``python manage.py syncdb``
7. Run the ``collectstatic`` management command: ``python manage.py collectstatic``.
8. Finally, run the app ``python manage.py runserver``

###Requirements :
1. Django==1.8.9
2. django-ckeditor==5.0.3
3. django-taggit==0.18.0
4. Pillow==3.1.1
5. pytz==2015.7
6. wheel==0.26.0
