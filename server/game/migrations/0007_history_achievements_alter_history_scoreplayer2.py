# Generated by Django 4.2.16 on 2025-01-11 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_alter_history_date_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='achievements',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='history',
            name='scorePlayer2',
            field=models.IntegerField(default=0),
        ),
    ]
