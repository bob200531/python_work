from django.shortcuts import render
from django.http import HttpResponse
# HttpResponse
# Create your views here.

# def homepage(request):
#     return HttpResponse('hi'),request
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