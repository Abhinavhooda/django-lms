# Generated by Django 4.2 on 2023-05-05 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_alter_usercourse_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessons',
            name='description',
            field=models.TextField(default=None, null=True),
        ),
    ]
