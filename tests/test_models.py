#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-categorized-flatpages
------------

Tests for `django-categorized-flatpages` models module.
"""

from django.test import TestCase

from cflatpages import models


class TestCflatpages(TestCase):

    def setUp(self):
        pass

    def test_category(self):
        """
        Category model
        """
        category = models.Category.objects.create(
            title='foo',
            slug='foo',
            pk=1)

        self.assertTrue(category.__str__(), 'foo')

    def test_flatpage(self):
        """
        Flatpage model
        """
        category = models.Category.objects.create(
            title='foo',
            slug='foo',
            pk=1)

        page = models.CFlatPage.objects.create(
            title='foo',
            keywords='foo',
            category=category, )

        self.assertTrue(page.__str__(), 'foo')

    def tearDown(self):
        pass
