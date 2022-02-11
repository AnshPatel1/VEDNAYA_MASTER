# Generated by Django 3.2.7 on 2022-02-04 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_main', '0020_doctor_connected_stockists'),
    ]

    operations = [
        migrations.AddField(
            model_name='arc',
            name='connected_stockists',
            field=models.ManyToManyField(to='api_main.Stockist'),
        ),
        migrations.AddField(
            model_name='chemist',
            name='connected_stockists',
            field=models.ManyToManyField(to='api_main.Stockist'),
        ),
    ]