# Generated by Django 3.2.7 on 2021-10-03 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_main', '0003_auto_20211003_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('CAPSULE', 'Capsule'), ('OIL', 'Oil'), ('SYRUP', 'Syrup'), ('TABLET', 'Tablet')], max_length=255),
        ),
    ]