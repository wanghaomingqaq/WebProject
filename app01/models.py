from django.db import models


class Login(models.Model):
    username = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)


class QiDian(models.Model):
    rank = models.CharField(max_length=32)
    title = models.CharField(max_length=32)
    author = models.CharField(max_length=32)
    type = models.CharField(max_length=32)
    status = models.CharField(max_length=32)
    href = models.CharField(max_length=64)


class Weibo(models.Model):
    user = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    url = models.CharField(max_length=256)
    content = models.TextField()
    jpg = models.CharField(max_length=256)
class Jilin(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    href = models.CharField(max_length=256)
    time = models.CharField(max_length=256)