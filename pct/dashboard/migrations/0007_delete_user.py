# Generated by Django 5.0.3 on 2024-03-30 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_rename_user1_user'),
        ('main', '0014_alter_booking_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
