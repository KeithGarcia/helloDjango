# Generated by Django 3.1 on 2020-09-10 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_author_favorites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='favorites',
            field=models.ManyToManyField(blank=True, related_name='favorites', to='homepage.Recipe'),
        ),
    ]