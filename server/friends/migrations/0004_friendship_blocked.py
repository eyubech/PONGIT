# Generated by Django 4.2.16 on 2024-12-21 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0003_remove_friendship_blocked_friendship_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendship',
            name='blocked',
            field=models.BooleanField(default=False),
        ),
    ]
