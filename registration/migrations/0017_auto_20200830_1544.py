# Generated by Django 3.1 on 2020-08-30 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0016_auto_20200830_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, default='img/hero-bg.jpg', null=True, upload_to='img/'),
        ),
    ]
