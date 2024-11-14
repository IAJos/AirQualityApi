# Generated by Django 5.1.2 on 2024-11-11 17:55

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('mode', models.IntegerField(choices=[(1, 'Manual'), (2, 'Automatic')], null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=20, null=True)),
                ('password', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantityCO2', models.IntegerField(null=True)),
                ('quantityCO', models.IntegerField(null=True)),
                ('quantityNO2', models.IntegerField(null=True)),
                ('quantityO3', models.IntegerField(null=True)),
                ('fine_particle', models.IntegerField(null=True)),
                ('temperature', models.FloatField(null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('device_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.device', to_field='name')),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='User',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.user'),
        ),
    ]
