# Generated by Django 3.1.4 on 2020-12-19 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20201219_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speciality',
            name='speciality',
            field=models.CharField(choices=[('Pediatrician', 'Pediatrician'), ('Cardiologist', 'Cardiologist'), ('Gynecologist', 'Gynecologist'), ('Internist', 'Internist'), ('Dermatologist', 'Dermatologist'), ('Family Medicine', 'Family Medicine')], default=6, max_length=100),
        ),
    ]
