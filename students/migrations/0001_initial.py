# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-13 22:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('student_class', models.IntegerField()),
                ('student_age', models.CharField(max_length=20)),
                ('principal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Principal')),
            ],
        ),
    ]
