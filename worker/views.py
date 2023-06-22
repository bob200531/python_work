from django.shortcuts import render,HttpResponse
from django.http import HttpResponse
from  .models import Workers

# Create your views here.

def workers_Info(request):
    workers=Workers.objects.all
    context={'workers':workers}
    context['example']='hello bob'
    return render(request,"workers.html", context)