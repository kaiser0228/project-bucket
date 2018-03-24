# Generated by Django 2.0.3 on 2018-03-24 22:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listitem',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 24, 22, 5, 32, 587293, tzinfo=utc), verbose_name='published date'),
        ),
        migrations.AlterField(
            model_name='listitem',
            name='votes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
