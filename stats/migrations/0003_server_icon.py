# Generated by Django 3.2.6 on 2021-11-20 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0002_server'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='icon',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
