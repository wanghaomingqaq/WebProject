from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    publish_data = models.DateField(auto_now_add=True)

    publish = models.ForeignKey(to='Publish',on_delete=models.CASCADE)
    authors = models.ManyToManyField(to='Author')



class Publish(models.Model):
    name = models.CharField(max_length=32)
    addr = models.CharField(max_length=64)
    email = models.EmailField()

class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    author_detail = models.OneToOneField(to='AuthorDetail',on_delete=models.CASCADE)

class AuthorDetail(models.Model):
    phone = models.BigIntegerField()
    addr = models.CharField(max_length=64)

class QiDian(models.Model):
    rank = models.CharField(max_length=32)
    title = models.CharField(max_length=32)
    author = models.CharField(max_length=32)
    type = models.CharField(max_length=32)
    status = models.CharField(max_length=32)
    href = models.CharField(max_length=64)
class Twitter(models.Model):
    content = models.CharField(max_length=191)


class Login(models.Model):
    username = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

class Weibo(models.Model):
    user = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    url = models.CharField(max_length=256)
    content = models.TextField()
    jpg = models.CharField(max_length=256)
