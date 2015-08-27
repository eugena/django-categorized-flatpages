Django Categorized Flatpages

============================

Installing:

pip install django_categorized_flatpages

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
