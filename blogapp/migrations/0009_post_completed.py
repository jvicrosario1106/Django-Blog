# Generated by Django 3.0.8 on 2020-07-24 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0008_auto_20200723_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
