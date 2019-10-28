# TEST DRIVEN DEVELOPMENT

##Steps Taken

###SETUP
```bash
cd file/path
```
Create Virtual Environment
```bash
py -3.6 -m venv virtualenv
```

virtual environment path: /c/PythonScripts/github_repo/TestDrivenDevelopment/\PythonScripts\github_repo\TestDrivenDevelopment\virtualenv/Scripts/python
```bash
source virtualenv/Scripts/activate
```
Installing packages
```bash
pip install "django<1.12" "selenium<4"
```

###SETTING THE PROJECT UP

Created a functional test in its own python file. 

Start Django project
```bash
django-admin.py startproject superlists .
```

## PROJECT PRGORESS CODE
###Adding an APP to the project
lists is the name of the app this parameter can be changed to whatever you like
```bash
python manage.py startapp lists
```
Add the name to the ```INSTALLED APPS``` in your settings file.
```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lists',
]
```
###Migrations
[Text from the book](https://www.obeythetestinggoat.com/book/chapter_post_and_database.html)   
"but there’s a second system that’s in charge of actually building the database called migrations. Its job is to give 
you the ability to add and remove tables and columns, based on changes you make to your models.py files.

One way to think of it is as a version control system for your database. As we’ll see later, it comes in particularly 
useful when we need to upgrade a database that’s deployed on a live server."

Code for the first database migration
```bash
$ python manage.py makemigrations
```

If we add a new field or table to our database or delete one then we need to make another migration. Which is done by
running the above code.

"We’ve told Django everything it needs to create the database, first via models.py and then when we created the 
migrations file. To actually apply it to creating a real database, we use another Django Swiss Army knife manage.py 
command, migrate:"

```bash
$ python manage.py migrate
```

## Start of Each Session
```bash
cd
```

```bash
source virtualenv/Scripts/activate
```

##Running Tests
```bash
python functional_tests.py
```

## CURRENT POSTIION

- Chapter 4
- Location on Page: "Improving Functional Tests: Ensuring Isolation and Removing Voodoo Sleeps"
- [Link to Current Position](https://www.obeythetestinggoat.com/book/chapter_explicit_waits_1.html)
- [Github Repo](https://github.com/hjwp/book-example/)

## TODO List

-[x] Don't save blank items for every request
-[x] Code smell: POST test is too long?
-[x] Display multiple item sin the table
-[ ] Clean up after FT runs
-[ ] Remove time.sleeps
-[ ] Support more than one list

###SCHEDULE

- Complete 3 chapters a day, 26 chapters in total: Completed two the first day. So there are 24 left which should take
me 8 days to complete.

##Notes

Git comes with a move function so that git notices that you have moved your file and continues to track it.
Below is the example code given from the book of how to perform a git move.
```bash
$ git mv functional_tests.py functional_tests/tests.py
$ git status # shows the rename to functional_tests/tests.py and __init__.py
```
