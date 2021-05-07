# Generated by Django 3.0.2 on 2021-05-07 08:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yakuri', '0002_auto_20210505_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='target',
            name='targetsnum',
            field=models.IntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(35)], verbose_name='作用点表示順'),
        ),
        migrations.AddField(
            model_name='work',
            name='worknum',
            field=models.IntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MinValueValidator(15)], verbose_name='作用分類の順序'),
        ),
        migrations.AlterField(
            model_name='fields',
            name='fieldsnum',
            field=models.IntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(35)], verbose_name='目次順番'),
        ),
    ]