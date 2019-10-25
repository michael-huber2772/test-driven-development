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

## Adding an APP to the project
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
- Location on Page: "A Little More of Our Front Page"
- [Link to Current Position](https://www.obeythetestinggoat.com/book/chapter_philosophy_and_refactoring.html)
- [Github Repo](https://github.com/hjwp/book-example/)

###SCHEDULE

- Complete 3 chapters a day, 26 chapters in total: Completed two the first day. So there are 24 left which should take
me 8 days to complete.