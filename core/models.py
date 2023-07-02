from django.db import models
from worker.models import Workers
from django.contrib.auth.models import User
# Create your models here.
class Vacancy(models.Model):
    title=models.CharField(max_length=255)
    salary=models.IntegerField(null=True, blank=True)
    description=models.TextField(default='Нет описнаня')
    is_relevant=models.BooleanField(default=True)
    email=models.EmailField()
    contacts=models.CharField(max_length=100,verbose_name='контакты')
    candidates=models.ManyToManyField(
        to=Workers,
        blank=True
    )
    review=models.ManyToManyField(
        to=User,
        blank=True
    )
    category=models.ForeignKey(
        to='Vacancy_category',
        null=True,blank=True,
        on_delete=models.SET_NULL,
        verbose_name='категория'
    )

    class Meta:
        verbose_name='Вакансия'
        verbose_name_plural='Вакансия'
        ordering=['salary']


    def __str__(self):
        return self.title


class Comapany(models.Model):
    name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    number_employees=models.IntegerField(null=True,blank=True)
    search_employees=models.BooleanField(default=True)

class Vacancy_category(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField(null=True,blank=True)
    def __str__(self):
         return self.name

