# Generated by Django 4.2.2 on 2023-07-01 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='author',
            field=models.CharField(default='введите имя', max_length=255),
        ),
    ]
