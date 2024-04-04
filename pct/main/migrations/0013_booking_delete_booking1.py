# Generated by Django 5.0.3 on 2024-03-30 12:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_rename_user_user1'),
        ('main', '0012_booking1_delete_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.PositiveSmallIntegerField()),
                ('phonenumber', models.IntegerField(default=None)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('row_num', models.PositiveSmallIntegerField()),
                ('col_num', models.PositiveSmallIntegerField()),
                ('status', models.IntegerField(choices=[(1, 'AVAILABLE'), (2, 'BLOCKED'), (3, 'BOOKED')], default=1)),
                ('session', models.CharField(max_length=200)),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking1_movie', to='dashboard.show')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='booking1_show', to='dashboard.user')),
            ],
            options={
                'unique_together': {('show', 'row_num', 'col_num')},
            },
        ),
        migrations.DeleteModel(
            name='booking1',
        ),
    ]