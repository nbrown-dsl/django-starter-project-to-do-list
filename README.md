# django-starter-project-to-do-list
this is start of adaption of to do list into protocol app

To migrate models to database run heroku in a bash shell (specifying app name) and then run migration.
$ heroku run bash -a dwight-london-protocols
(you will need to cd to parent dir of manage.py file when in heroku shell)
$ python manage.py makemigrations
$ python manage.py migrate

