# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('flatpages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('slug', models.SlugField(unique=True, max_length=60, verbose_name='slug')),
                ('description', models.CharField(max_length=255, null=True, verbose_name='description', blank=True)),
                ('text', models.TextField(null=True, verbose_name='text', blank=True)),
                ('num', models.PositiveSmallIntegerField(default=1, verbose_name='order number')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', verbose_name='parent', blank=True, to='cflatpages.Category', null=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='CFlatPage',
            fields=[
                ('flatpage_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='flatpages.FlatPage')),
                ('keywords', models.CharField(max_length=255, verbose_name='keywords', blank=True)),
                ('description', models.CharField(max_length=100, verbose_name='description', blank=True)),
                ('category', mptt.fields.TreeForeignKey(related_name='page', verbose_name='category', to='cflatpages.Category')),
            ],
            options={
                'verbose_name': 'categorized flatpage',
                'verbose_name_plural': 'categorized flatpages',
            },
            bases=('flatpages.flatpage',),
        ),
    ]
