# Generated by Django 2.1.7 on 2019-12-01 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0077_auto_20191201_0516'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='extra_requested_matches_per_week',
            field=models.IntegerField(default=0),
        ),
    ]
