# Generated by Django 4.2 on 2023-05-03 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_alter_video_time_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='author_role',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
    ]
