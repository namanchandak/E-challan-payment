# Generated by Django 3.2 on 2023-08-16 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challan_app', '0003_auto_20230816_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challan',
            name='Challan_number',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='challan',
            name='Payment_status',
            field=models.BooleanField(default=False),
        ),
    ]
