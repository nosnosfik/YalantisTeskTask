To run on a PC, must be installed:
[Python 3.10](https://www.python.org/downloads/)

#### Clone repository

git clone https://github.com/nosnosfik/YalantisTeskTask.git

#### Initial setup

+ Create a virtual environment and activate it
`python -m venv \path\to\create\new\virtual\environment`
`.\venv\Scripts\activate`

+ Install all required dependencies for Django to work
`pip install -r requirements.txt`

+ Install all migrations
`python manage.py makemigrations`
`python manage.py migrate`

+ Run project
`python manage.py runserver`