# Generated by Django 3.0.2 on 2021-05-01 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yakuri', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='subinfo',
            field=models.TextField(blank=True, null=True, verbose_name='講義内容の紹介'),
        ),
        migrations.AddConstraint(
            model_name='detail',
            constraint=models.UniqueConstraint(fields=('field', 'name'), name='field_name'),
        ),
    ]
