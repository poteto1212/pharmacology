# Generated by Django 3.0.2 on 2021-05-08 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yakuri', '0006_detail_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='blandname',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='主な先発品名'),
        ),
    ]
