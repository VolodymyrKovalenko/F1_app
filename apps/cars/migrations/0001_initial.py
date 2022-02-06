# Generated by Django 4.0.2 on 2022-02-06 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('drivers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=64)),
                ('company', models.CharField(max_length=54)),
                ('model', models.CharField(max_length=64)),
                ('creation_date', models.DateField()),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='drivers.driver')),
            ],
        ),
    ]
