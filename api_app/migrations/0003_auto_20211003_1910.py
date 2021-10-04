# Generated by Django 3.2.7 on 2021-10-03 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0002_article_publication'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('capsule', 'oil'), ('syrup', 'tablet')], max_length=255),
        ),
    ]
