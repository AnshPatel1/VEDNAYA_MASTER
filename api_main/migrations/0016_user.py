# Generated by Django 3.2.7 on 2021-10-07 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_main', '0015_auto_20211005_0923'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255, unique=True)),
                ('mso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_main.mso')),
            ],
        ),
    ]