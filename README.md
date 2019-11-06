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

- Chapter 7
- Location on Page: "What to Functionally Test About Layout and Style" down by the first functional test run
- [Link to Current Position](https://www.obeythetestinggoat.com/book/chapter_prettification.html#_using_bootstrap_components_to_improve_the_look_of_the_site)
- [Github Repo](https://github.com/hjwp/book-example/)

## TODO List

-[x] Don't save blank items for every request
-[x] Code smell: POST test is too long?
-[x] Display multiple item sin the table
-[x] Clean up after FT runs
-[x] Remove time.sleeps
-[x] Support more than one list
-[x] Adjust model so that items are associated with different lists
-[x] Add unique URLs for each list
-[x] Add a URL for creating a new list via POST
-[x] Add URLs for adding a new item to an existing list via post
-[ ] Refactor away some duplication in urls.py

###SCHEDULE

- Complete 3 chapters a day, 26 chapters in total: Completed two the first day. So there are 24 left which should take
me 8 days to complete.

##Notes


### GIT Notes
#### Git Move
Git comes with a move function so that git notices that you have moved your file and continues to track it.
Below is the example code given from the book of how to perform a git move.
```bash
$ git mv functional_tests.py functional_tests/tests.py
$ git status # shows the rename to functional_tests/tests.py and __init__.py
```

#### Git diff

"The -M flag on the git diff is a useful one. It means "detect moves", so it will notice that functional_tests.py and 
functional_tests/tests.py are the same file, and show you a more sensible diff"
[Link to site page where I got the quote](https://www.obeythetestinggoat.com/book/chapter_explicit_waits_1.html)
```bash
$ git status # functional_tests.py renamed + modified, new __init__.py
$ git add functional_tests
$ git diff --staged -M
$ git commit  # msg eg "make functional_tests an app, use LiveServerTestCase"
```
