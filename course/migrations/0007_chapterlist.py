# Generated by Django 2.1.8 on 2020-04-20 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_auto_20200419_1944'),
    ]

    operations = [
        migrations.CreateModel(
            name='chapterlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameOfChapters', models.CharField(max_length=100)),
                ('nameOfCourse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
        ),
    ]