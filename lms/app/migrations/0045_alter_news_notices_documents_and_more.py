# Generated by Django 4.2 on 2023-05-08 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0044_testimonials_testi_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_notices',
            name='documents',
            field=models.FileField(blank=True, upload_to='media/News_Notices/documents'),
        ),
        migrations.AlterField(
            model_name='upcoming_events',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/events/upcoming'),
        ),
    ]
