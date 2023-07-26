from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponse
from  .models import Workers
from .models import Resume
from .resume_forms import ResumeForm,ResumeEditform
# redirect перенаправлени по сылке
# Create your views here.

def workers_Info(request):
    workers=Workers.objects.all
    context={'workers':workers}
    context['example']='hello bob'
    return render(request,"workers.html", context)


def resume_list(request):
    resume_qery=Resume.objects.all()
    return render(request,'resume/resume_list.html',{'resumes':resume_qery})


def my_resume(request):
    # resume_qery=Resume.objects.all()
    if request.user.is_authenticated:
        resume_qery = Resume.objects.filter(worker=request.user.worker)
        # resume_qery = Resume.objects.filter(worker=request.user.worker)
        return render(request,'resume/resume_list.html',{'resumes':resume_qery})
    else:
        return redirect("home")

def add_resume(request):
    if request.method == 'GET':
        return render(request,'resume_add.html')
        # ПОКАЗЫВАЕТ ФОРМУ
    elif request.method == 'POST':
        new_resume=Resume()
        # new_resume.author=request.worker.author
        new_resume.author=request.user.author
        new_resume.name=request.POST['form-title']
        new_resume.resume_text=request.POST['forma-text']
        new_resume.save()
        # запсывает резюмем БД
        return render(request, 'resume_add.html')



def resume_info(request,id=id):
    resume_object=Resume.objects.get(id=id)
    context={'resume':resume_object}
    return render(request,"resume/resume_info.html",context)

def resume_edit(request, id):
    redactor_resume = Resume.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'resume/resume_redactor.html')
    elif request.method == 'POST':
        redactor_resume.name = request.POST['name']
        redactor_resume.resume_text = request.POST['resume_text']
        redactor_resume.experience = int(request.POST['experience'])
        redactor_resume.contacts= int(request.POST['contacts'])
        # Устанавливаем автора резюме из текущего пользователя
        # redactor_resume.author = request.user
        redactor_resume.save()
        return redirect(f'/resume-info/{redactor_resume.id}/')
    return render(request, 'resume/resume_redactor.html', {'resume': redactor_resume})


def resume_edit_dj(request,id):
    resume_objec=Resume.objects.get(id=id) # записывает даные передачей request.POST
    if request.method=='GET':
        form = ResumeEditform(instance=resume_objec) # считыват данные
        return render(request,'resume/resume_edit_dj.html',{'redacterion':form})
    elif request.method=='POST':
        form = ResumeEditform(data=request.POST,instance=resume_objec,files=request.FILES)
        obj=form.save()
        return redirect(resume_info,id=obj.id)

def add_resume_df_django_form(request):
    if request.method == 'POST':
        form_resume = ResumeForm(request.POST)
        if form_resume.is_valid():
            resume_new = form_resume.save(commit=False)
            resume_new.author_id = request.user.id  # Устанавливаем идентификатор текущего пользователя как автора резюме
            resume_new.save()
            return redirect(f'/resume-info/{resume_new.id}/')
    obj_resume = ResumeForm()
    return render(request, 'resume/resume_django_form.html', {'resume_ad': obj_resume})

# def add_resume_df_django_form(request):
#     if request.method == 'POST':
#         form_resume=ResumeForm(request.POST)
#         if form_resume.is_valid():
#             resume_new=form_resume.save()
#             return redirect(f'/resume-info/{resume_new.id}/')
#     obj_resume = ResumeForm()
#     return render(request,'resume/resume_django_form.html',{'resume_ad':obj_resume})
# def resume_edit(request,id):
#     redactor_resume = Resume.objects.get(id=id)
#     if request.method == 'GET':
#         return render(request,'resume/resume_redactor.html')
#     elif request.method == 'POST':
#         # redactor_resume=Resume.objects.get(id=id)
#         redactor_resume.name=request.POST['name']
#         redactor_resume.author = request.POST['author']
#         redactor_resume.resume_text = request.POST['resume_text']
#     return render(request,'resume/resume_redactor.html',{'resume':redactor_resume})





def workers_info(request,id):
    worker_object=Workers.objects.get(id=id)
    context={'worker_user': worker_object}
    return render(request,'user_worker.html',context)

# def my_resume(request):
