# Generated by Django 2.0.3 on 2018-04-06 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design_school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='name',
            field=models.CharField(blank=True, default='-', max_length=20),
        ),
    ]