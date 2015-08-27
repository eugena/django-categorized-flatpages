from setuptools import setup

setup(
    name='django-categorized-flatpages',
    version='0.1',
    packages = ['categorized_flatpages'],
    include_package_data = True,
    license='MIT',
    keywords=['django', 'flatpages', 'categories', 'mptt', ],
    description='Django categorized by mptt flatpages with SEO',
    long_description=open('README.md', 'r').read(),
    url='https://github.com/eugena/django_categorized_flatpages',
    author='Eugena Mihailikova',
    author_email='eugena.mihailikova@gmail.com',
    install_requires=[
        'django-mptt',
    ],
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
