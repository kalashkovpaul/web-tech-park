# Generated by Django 3.2.9 on 2021-12-10 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20211125_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_id',
            field=models.IntegerField(default=0),
        ),
    ]