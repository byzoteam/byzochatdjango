# Generated by Django 3.2.8 on 2024-06-24 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=250)),
                ('message', models.TextField(blank=True, null=True)),
                ('role', models.CharField(default='user', max_length=250)),
                ('message_type', models.CharField(default='text', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('seen', models.BooleanField(default=False)),
                ('seen_time_stamp', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=250)),
                ('is_unread_user', models.BooleanField(default=False)),
                ('is_unread_admin', models.BooleanField(default=False)),
                ('is_user_active', models.BooleanField(default=False)),
                ('is_admin_active', models.BooleanField(default=False)),
                ('user_lastactive', models.DateTimeField(blank=True, null=True)),
                ('admin_lastactive', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
