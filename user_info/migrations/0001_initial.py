# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-19 03:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('user_status', models.CharField(default=1, max_length=1)),
                ('roleid', models.CharField(default=0, max_length=1)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('realname', models.CharField(default='', max_length=50)),
                ('address', models.CharField(default='', max_length=100)),
                ('phone', models.CharField(default='', max_length=11)),
            ],
        ),
    ]
