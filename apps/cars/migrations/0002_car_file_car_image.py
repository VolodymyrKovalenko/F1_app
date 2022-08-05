# Generated by Django 4.0.2 on 2022-08-01 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='cars_files/'),
        ),
        migrations.AddField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='car_images/'),
        ),
    ]