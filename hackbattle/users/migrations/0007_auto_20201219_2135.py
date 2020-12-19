# Generated by Django 3.1.4 on 2020-12-19 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20201219_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientrecord',
            name='xray',
            field=models.ImageField(null=True, upload_to='report_pics'),
        ),
        migrations.AlterField(
            model_name='patientrecord',
            name='ct_scan',
            field=models.ImageField(null=True, upload_to='report_pics'),
        ),
        migrations.AlterField(
            model_name='patientrecord',
            name='symptom2',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='patientrecord',
            name='symptom3',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='patientrecord',
            name='symptom4',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
