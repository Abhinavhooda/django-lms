# Generated by Django 4.2 on 2023-04-18 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='name',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
