# Generated by Django 4.2 on 2023-04-19 05:17

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_level_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='name', unique=True),
        ),
        migrations.AlterField(
            model_name='courses',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='title', unique=True),
        ),
    ]
