# Generated by Django 3.0.5 on 2020-12-20 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20201220_0001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='accepted',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='date_of_appt',
        ),
    ]
