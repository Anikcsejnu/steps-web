# Generated by Django 2.1.8 on 2020-04-19 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='dept',
            field=models.CharField(choices=[('Science', 'SCIENCE'), ('business studies', 'BUSINESS STUDIES'), ('english', 'ENGLISH'), ('ict', 'ICT')], default='science', max_length=100),
        ),
    ]