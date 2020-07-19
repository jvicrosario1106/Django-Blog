# Generated by Django 3.0.8 on 2020-07-18 08:08

import blogapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_remove_newsletter_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[blogapp.models.email_validate]),
        ),
    ]