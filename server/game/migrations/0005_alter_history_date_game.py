# Generated by Django 4.2.16 on 2025-01-11 12:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_history_date_game_history_scoreplayer1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='date_game',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
