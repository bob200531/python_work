# Generated by Django 4.2.2 on 2023-07-25 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_vacancy_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='skills',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.skill'),
        ),
    ]
