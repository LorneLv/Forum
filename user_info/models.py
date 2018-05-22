# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class userInfo(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    user_status = models.CharField(max_length=1,default=1)
    roleid = models.CharField(max_length=1,default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    realname = models.CharField(max_length=50,default='')
    address = models.CharField(max_length=100,default='')
    phone = models.CharField(max_length=11, default='')
    def __str__(self):
        return self.email.encode('utf-8')


class posttheme(models.Model):
    """创建论坛主题数据库"""
    posttitlename = models.CharField(max_length=255)
    posttheme_username = models.CharField(max_length=20)
    posttheme_email = models.EmailField(max_length=50)
    posttheme_imgaddress = models.CharField(max_length=255)
    posttheme_address = models.CharField(max_length=255)
    posttheme_roleid = models.CharField(max_length=1, default=0)
    posttheme_mode = models.CharField(max_length=20, default='qicaiFish')
    posttheme_comm = models.TextField()
    posttheme_status = models.CharField(max_length=1,default=0)
    posttheme_create_time = models.DateTimeField(auto_now_add=True)


class postreply(models.Model):
    posttheme = models.ForeignKey(posttheme)
    postreply_comm = models.TextField()
    postreply_username = models.CharField(max_length=20)
    postreply_email = models.EmailField(max_length=50)
    postreply_imgaddress = models.CharField(max_length=255)
    postreply_create_time = models.DateTimeField(auto_now_add=True)