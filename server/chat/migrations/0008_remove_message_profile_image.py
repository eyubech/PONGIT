# Generated by Django 4.2.16 on 2025-01-06 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_message_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='profile_image',
        ),
    ]
