# Generated by Django 3.0.8 on 2020-12-18 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20201219_0841'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SeasonBotMatchupStats',
            new_name='CompetitionBotMatchupStats',
        ),
    ]
