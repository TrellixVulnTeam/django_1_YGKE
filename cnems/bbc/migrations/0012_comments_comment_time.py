# Generated by Django 2.1.2 on 2018-12-05 01:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bbc', '0011_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comment_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
