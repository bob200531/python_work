from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Vacancy
from .models import Comapany
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import VacancyForm,VacancyEditform,CompanyForm,CompanyEdit
from  .filters import VacancyFilter
# HttpResponse
# Create your views here.

def homepage(request):
    # if request.method == 'GET':
    #     return HttpResponse('Метод не разрешен, только GET')
    # context={}
    # context['vacban']=Vacancy.objects.all()[:5]
    # return (request,'info.html',context)
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
    # vacancies=Vacancy.objects.all
    vacancies_filter = VacancyFilter(request.GET, queryset=Vacancy.objects.all())
    # context={'vacancies':vacancies}
    # context['example']='hello world'
    context ={"vacancies_filter":vacancies_filter}
    context['example'] = 'hello world'
    return render(request, 'vacancies.html',context)

def vacancies_info(request,id):
    information_read=Vacancy.objects.get(id=id)
    candidate = information_read.candidates.all()
    context={
        'read':information_read,
        'candidates':candidate,
    }
    return render(request,"vacancies/vacancies.html",context)

def copmpany_list(request):
    company=Comapany.objects.all
    context={'company':company}
    context['example']="lorem ipsum"
    return render(request, "company.html",context)


def company_lists(request,id):
    lists_company=Comapany.objects.get(id=id)
    context={'lists':lists_company}
    return render(request,'company/company_list.html',context)


def company_add(request):
    if request.method=='POST':
        company_form=CompanyForm(request.POST)
        if company_form.is_valid():
            company_form.save()
            new_company=company_form.save()
            # return HttpResponse('Добавлено')
            return redirect(f'/company-list/{new_company.id}/')
    ad_company=CompanyForm()
    return render(request,'company/company_add.html',{'add':ad_company})


def company_redactor(request,id):
    company_redactor = Comapany.objects.get(id=id)
    # company_redactor=Comapany.objects.get(id=id)
    if request.method == 'GET':
        redact=CompanyForm(instance=company_redactor)
        return render(request,'company/company_redacto.html',{'redactor_company': redact})
    elif request.method == 'POST':
        redact=CompanyForm(data=request.POST,instance=company_redactor)
        company_save=redact.save()
        return redirect(company_lists,id=company_save.id)





def search(request):
    word=request.GET['keyword']
    vacancies_list=Vacancy.objects.filter(title__contains=word)
    context = {'vacancies': vacancies_list}
    return render(request, 'vacancies.html', context)


def sign_in(request):
    if request.method == 'POST':
        username=request.POST['username']
        password =request.POST['password']
        user = authenticate(username=username,password=password)
        if user :
            login(request,user)
            return redirect(homepage)
        else:
            return HttpResponse('Неверный логин или пороль ')
    return render(request,'auth/sign_in.html')
def sign_out(request):
    logout(request)
    return redirect(sign_in)
def reg_view(request):
    if request.method == "POST":
        user = User(
            username=request.POST["username"]
        )
        user.save()
        user.set_password(request.POST["password"])
        user.save()
        return HttpResponse("Готово")

    return render(
        request,
        "auth/registr.html"
    )

def vacancy_add(request):
    if request.method=='POST':
        add_vacancy=Vacancy(
            title =request.POST['title'],
            salary= request.POST['salary'],
            description= request.POST['description'],
            email = request.POST['email'],
            contacts=request.POST['contacts']
        )
        add_vacancy.save()
        # add_vacancy=add_vacancy.save()
        return redirect(f'/vacancy/{add_vacancy.id}/')
        # return redirect(vacancies_info,id=add_vacancy.id)
        # add_vacancy.save()
    return render(request,"vacancies/vacancy_add.html")


def vacancy_edit(request, id):
    new_vacancy = Vacancy.objects.get(id=id)
    if request.method == 'POST':
        new_vacancy.title = request.POST['title']
        new_vacancy.salary = int(request.POST['salary'])
        new_vacancy.description = request.POST['description']
        new_vacancy.email = request.POST['email']
        new_vacancy.contacts = request.POST['contacts']
        new_vacancy.save()
        return redirect(f'/vacancy/{new_vacancy.id}/')
    return render(request, "vacancies/vacancy_edit.html", {'vacancy': new_vacancy})


def vacancy_add_via_django_form(request):
    if request.method=='POST':
        form=VacancyForm(request.POST,files=request.FILES)
        if form.is_valid():
            new_vacancy=form.save()
            return redirect(f'/vacancy/{new_vacancy.id}/')
    vacancy_form=VacancyForm()
    return render(request, "vacancies/vacancy_django_form.html",{'vacancy_form': vacancy_form})


def vacancy_redacto(request,id):
    vacancy_redact=Vacancy.objects.get(id=id)
    if request.method == 'GET':
        form_redact=VacancyEditform(instance=vacancy_redact)
        return render(request,'vacancies/vacancy_redact.html',{'redict': form_redact})
    elif request.method == 'POST':
        form=VacancyEditform(data=request.POST,instance=vacancy_redact)
        redict=form.save()
        return redirect(vacancies_info,id=redict.id)



# def vacancy_edit(request,id):
#     new_vacancy = Vacancy.objects.get(id=id)
#     if request.method=='POST':
#         new_vacancy.title=request.POST['title']
#         new_vacancy.salary=int(request.POST['salary']),
#         new_vacancy.description=request.POST['description'],
#         new_vacancy.email=request.POST['email'],
#         new_vacancy.contacts=request.POST['contacts']
#         new_vacancy.save()
#         return redirect(f'/vacancy/{add_vacancy.id}/')
#     return render(request,"vacancies/vacancy_edit.html",{'vacancy':new_vacancy})
#



