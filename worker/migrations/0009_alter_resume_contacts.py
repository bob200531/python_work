# Generated by Django 4.2.2 on 2023-07-27 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0008_alter_resume_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='contacts',
            field=models.CharField(max_length=255, null=True, verbose_name='контакты'),
        ),
    ]