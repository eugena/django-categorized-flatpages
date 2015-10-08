#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-categorized-flatpages
------------

Tests for `django-categorized-flatpages` admin module.
"""

from django.conf import settings
from django.test import TestCase
from django.test.utils import override_settings
from django.contrib.admin.sites import AdminSite

from cflatpages import models, admin

class MockRequest(object):
    pass

request = MockRequest()


class TestCflatpagesAdmin(TestCase):

    def setUp(self):
        self.site = AdminSite()

    def test_category_admin(self):
        """
        Category admin
        """
        self.assertIsNone(
            self.site.register(models.Category, admin.CategoryAdmin))

    def test_page_admin(self):
        """
        Page admin
        """
        self.assertIsNone(
            self.site.register(models.CFlatPage, admin.CategorizedFlatPageAdmin))

    @override_settings()
    def test_page_settings_admin(self):
        """
        Page admin
        """
        settings.INSTALLED_APPS = settings.INSTALLED_APPS + [
            "ckeditor",
        ]
        self.assertIsNone(
            self.site.register(models.CFlatPage, admin.CategorizedFlatPageAdmin))

    def tearDown(self):
        pass
