# Generated by Django 5.0 on 2023-12-13 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('description', models.TextField()),
                ('year', models.IntegerField()),
                ('img', models.ImageField(upload_to='projects_images/')),
                ('repository', models.URLField()),
                ('technologies', models.ManyToManyField(to='projects.technology')),
            ],
        ),
    ]
