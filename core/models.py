from django.db import models
from worker.models import Workers
from django.contrib.auth.models import User
# Create your models here.
class Vacancy(models.Model):
    title=models.CharField(max_length=255,verbose_name='Название вакансии:')
    salary=models.IntegerField(null=True, blank=False,verbose_name='Зарплата')
    description=models.TextField(default='Нет описания',verbose_name='Описание')
    work_experience = models.IntegerField(verbose_name='Опыт работы',default=0)
    is_relevant=models.BooleanField(default=True,verbose_name='Потверждение')
    email=models.EmailField()
    contacts=models.CharField(max_length=100,verbose_name='контакты')
    skills = models.ForeignKey(
        to = 'Skill',
        on_delete=models.SET_NULL,
        null = True,
        blank = False
    )
    candidates=models.ManyToManyField(
        to=Workers,
        blank=True,
        verbose_name='Кандидат'
    )
    review=models.ManyToManyField(
        to=User,
        blank=True,
        verbose_name='Просметрено'
    )
    STATUS_CHOICES = [
            ('full time','Полный рабочий день'),
            ('part time','Частичная занятость'),
            ('piece work','Сделаная работа'),
        ]
    employment = models.CharField(max_length=10, choices=STATUS_CHOICES, default='full time')
    category=models.ForeignKey(
        to='Vacancy_category',
        null=True,blank=False,
        on_delete=models.SET_NULL,
        verbose_name='Категории'
    )

    class Meta:
        verbose_name='Вакансия'
        verbose_name_plural='Вакансия'
        ordering=['salary']# сортировка
        unique_together=[['title', 'email']]#уникальность полей


    def __str__(self):
        return self.title
class Skill(models.Model):
    skill_name = models.CharField(max_length=100,blank=False,null=False,verbose_name='Назавание навыка')
    # skill_description =models.TextField(verbose_name='Описание')
    # work_experience = models.IntegerField(verbose_name='Опыт работы')
    # STATUS_CHOICES = [
    #     ('full time','Полный рабочий день'),
    #     ('part time','Частичная занятость'),
    #     ('piece work','Сделаная работа'),
    # ]
    # employment = models.CharField(max_length=10,choices=STATUS_CHOICES,default='full time')
    def __str__(self):
        return f'{self.skill_name}'
class Comapany(models.Model):
    name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    number_employees=models.IntegerField(null=True,blank=True)
    search_employees=models.BooleanField(default=True)
    created_at = models.TimeField(auto_now_add=True, verbose_name='Время создания',null=True,blank=True)

class Vacancy_category(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField(null=True,blank=True)
    def __str__(self):
         return self.name

