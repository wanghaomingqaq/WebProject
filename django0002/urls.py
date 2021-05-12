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
    path('login/', views.login),
    url(r'^$', views.register),
    path('home/',views.home,name='home'),
    path('qidian/',views.qidian,name="qidian"),
    path('refresh/',views.qidian_refresh,name="refresh"),
    path('twitter/',views.twitter,name="twitter"),
    path('weibo/',views.weibo_net,name="weibo"),
    path('hupu/',views.hupu,name="hupu"),
    path('cat/',views.cat,name ='cat'),
    path('write/',views.write,name='write'),
    path('jlu_new/',views.jlu_new),
    path('jlu/',views.jlu)

]
