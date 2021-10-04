# Generated by Django 3.2.7 on 2021-10-04 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0007_doctor_mso'),
    ]

    operations = [
        migrations.CreateModel(
            name='HQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('pincode', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='mso',
            name='Connected Doctors',
            field=models.ManyToManyField(to='api_app.Doctor'),
        ),
        migrations.AddField(
            model_name='mso',
            name='HQ',
            field=models.CharField(default='NULL', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mso',
            name='Territory',
            field=models.CharField(default='NULL', max_length=255),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Chemist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Chemist Name', models.CharField(max_length=255)),
                ('Person in Charge', models.CharField(max_length=255)),
                ('Business Type', models.CharField(choices=[('RETAIL', 'Retail'), ('WHOLESALE', 'Wholesale'), ('BOTH', 'Both')], max_length=255)),
                ('Products Under Support', models.ManyToManyField(to='api_app.Product')),
                ('Select Sitting Doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_app.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='ARC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Retailer Name', models.CharField(max_length=255)),
                ('Person in Charge', models.CharField(max_length=255)),
                ('Business Type', models.CharField(choices=[('RETAIL', 'Retail'), ('WHOLESALE', 'Wholesale'), ('BOTH', 'Both')], max_length=255)),
                ('Products Under Support', models.ManyToManyField(to='api_app.Product')),
                ('Select Sitting Doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_app.doctor')),
            ],
        ),
        migrations.AddField(
            model_name='mso',
            name='Connected ARCs',
            field=models.ManyToManyField(to='api_app.ARC'),
        ),
        migrations.AddField(
            model_name='mso',
            name='Connected Chemists',
            field=models.ManyToManyField(to='api_app.Chemist'),
        ),
        migrations.AlterField(
            model_name='mso',
            name='Name',
            field=models.ForeignKey(default='N/A', on_delete=django.db.models.deletion.CASCADE, to='api_app.hq'),
        ),
    ]
