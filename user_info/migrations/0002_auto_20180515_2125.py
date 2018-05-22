# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-15 13:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='postreply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postreply_comm', models.TextField()),
                ('postreply_username', models.CharField(max_length=20)),
                ('postreply_email', models.EmailField(max_length=50)),
                ('postreply_imgaddress', models.CharField(max_length=255)),
                ('postreply_create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='posttheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posttitlename', models.CharField(max_length=255)),
                ('posttheme_username', models.CharField(max_length=20)),
                ('posttheme_email', models.EmailField(max_length=50)),
                ('posttheme_imgaddress', models.CharField(max_length=255)),
                ('posttheme_address', models.CharField(max_length=255)),
                ('posttheme_roleid', models.CharField(default=0, max_length=1)),
                ('posttheme_mode', models.CharField(default='qicaiFish', max_length=20)),
                ('posttheme_comm', models.TextField()),
                ('posttheme_status', models.CharField(default=0, max_length=1)),
                ('posttheme_create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='postreply',
            name='posttheme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_info.posttheme'),
        ),
    ]
