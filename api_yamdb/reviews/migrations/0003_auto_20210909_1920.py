# Generated by Django 2.2.16 on 2021-09-09 19:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_title_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True, validators=[django.core.validators.RegexValidator(message='Только Буквы И Цифры!', regex='^[-a-zA-Z0-9_]+$')]),
        ),
    ]