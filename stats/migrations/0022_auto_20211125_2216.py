# Generated by Django 3.2.6 on 2021-11-25 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0021_alter_vip_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vip',
            name='active',
        ),
        migrations.RemoveField(
            model_name='vip',
            name='discord_id',
        ),
        migrations.RemoveField(
            model_name='vip',
            name='profile_url',
        ),
    ]