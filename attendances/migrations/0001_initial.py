# Generated by Django 2.0 on 2018-11-16 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registrations', '0002_auto_20181024_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('for_date', models.DateField(null=True, verbose_name='For Date')),
                ('time_arrived', models.TimeField(null=True, verbose_name='Time Arrived')),
                ('time_left', models.TimeField(null=True, verbose_name='Time Left')),
                ('registration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registrations.Registration')),
            ],
        ),
    ]
