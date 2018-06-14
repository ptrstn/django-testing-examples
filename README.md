[![Build Status](https://travis-ci.com/ptrstn/django-testing-examples.svg?branch=master)](https://travis-ci.com/ptrstn/django-testing-examples)
[![codecov](https://codecov.io/gh/ptrstn/django-testing-examples/branch/master/graph/badge.svg)](https://codecov.io/gh/ptrstn/django-testing-examples)
# Django Testing Examples

### Test this repository
```bash
git clone https://github.com/ptrstn/django-testing-examples.git
cd django-testing-examples
python -m venv venv
source venv/bin/activate
pip install django==1.11
pip install -r testing-requirements.txt
pytest
```

### Generate HTML coverage report
```bash
pytest --cov=. --cov-report=html
chromium htmlcov/index.html
```

### Test for Deprecation Warnings
If you want to upgrade from Django 1.11 to Django 2.0 you need to make sure that there are no DeprecationWarnings:
```bash
PYTHONWARNINGS=all pytest
# or
python -Wall manage.py test
```

### How this project was created
```bash
mkdir django-testing-examples
cd django-testing-examples
python -m venv venv
source venv/bin/activate
pip install -I django==1.11
git init
wget "https://www.gitignore.io/api/django%2Cpython%2Cpycharm%2Ball" -O .gitignore
django-admin startproject django_testing_examples .
python manage.py startapp myapp
python manage.py migrate
```