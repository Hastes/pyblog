# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-22 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160608_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_author',
            field=models.CharField(max_length=200, verbose_name='Ваше имя'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.TextField(verbose_name='Текст'),
        ),
    ]
