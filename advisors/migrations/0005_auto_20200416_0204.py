# Generated by Django 2.2.6 on 2020-04-16 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advisors', '0004_auto_20200415_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advisor',
            name='phone',
            field=models.CharField(max_length=100),
        ),
    ]