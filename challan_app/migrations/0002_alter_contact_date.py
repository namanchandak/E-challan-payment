# Generated by Django 3.2 on 2023-08-15 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challan_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Date',
            field=models.DateField(auto_now_add=True),
        ),
    ]