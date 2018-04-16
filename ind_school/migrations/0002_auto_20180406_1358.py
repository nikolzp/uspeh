# Generated by Django 2.0.3 on 2018-04-06 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ind_school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inddetails',
            name='des_hours',
            field=models.CharField(default='-', max_length=40, null=True, verbose_name='Желательное кол ак/часов'),
        ),
        migrations.AlterField(
            model_name='inddetails',
            name='price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Цена за ак/ч'),
        ),
        migrations.AlterField(
            model_name='inddetails',
            name='title',
            field=models.CharField(default='-', max_length=60, null=True, verbose_name='Название курса'),
        ),
    ]