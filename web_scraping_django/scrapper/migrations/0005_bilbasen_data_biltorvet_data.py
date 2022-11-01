# Generated by Django 3.2.6 on 2022-11-01 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('scrapper', '0004_auto_20221101_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bilbasen_data',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=200)),
                ('Address', models.CharField(max_length=200)),
                ('Phone', models.CharField(max_length=200)),
                ('Fax', models.CharField(max_length=200)),
                ('Number_of_listings', models.IntegerField()),
                ('Web_Link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Biltorvet_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('zipAndCity', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
            ],
        ),
    ]
