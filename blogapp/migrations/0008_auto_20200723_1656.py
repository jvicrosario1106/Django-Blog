# Generated by Django 3.0.8 on 2020-07-23 08:56

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0007_auto_20200720_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='desc',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]