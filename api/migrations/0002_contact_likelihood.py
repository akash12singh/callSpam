# Generated by Django 4.2.13 on 2024-06-09 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='likelihood',
            field=models.FloatField(default=0.0),
        ),
    ]
