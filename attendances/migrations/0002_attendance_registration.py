# Generated by Django 2.0 on 2018-11-16 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registrations', '0001_initial'),
        ('attendances', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='registration',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registrations.Registration'),
        ),
    ]
