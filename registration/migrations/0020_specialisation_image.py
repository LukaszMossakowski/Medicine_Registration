# Generated by Django 3.1 on 2020-08-30 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0019_auto_20200830_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialisation',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='specialisation/'),
        ),
    ]
