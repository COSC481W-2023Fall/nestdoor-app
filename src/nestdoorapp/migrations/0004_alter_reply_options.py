# Generated by Django 4.2.6 on 2023-11-27 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nestdoorapp', '0003_userext'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reply',
            options={'ordering': ['-datetime_posted']},
        ),
    ]
