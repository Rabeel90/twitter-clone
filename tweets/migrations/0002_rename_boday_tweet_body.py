# Generated by Django 4.1.2 on 2022-10-06 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='boday',
            new_name='body',
        ),
    ]