# Generated by Django 3.2.8 on 2021-11-26 07:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimelineModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateData', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=50, verbose_name='タイムライン名')),
                ('description', models.TextField(blank=True, verbose_name='説明')),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('updated_datetime', models.DateTimeField(auto_now=True)),
                ('create_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='relate_user_timeline', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RoutineModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='タイトル')),
                ('description', models.TextField(blank=True, verbose_name='説明')),
                ('start_time', models.TimeField(verbose_name='開始時間')),
                ('end_time', models.TimeField(blank=True, null=True, verbose_name='終了時間')),
                ('category', models.CharField(blank=True, choices=[('インボックス', 'インボックス'), ('生活', '生活'), ('仕事', '仕事'), ('家族', '家族')], default='インボックス', max_length=30, verbose_name='カテゴリ')),
                ('status', models.CharField(blank=True, choices=[('過ぎています。', '過ぎています。'), ('完了', '完了'), ('対応中', '対応中'), ('未対応', '未対応')], default='未対応', max_length=30, verbose_name='ステータス')),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('updated_datetime', models.DateTimeField(auto_now=True)),
                ('create_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='relate_user_routine', to=settings.AUTH_USER_MODEL)),
                ('timeline', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='timeline_model', to='app.timelinemodel')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('complete', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='relate_user_task', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'order_with_respect_to': 'user',
            },
        ),
    ]
