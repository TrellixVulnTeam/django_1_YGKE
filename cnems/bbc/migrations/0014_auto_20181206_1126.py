# Generated by Django 2.1.2 on 2018-12-06 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbc', '0013_auto_20181205_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_title',
            field=models.CharField(max_length=50),
        ),
    ]
