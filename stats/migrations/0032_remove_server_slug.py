# Generated by Django 3.2.6 on 2023-04-24 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0031_auto_20230424_1057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='server',
            name='slug',
        ),
    ]