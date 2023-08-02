from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ArticleNew(models.Model):
    author =models.OneToOneField(
        to = User,
        blank=True,
        related_name='article_new_object',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    description = models.TextField(default='Нет описания')
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)
    views_count = models.IntegerField(default=0)
    likes_users = models.ManyToManyField(
        to=User,
        blank = True,
    )