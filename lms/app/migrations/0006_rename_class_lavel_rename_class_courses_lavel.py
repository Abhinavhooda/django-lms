# Generated by Django 4.2 on 2023-04-19 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_class_courses_class'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Class',
            new_name='Lavel',
        ),
        migrations.RenameField(
            model_name='courses',
            old_name='Class',
            new_name='Lavel',
        ),
    ]
