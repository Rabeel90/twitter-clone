# Generated by Django 4.0.3 on 2022-10-12 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0003_alter_tweet_body_alter_tweet_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='likes',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='likes'),
        ),
    ]
