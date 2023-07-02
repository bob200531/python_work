from django.contrib import admin
from .models import Vacancy
from .models import   Comapany
from .models import Vacancy_category

admin.site.register(Vacancy)# СОЗДАНЕИ ГОТОВЫХ ПОЛЕЙ
# verbose_name создание на русском полей
# Register your models here.
admin.site.register(Comapany)
admin.site.register(Vacancy_category)
