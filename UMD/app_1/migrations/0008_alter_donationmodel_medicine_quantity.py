# Generated by Django 4.0.3 on 2022-04-11 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0007_donationmodel_phone_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationmodel',
            name='medicine_quantity',
            field=models.CharField(default='0', max_length=300),
        ),
    ]
