# Generated by Django 3.2 on 2021-04-28 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date_published',
            new_name='pub_date',
        ),
    ]
