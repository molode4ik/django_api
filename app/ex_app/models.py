from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    money = models.IntegerField()


class Admin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Teaser(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=300)
    category = models.CharField(max_length=30)
    status_list = (
        ('paid', 'Оплачено'),
        ('failure', 'Отказ'),

    )
    author = models.ForeignKey(Author, related_name='author', on_delete=models.PROTECT)
    status = models.CharField(max_length=50, choices=status_list, blank=True)
