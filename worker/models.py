from django.db import models

# Create your models here.
class Workers(models.Model):
    name=models.CharField(max_length=255,verbose_name='Имя')
    specialization=models.CharField(max_length=255,verbose_name='Специализация')
    expected_salary=models.IntegerField(null=True,blank=True,verbose_name='Зарплата')
    job_search=models.BooleanField(default=True,verbose_name='Ищет работу')


