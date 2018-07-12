# Generated by Django 2.0.6 on 2018-07-02 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=256)),
                ('LT', models.CharField(max_length=256)),
                ('slotstart', models.TimeField()),
                ('slotend', models.TimeField()),
                ('section', models.CharField(max_length=256)),
                ('teacher', models.CharField(max_length=256)),
                ('subject', models.CharField(max_length=256)),
            ],
        ),
    ]