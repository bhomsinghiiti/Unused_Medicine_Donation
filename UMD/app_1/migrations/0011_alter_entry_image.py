# Generated by Django 4.0.3 on 2022-04-11 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0010_alter_entry_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='image',
            field=models.ImageField(upload_to='profile/images'),
        ),
    ]