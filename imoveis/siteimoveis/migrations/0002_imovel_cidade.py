# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 01:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteimoveis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imovel',
            name='cidade',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
