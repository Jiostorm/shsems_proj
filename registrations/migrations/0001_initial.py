# Generated by Django 2.0 on 2018-11-16 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parents_permit', models.FileField(default='', upload_to='uploads/permits/', verbose_name="Parent's Permit")),
                ('parents_contact_number', models.CharField(max_length=50, verbose_name="Parent's Contact Number")),
                ('waiver', models.FileField(default='', upload_to='uploads/waivers/', verbose_name='Waiver')),
                ('date_registered', models.DateTimeField(auto_now_add=True, verbose_name='Date/Time Registered')),
                ('status', models.CharField(default='Approved', max_length=15, verbose_name='Status')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
            ],
        ),
    ]
