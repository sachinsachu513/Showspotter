# Generated by Django 5.0.3 on 2024-03-28 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='session',
        ),
        migrations.AddField(
            model_name='booking',
            name='phonenumber',
            field=models.IntegerField(default=None),
        ),
    ]
