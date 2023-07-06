from django import forms
from .models import Vacancy



class VacancyForm(forms.ModelForm):
    class Meta:
        model=Vacancy # ToDo
        fields=['title','salary','description','email','contacts']



