from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Recruit(models.Model):
    user = models.OneToOneField(
        to = User,
        blank=True,
        on_delete=models.CASCADE
    )
    city = models.CharField(null=True,blank=True,max_length=255,verbose_name='Город')
    country = models.CharField(null=True,blank=True,max_length=255,verbose_name='Страна')
    payment_for_found = models.IntegerField(null=True,blank=True,verbose_name='Денежное поступление')
    bonus_percent = models.DecimalField(max_length=5,decimal_places=2,max_digits=3,verbose_name='Бонусы платежа')
    # bonus_percent = models.IntegerField(null=True,blank=True,verbose_name='Проценты')

    def __str__(self):
        return f"{self.user}"
class ListRecruit(models.Model):
    pass