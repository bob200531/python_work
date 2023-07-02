from django.shortcuts import render,HttpResponse
from django.http import HttpResponse
from  .models import Workers
from .models import Resume

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
    resume_qery = Resume.objects.filter(worker=request.user.worker)
    return render(request,'resume/resume_list.html',{'resumes':resume_qery})



def resume_info(request,id=id):
    resume_object=Resume.objects.get(id=id)
    context={'resume':resume_object}
    return render(request,"resume/resume_info.html",context)



def workers_info(request,id):
    worker_object=Workers.objects.get(id=id)
    context={'worker_user': worker_object}
    return render(request,'user_worker.html',context)

# def my_resume(request):
