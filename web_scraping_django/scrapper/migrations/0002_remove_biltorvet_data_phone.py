# Generated by Django 3.2.6 on 2022-11-01 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biltorvet_data',
            name='phone',
        ),
    ]
