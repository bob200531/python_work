# Generated by Django 4.2.2 on 2023-07-27 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0009_alter_resume_contacts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='contacts',
            field=models.IntegerField(null=True, verbose_name='контакты'),
        ),
    ]
