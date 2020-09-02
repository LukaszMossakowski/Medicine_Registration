# Generated by Django 3.1 on 2020-08-21 15:11

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medical_title', models.CharField(max_length=64, verbose_name='medical title')),
                ('first_name', models.CharField(max_length=64, verbose_name='Name')),
                ('last_name', models.CharField(max_length=64, verbose_name='Surname')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Name role')),
            ],
        ),
        migrations.CreateModel(
            name='Specialisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialisation', models.CharField(max_length=64, verbose_name='Name specialisation')),
                ('description', models.TextField(verbose_name='Describe specialisation')),
            ],
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date(2020, 8, 21), verbose_name='Determine date of term (in YYYY-MM-DD form):')),
                ('time_from', models.TimeField(default=datetime.time(8, 0), verbose_name='Determine beginning time (in format HH:MM)')),
                ('time_to', models.TimeField(default=datetime.time(8, 0), verbose_name='Determine ending time (in format HH:MM)')),
                ('status', models.CharField(default='unreserved', max_length=64)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.doctor', verbose_name='Select doctor')),
                ('user', models.ManyToManyField(through='registration.Appointment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialisation',
            field=models.ManyToManyField(to='registration.Specialisation'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='visit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.term'),
        ),
    ]
