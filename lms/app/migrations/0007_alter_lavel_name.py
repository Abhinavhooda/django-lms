# Generated by Django 4.2 on 2023-04-19 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_class_lavel_rename_class_courses_lavel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lavel',
            name='name',
            field=models.CharField(max_length=3),
        ),
    ]
