# Generated by Django 3.2.7 on 2021-10-04 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aroundMe', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AlterField(
            model_name='post',
            name='latitud',
            field=models.FloatField(default=-33.4569),
        ),
        migrations.AlterField(
            model_name='post',
            name='longitud',
            field=models.FloatField(default=-70.6483),
        ),
    ]
