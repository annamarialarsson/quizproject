# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-09 09:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='quiz.Quiz'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='correct',
            field=models.PositiveIntegerField(),
        ),
    ]
