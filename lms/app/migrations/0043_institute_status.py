# Generated by Django 4.2 on 2023-05-08 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0042_alter_institute_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='institute',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Draft', 'Draft')], max_length=100, null=True),
        ),
    ]
