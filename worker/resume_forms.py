from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['name', 'resume_text', 'experience', 'contacts']

class ResumeEditform(forms.ModelForm):
    class Meta:
        model=Resume
        fields=['name', 'resume_text', 'experience', 'contacts']

