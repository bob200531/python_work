# Generated by Django 4.2.2 on 2023-06-23 13:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('worker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workers',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='workers',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Имя'),
        ),
    ]