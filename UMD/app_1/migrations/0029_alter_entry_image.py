# Generated by Django 4.0.3 on 2022-04-13 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0028_alter_entry_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='image',
            field=models.FileField(blank=True, default='/static/defaultStatus.png', null=True, upload_to=''),
        ),
    ]
