# Generated by Django 3.2 on 2023-08-17 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challan_app', '0004_auto_20230816_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challan',
            name='Offense_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='challan',
            name='Offense_time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
