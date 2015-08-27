Django Categorized Flatpages
============================

[![Build Status](https://travis-ci.org/eugena/django-categorized-flatpages.svg?branch=master)](https://travis-ci.org/eugena/django-categorized-flatpages)

Installing:

```bash
pip install -e git://github.com/eugena/django-categorized-flatpages.git#egg=django_categorized_flatpages
```

In settings:

```python
INSTALLED_APPS = (
	...
	'django.contrib.sites',
    'django.contrib.flatpages',
	...
    'mptt',
    'cflatpages',
    ...
)


MIDDLEWARE_CLASSES = (
	...
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
	...
)
```
