# Generated by Django 2.1.2 on 2018-12-03 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bbc', '0008_auto_20181130_1106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='news_likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='likes',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbc.News'),
        ),
        migrations.AddField(
            model_name='likes',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbc.Users'),
        ),
    ]
