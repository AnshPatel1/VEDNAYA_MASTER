# Generated by Django 3.2.7 on 2022-02-10 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_main', '0022_sblr_total_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='sblr',
            name='summary',
            field=models.TextField(default='unset'),
            preserve_default=False,
        ),
    ]