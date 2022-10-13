# Generated by Django 4.0.3 on 2022-10-12 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_rename_boday_tweet_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='body',
            field=models.TextField(max_length=300, verbose_name='body'),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='likes',
            field=models.PositiveIntegerField(default=0, verbose_name='likes'),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='name',
            field=models.CharField(max_length=30, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='updated_at'),
        ),
    ]
