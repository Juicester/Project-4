# Generated by Django 3.0.7 on 2020-06-13 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nflanalysis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='int_against',
        ),
    ]
