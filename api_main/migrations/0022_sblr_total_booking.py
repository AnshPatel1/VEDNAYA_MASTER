# Generated by Django 3.2.7 on 2022-02-09 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_main', '0021_auto_20220204_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='sblr',
            name='total_booking',
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
    ]
