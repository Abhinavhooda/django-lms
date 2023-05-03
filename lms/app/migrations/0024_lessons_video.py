# Generated by Django 4.2 on 2023-05-03 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_learning_point_course_requirement_point_course_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='lessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('course', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.courses')),
            ],
        ),
        migrations.CreateModel(
            name='video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.IntegerField(null=True)),
                ('thumbnail', models.ImageField(null=True, upload_to='media/course/lessons')),
                ('title', models.CharField(max_length=200)),
                ('video_link', models.CharField(max_length=200)),
                ('time_duration', models.FloatField(null=True)),
                ('preview', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.courses')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.lessons')),
            ],
        ),
    ]