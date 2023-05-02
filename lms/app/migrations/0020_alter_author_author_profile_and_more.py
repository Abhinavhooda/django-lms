# Generated by Django 4.2 on 2023-05-02 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_alter_author_author_profile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='author_profile',
            field=models.ImageField(upload_to='media/author'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='featured_image',
            field=models.ImageField(null=True, upload_to='media/featured_img'),
        ),
    ]