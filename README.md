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