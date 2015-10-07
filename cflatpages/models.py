# -*- coding: utf-8 -*-
from django.contrib.flatpages.models import FlatPage
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Category(MPTTModel):
    """
    The model of page category
    """
    title = models.CharField(_(u'title'), max_length=100)
    slug = models.SlugField(_(u'slug'), max_length=60, unique=True)
    parent = TreeForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        verbose_name=u'parent', )
    description = models.CharField(
        _(u'description'),
        max_length=255,
        blank=True,
        null=True, )
    text = models.TextField(
        _(u'text'),
        blank=True,
        null=True, )
    num = models.PositiveSmallIntegerField(_(u'order number'), default=1, )
    created = models.DateTimeField(_(u'created'), auto_now_add=True)
    modified = models.DateTimeField(_(u'modified'), auto_now=True)

    def __str__(self):
        return self.title

    class MPTTMeta():
        order_insertion_by = ['num']

    class Meta():
        verbose_name = _(u'category')
        verbose_name_plural = _(u'categories')


@python_2_unicode_compatible
class CFlatPage(FlatPage):
    """
    The model of categorized Flatpage
    """
    keywords = models.CharField(_(u'keywords'), max_length=255, blank=True)
    description = models.CharField(_(u'description'), max_length=100, blank=True)
    category = TreeForeignKey(
        Category,
        verbose_name=_(u'category'),
        related_name='page', )

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = _(u'categorized flatpage')
        verbose_name_plural = _(u'categorized flatpages')
