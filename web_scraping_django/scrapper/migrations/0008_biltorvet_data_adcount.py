# Generated by Django 3.2.6 on 2022-11-01 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper', '0007_bilbasen_data_biltorvet_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='biltorvet_data',
            name='adCount',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
