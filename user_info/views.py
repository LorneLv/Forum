# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
import  re
from hashlib import sha1
from models import *
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
def register(request):
    return  render(request,'register/register.html',{'title':'Color论坛注册会员'})
def register_hand(request):
    post = request.POST
    username = post.get('xing')
    user_email = post.get('email')
    user_remail = post.get('remail')
    user_password = post.get('password')
    # if not all([username, user_password, user_email,user_remail],):
    #     return render(request, 'register/register.html', {'errmsg': '数据不完整'})
    if re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', str(user_email)):
        if user_email ==user_remail:
            try:
                user = userInfo.objects.get(email=user_email)
            except userInfo.DoesNotExist:
                # 邮箱不存在
                user = None
            if user:
                # 邮箱已存在
                return render(request, 'register/register.html', {'errmsg': '邮箱已存在'})
            s1 = sha1()
            s1.update(user_password)
            password = s1.hexdigest()
            user = userInfo()
            user.username = username
            user.password = password
            user.email = user_email
            user.save()
            return redirect('/login/', )
        else:
            return render(request, 'register/register.html', {'errmsg': '两次输入的邮箱不一致'})

    else:
        return render(request, 'register/register.html', {'errmsg': '邮箱格式不正确'})



def index(request):
    try:
        if request.session['user_email']:
            return render(request, 'index/index2.html',{'title':'Color论坛2018引领时尚潮流'} )
        else:
            return render(request, 'index/index.html',{'title':'Color论坛2018引领时尚潮流'})
    except:
        return render(request, 'index/index.html',{'title':'Color论坛2018引领时尚潮流'})


def index_read(request):
    try:
        if request.session['user_email']:
            return render(request, 'index/index2.html',{'title':'Color论坛2018引领时尚潮流'} )
        else:
            return render(request, 'index/login.html', )
    except:
        return render(request, 'index/login.html', )
def index_hand(request):
    del request.session['user_email']
    return render(request, 'index/login.html', )
def login(request):
    return render(request, 'index/login.html',{'title':'登录Color论坛'})

def login_hand(request):
    post = request.POST
    email = post.get('email')
    password = post.get("password")
    jizhu =post.get("jizhu",0)
    users = userInfo.objects.filter(email=email)
    if len(users)==1:
        s1 = sha1()
        s1.update(password)
        if s1.hexdigest()==users[0].password:
            red = HttpResponseRedirect('/index/')
            if jizhu !=0:
                red.set_cookie('user_email',email)
            else:
                red.set_cookie('user_email','',max_age=-1)
            request.session['user_id'] =users[0].id
            request.session['user_email'] = email
            return red
        else:
            context = {'error_email':0,'error_pwd':1,'user_email':email,'pwd':password}
            return render(request, 'index/login.html', context)
    else:
        context = { 'error_email': 1, 'error_pwd': 0, 'user_email': email, 'pwd': password}
        return render(request, 'index/login.html', context)


def list(request):
    # try:
    #     if request.session['user_email']:
            post = postreply.objects.order_by("postreply_create_time")
            # post = postreply.objects.all()
            # post_new = post.posttheme.id
            # postre = postreply.objects.filter(postreply.username__posttheme.username__='rolid')
            # postint = len(post)
            # post_n = userInfo.objects.all()()
            # for  i in  range(0,len(post)):
            # email = post[i].email
            # if email == post_n[i].email
            # email ='1029159035@qq.com'
            # posttitle = post[i].titlename
            # postimg = post[i].imgaddress
            # posttime = post[i].create_time
            # postreply = post[i].reply_email
            # content = {'posttitle':posttitle,'postimg':postimg,'posttime':posttime,'postreply':postreply}
            # postname = post_n[0].username
            return render(request, 'forum_list/list2.html',{'post':post})
    #     else:
    #         return render(request, 'forum_list/list.html', {'title': '您好这里是列表页'})
    # except:
    #     return render(request, 'forum_list/list.html', {'title': '您好这里是列表页'})

def discuss(request):
    try:
        if request.session['user_email']:
            post = postreply.objects.order_by("postreply_create_time")

            return render(request, 'forum_discuss/discusis2.html', {'title': '您好这里是讨论页','post':post})
        else:
            return render(request, 'forum_discuss/discuss.html', {'title': '您好这里是讨论页'})
    except:
        return render(request, 'forum_discuss/discuss.html', {'title': '您好这里是讨论页'})

