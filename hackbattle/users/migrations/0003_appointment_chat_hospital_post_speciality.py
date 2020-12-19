# Generated by Django 3.0.5 on 2020-12-19 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_patientrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=100)),
                ('description', models.TextField(default='Welcome!', max_length=400)),
                ('image', models.ImageField(default='default.jpg', upload_to='hospital_pics')),
                ('phone_no', models.CharField(default=None, max_length=15)),
                ('rating', models.IntegerField(default=3)),
                ('huser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speciality', models.CharField(choices=[('1', 'Pediatrician'), ('2', 'Cardiologist'), ('3', 'Gynecologist'), ('4', 'Internist'), ('5', 'Dermatologist'), ('6', 'Family Medicine')], default=6, max_length=100)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(default='Patient', max_length=15)),
                ('message', models.CharField(max_length=300)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Hospital')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepted', models.BooleanField()),
                ('date_of_appt', models.DateTimeField(default=None)),
                ('hname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Hospital')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile')),
            ],
        ),
    ]