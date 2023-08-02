import django_filters
from .models import Vacancy

class VacancyFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    salary__gt = django_filters.NumberFilter(field_name='salary', lookup_expr='gt')# БОЛЬШЕ
    salary__lt = django_filters.NumberFilter(field_name='salary', lookup_expr='lt')# МЕНЬШЕ
    class Meta:
        model = Vacancy
        fields = ['salary','title']
