## Introduction

this package helps to integrate [playmobile.uz](http://playmobile.uz) and your application is built on [django](https://www.djangoproject.com/).

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

```bash
pip install requests
pip install djangorestframework
pip install playmobile
```

## Usage

```python
# settings.py

INSTALLED_APPS = [
     ... 
    'playmobile',
    'rest_framework',
     ...
]

PLAY_MOBILE_SETTINGS = {
    'API_URL': '',
    'LOGIN': '',
    'PASSWORD': '',
    'PREFIX': '',     # example : abc - Organization name. no more 20 characters.
    'ORIGINATOR': ''     # if this field is empty default 3700 or set your originator name
}


## Documentation
 - playmobile.uz [docs](https://playmobile.uz/instr/Broker_API_18.11.2019.pdf)
 - django-rest-framework [docs](https://www.django-rest-framework.org/)
