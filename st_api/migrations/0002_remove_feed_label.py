# Generated by Django 2.0.2 on 2018-02-24 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('st_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='label',
        ),
    ]