# Generated by Django 3.2.8 on 2022-03-05 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardmember',
            name='archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cardcomment',
            name='archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cardmember',
            name='archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='referral',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]