# Generated by Django 3.0.5 on 2020-05-20 18:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20200510_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='uploaded_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 20, 18, 25, 7, 373970, tzinfo=utc)),
        ),
    ]