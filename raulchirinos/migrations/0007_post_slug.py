# Generated by Django 2.0.4 on 2018-05-06 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raulchirinos', '0006_auto_20180506_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=500, unique=True),
        ),
    ]
