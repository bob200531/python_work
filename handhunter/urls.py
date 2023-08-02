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
from django.urls import path,include
# from core.views import homepage
# from handhunter.core.views import homepage
# from handhunter.core.views import contacts
# from handhunter.core.views import about
from core.views import about, contacts,adres,homepage,vacancies_list,copmpany_list,vacancies_info,search,reg_view
from worker.views import workers_Info,workers_info,resume_info,resume_list,my_resume,add_resume
from core.views import vacancy_add,vacancy_edit,vacancy_add_via_django_form,vacancy_redacto,company_add,company_lists,company_redactor,sign_in,sign_out
from  worker.views import resume_edit,add_resume_df_django_form,resume_edit_dj
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

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
    path('vacancy-redactor/<int:id>/',vacancy_redacto,name='vacancy-redactor'),
    path('company/',copmpany_list),
    path('company-list/<int:id>/',company_lists,name='company-list'),
    path('company_add/',company_add,name='company_add'),
    path('company-redactor/<int:id>/',company_redactor),
    path('workers/',workers_Info),
    path('worker/<int:id>/',workers_info),
    path('resume-list/',resume_list),
    path('resume-info/<int:id>/',resume_info),
    path('my-resume/',my_resume,name='my-resume'),
    # path('vacancy/<int:id>/',vacancies_info,name='vacancy-info'),
    path('search/',search,name='search'),
    path('add-resume/',add_resume,name='add-resume'),
    path('resume-edit/<int:id>/',resume_edit,name='resume-edit'),
    path('resume-edit-dj/<int:id>/',resume_edit_dj,name='resume-edit-dj'),
    path('add-resume-df/',add_resume_df_django_form),
    path('registration/',reg_view, name='reg'),
    path('sign-in/',sign_in,name='sign-in'),
    path('login-generic/',LoginView.as_view(),name='sign-in-generic'),
    path('sign-out/',sign_out,name='sign-out'),
    path('recruit/',include('recruit.urls')),
    path('news/',include('News.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
