# Generated by Django 3.2.8 on 2021-11-01 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_auto_20211102_0835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='color',
            new_name='theme',
        ),
    ]
