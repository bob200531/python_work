"""
URL configuration for handhunter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from core.views import homepage
# from handhunter.core.views import homepage
# from handhunter.core.views import contacts
# from handhunter.core.views import about
from core.views import about, contacts,adres,homepage,vacancies_list,copmpany_list,vacancies_info,search,reg_view
from worker.views import workers_Info,workers_info,resume_info,resume_list,my_resume,add_resume
from core.views import vacancy_add,vacancy_edit,vacancy_add_via_django_form
from  worker.views import resume_edit,add_resume_df_django_form
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',about),
    path('contacts/',contacts),
    path('adres/',adres),
    path('homepage/',homepage,name="home"),
    # path('', homepage),
    path('vacancies/',vacancies_list),
    path('vacancy/<int:id>/', vacancies_info, name='vacancy-info'),
    path('add-vacansies/', vacancy_add),
    path('add-vacansies-df/',vacancy_add_via_django_form),
    path('vacancy-edit/<int:id>/',vacancy_edit, name='vacancy-edit'),
    path('company/',copmpany_list),
    path('workers/',workers_Info),
    path('worker/<int:id>/',workers_info),
    path('resume-list/',resume_list),
    path('resume-info/<int:id>/',resume_info),
    path('my-resume/',my_resume,name='my-resume'),
    # path('vacancy/<int:id>/',vacancies_info,name='vacancy-info'),
    path('search/',search,name='search'),
    path('add-resume/',add_resume,name='add-resume'),
    path('resume-edit/<int:id>/',resume_edit,name='resume-edit'),
    path('add-resume-df/',add_resume_df_django_form),
    path('registration/',reg_view, name='reg'),
]
