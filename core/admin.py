from django.contrib import admin
from .models import Vacancy
from .models import   Comapany

admin.site.register(Vacancy)# СОЗДАНЕИ ГОТОВЫХ ПОЛЕЙ
# verbose_name создание на русском полей
# Register your models here.
admin.site.register(Comapany)