# warehouse-management-system

This is an educational project. The goal is to create an application for warehouse management.

Local deployment of Django project:

1. Install virtual environment on computer

`pip3 install virtualenv`

2. Create virtual environment for the project (On macOS or Linux)

`python3 -m venv [environment-name]`

3. Activate virtual environment

`source [environment-name]/bin/activate`

4. Install project dependencies on virtual environment from requirements.txt

`pip install -r requirements.txt`

5. Deactivate env

`deactivate`

Every time while working on the project repeat step 3 and 5. Make all the installations inside of virtual environment.

Useful commands:

Create a project:
`django-admin startproject [project-name]`

Create an application:
`python3 manage.py startapp [application-name]`
or
`django-admin startapp [application-name]`

Create superuser of admin site:
`python3 manage.py createsuperuser`

Run server:
`python3 manage.py runserver`
