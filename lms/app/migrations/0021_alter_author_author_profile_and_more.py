# Generated by Django 4.2 on 2023-05-02 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_alter_author_author_profile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='author_profile',
            field=models.ImageField(upload_to='author'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='featured_image',
            field=models.ImageField(null=True, upload_to='featured_img'),
        ),
    ]