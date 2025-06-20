# Generated by Django 5.2.1 on 2025-05-30 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('genre', models.CharField(max_length=100)),
                ('director', models.CharField(blank=True, max_length=100)),
                ('poster_url', models.URLField(blank=True)),
            ],
        ),
    ]
