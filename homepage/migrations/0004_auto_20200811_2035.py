# Generated by Django 3.1 on 2020-08-11 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20200806_1935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='body',
        ),
        migrations.AddField(
            model_name='recipe',
            name='time_required',
            field=models.CharField(default='', max_length=24),
        ),
    ]
