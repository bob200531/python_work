# Generated by Django 4.2.2 on 2023-06-25 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0003_alter_workers_user_coment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('resume_text', models.TextField()),
            ],
        ),
    ]
