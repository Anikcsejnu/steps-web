# Generated by Django 3.0.5 on 2020-05-02 07:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0010_auto_20200502_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='uploaded_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 2, 7, 40, 4, 371702, tzinfo=utc)),
        ),
    ]