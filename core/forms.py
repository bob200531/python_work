from django import forms
from .models import Vacancy
from .models import Comapany


class VacancyForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput({"class": "special form-label mx-auto "}))
    salary = forms.IntegerField(widget=forms.TextInput({"class": "special form-control mx-auto"}))
    description = forms.TimeField(widget=forms.Textarea({"class": "special form-control mx-auto "}))
    email = forms.EmailField(widget=forms.TextInput({"class": "special form-control mx-auto "}))
    contacts = forms.CharField(widget=forms.TextInput({"class": "special form-label mx-auto "}))
    class Meta:
        model=Vacancy # Todo
        fields=['title','salary','description','email','contacts']

class VacancyEditform(forms.ModelForm):
    class Meta:
        model=Vacancy # Todo
        fields = ['title', 'salary', 'description', 'email', 'contacts']

class CompanyForm(forms.ModelForm):
    class Meta:
        model=Comapany
        fields=['name','address','number_employees','search_employees',]
        exclude=['created_at']# исключение не редактируемых полей

class CompanyEdit(forms.ModelForm):
    class Meta:
        model=Comapany
        fields = ['name', 'address', 'number_employees', 'search_employees',]
        exclude = ['created_at']
