# Generated by Django 2.0.7 on 2018-07-10 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0002_auto_20180702_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='buswd',
            name='institute',
            field=models.CharField(default='LNMIIT', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buswe',
            name='institute',
            field=models.CharField(default='LNMIIT', max_length=256),
            preserve_default=False,
        ),
    ]