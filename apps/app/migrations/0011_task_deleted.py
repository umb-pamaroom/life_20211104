# Generated by Django 3.2.8 on 2023-01-14 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_timelinemodel_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
