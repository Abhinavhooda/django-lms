# Generated by Django 4.2 on 2023-05-03 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_learning_point_requirement_point_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='learning_point',
            name='course',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.courses'),
        ),
        migrations.AddField(
            model_name='requirement_point',
            name='course',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.courses'),
        ),
        migrations.AlterField(
            model_name='learning_point',
            name='points',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='requirement_point',
            name='points',
            field=models.CharField(default=None, max_length=500),
        ),
    ]
