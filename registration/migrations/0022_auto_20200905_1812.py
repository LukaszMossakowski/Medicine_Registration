# Generated by Django 3.1 on 2020-09-05 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0021_auto_20200905_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='term',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.term', verbose_name='related appointment'),
        ),
    ]
