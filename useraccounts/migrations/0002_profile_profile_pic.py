# Generated by Django 3.2 on 2021-05-06 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
