# Generated by Django 5.0.3 on 2024-03-28 14:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_user'),
        ('main', '0005_alter_booking_show'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='show',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_show', to='dashboard.show'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='booking_show', to=settings.AUTH_USER_MODEL),
        ),
    ]
