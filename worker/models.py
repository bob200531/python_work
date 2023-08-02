from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Workers(models.Model):# один к одному
    username=models.OneToOneField(
        to=User,
        null=True,
        blank=False,
        # on_delete=models.CASCADE, #значение столбцов для django
        on_delete=models.SET_NULL, # ЗАБИВАЕТ НУЛЯМИ
    )
    name=models.CharField(max_length=255,verbose_name='Имя')
    specialization=models.CharField(max_length=255,verbose_name='Специализация')
    expected_salary=models.IntegerField(null=True,blank=True,verbose_name='Зарплата')
    job_search=models.BooleanField(default=True,verbose_name='Ищет работу')

class Coment(models.Model):
    text=models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)
    worker=models.ForeignKey(
        to=Workers,
        on_delete=models.CASCADE
    )
    author=models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )

class Resume(models.Model):
    name=models.CharField(max_length=255)
    author=models.ForeignKey(
        to=Workers,
        on_delete=models.CASCADE
    )
    resume_text=models.TextField(verbose_name='О себе')
    experience=models.IntegerField(verbose_name='Опыт работы',default=0)
    education=models.CharField(max_length=255,verbose_name='Образование',null=True,blank=False)
    skills=models.CharField(verbose_name='Наваки',max_length=255,default='SEO')
    contacts = models.IntegerField(verbose_name='контакты',null=True,blank=False)
    # contacts = models.CharField(verbose_name='контакты',null=True,blank=False ,max_length=255)
    profile_photo = models.ImageField(
        null=True, blank=True,
        upload_to="profile_photo/",
        verbose_name='Фото сoтрудника',
    )

    def __str__(self):
        return f"{self.author.username}{self.name}"


