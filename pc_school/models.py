from django.db import models
from django.urls import reverse


class Coach(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True, default='-')
    surname = models.CharField(max_length=20, null=True, blank=True, default='-')
    phone = models.CharField(max_length=15, null=True, blank=True, default='-')
    description = models.TextField(null=True, blank=True, default='-')

    def __str__(self):
        return self.surname


class PCDetail(models.Model):
    title = models.ForeignKey("PCTitle", null=True, default=True, on_delete=models.CASCADE, related_name='design_title', verbose_name='Имя курса')
    coach = models.ManyToManyField("Coach", blank=True, null=True, default='-', related_name='coachs', verbose_name='Преподаватель')
    price = models.IntegerField(null=True, blank=True, default=0, verbose_name='Цена за курс')
    price_month = models.IntegerField(null=True, blank=True, default=0, verbose_name='Цена за месяц')
    discount = models.IntegerField(null=True, blank=True, default=0, verbose_name='Скидка')
    mode = models.CharField(max_length=20, null=True, blank=True, default='-', verbose_name='Режим занятий') #режим(пон спеда)
    time_to_class = models.CharField(max_length=40, null=True, blank=True, default='-', verbose_name='Время занятий') # время занятий (18:00-20:00)
    date_to_start = models.CharField(max_length=40, null=True, blank=True, default='-', verbose_name='Дата старта занятий') #дата старта занятий
    count_students = models.IntegerField(null=True, blank=True, default=0, verbose_name='Количество записанных')

    def __str__(self):
        info = '{}грн. курс || {}грн. месяц || {} || {} || {}дата старта'.format(self.price, self.price_month,
                                                                                 self.mode,
                                                                                 self.time_to_class, self.date_to_start)
        return info

    def get_absolute_url(self):
        return reverse('pc_school_detail')


class PCTitle(models.Model):
    name_cours = models.CharField(max_length=255, default=' ', verbose_name='Название курса')
    description = models.TextField(blank=True, null=True, default=' ', verbose_name='Описание курса')

    def __str__(self):
        return self.name_cours

    def get_absolute_url(self):
        return reverse('pc_school_create_det')