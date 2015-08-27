Django Categorized Flatpages

============================

Installing:

```bash
pip install -e https://github.com/eugena/django_categorized_flatpages#egg=django_categorized_flatpages
```

In settings:

INSTALLED_APPS = (
	...
	'django.contrib.sites',
    'django.contrib.flatpages',
	...
    'mptt',
    'categorized_flatpages',
    ...
)


MIDDLEWARE_CLASSES = (
	...
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
	...
)
