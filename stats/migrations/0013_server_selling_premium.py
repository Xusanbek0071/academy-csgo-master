# Generated by Django 3.2.6 on 2021-11-23 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0012_alter_server_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='selling_premium',
            field=models.BooleanField(default=True),
        ),
    ]
