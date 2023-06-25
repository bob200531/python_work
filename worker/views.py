from django.shortcuts import render,HttpResponse
from django.http import HttpResponse
from  .models import Workers

# Create your views here.

def workers_Info(request):
    workers=Workers.objects.all
    context={'workers':workers}
    context['example']='hello bob'
    return render(request,"workers.html", context)

def workers_info(request,id):
    worker_object=Workers.objects.get(id=id)
    context={'worker_user': worker_object}
    return render(request,'user_worker.html',context)
