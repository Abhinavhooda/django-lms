# Generated by Django 4.2 on 2023-04-19 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_lavel_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lavel',
            new_name='Level',
        ),
        migrations.RenameField(
            model_name='courses',
            old_name='Lavel',
            new_name='level',
        ),
    ]
