# Generated by Django 4.2 on 2023-05-05 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0037_alter_video_time_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='time_duration',
            field=models.FloatField(),
        ),
    ]
