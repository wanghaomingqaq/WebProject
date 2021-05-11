"""django0002 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    url(r'^$', views.register),
    path('userlist/', views.userlist),
    path('edit_user/', views.edit_user),
    path('del_user/', views.del_user),
    path('add_file/',views.add_file),
    path('class/',views.Mylogin.as_view()),
    path('home/',views.home,name='home'),
    path('book/',views.book_list,name='book_list'),
    path('book/add/',views.book_add,name='book_add'),
    path('book/del/',views.book_del,name='book_del'),
    path('book/edit/',views.book_edit,name='book_edit'),
    path('book/author/',views.author,name='author'),
    path('study/',views.study,name="study"),
    path('trans/',views.sys_time,name="trans"),
    path('qidian/',views.qidian,name="qidian"),
    path('rank/',views.rank,name="rank"),
    path('joke/',views.joke,name="joke"),
    path('weibo/',views.weibo_net,name="weibo"),
    path('hupu/',views.hupu,name="hupu")

]
