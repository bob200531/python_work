from django.shortcuts import render
from django.http import HttpResponse
from .models import Vacancy
from .models import Comapany
# HttpResponse
# Create your views here.

def homepage(request):
    return render(request=request,template_name='index.html')
    # return HttpResponse('hi'),request
def about(request):
    return HttpResponse("Найдите работу или работника мечты")


def contacts(request):
    return  HttpResponse("Phone: +996777123456 Email:gnatawa44@gamil.com")

def adres(request):
    return  HttpResponse("""
    <div>
        <li>
            <oL>г.Бишкек, улица Ленина </ol>
        </li>
    </div>
    """)

def vacancies_list(request):
    vacancies=Vacancy.objects.all
    context={'vacancies':vacancies}
    context['example']='hello world'
    return render(request, 'vacancies.html',context)

def copmpany_list(request):
    company=Comapany.objects.all
    context={'company':company}
    context['example']="lorem ipsum"
    return render(request, "company.html",context)
