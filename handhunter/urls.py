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
from core.views import about, contacts,adres
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',about),
    path('contacts/',contacts),
    path('adres/',adres),
    # path('', homepage),
]