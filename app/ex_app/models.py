from django.db import models


class Teaser(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=300)
    category = models.CharField(max_length=30)
    status_list = (
        ('paid', 'Оплачено'),
        ('failure', 'Отказ'),

    )
    author = models.CharField(max_length=64)
    status = models.CharField(max_length=50, choices=status_list, blank=True)