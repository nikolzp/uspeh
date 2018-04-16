from django.db import models
from django.urls import reverse


class Coach(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True, default='-')
    surname = models.CharField(max_length=20, null=True, blank=True, default='-')
    phone = models.CharField(max_length=15, null=True, blank=True, default='-')
    description = models.TextField(null=True, blank=True, default='-')

    def __str__(self):
        return self.surname


class IndDetails(models.Model):
    title = models.CharField(max_length=60, null=True, default='-', verbose_name='Название курса')
    coach = models.ManyToManyField("Coach", blank=True, null=True, default='-', related_name='coachs', verbose_name='Преподаватель')
    price = models.IntegerField(null=True, blank=True, default=0, verbose_name='Цена за ак/ч')
    des_hours = models.CharField(max_length=40, null=True, default='-', verbose_name='Желательное кол ак/часов')

    def __str__(self):
        info = '{} || || {}'.format(self.title, self.price)
        return info

    def get_absolute_url(self):
        return reverse('ind_school_detail')
