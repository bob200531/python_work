from django.urls import path,include
from .views import *

urlpatterns = [
    path('list-news/',list_news,name='list-news'),
    path('detail-news/<int:pk>/',detail_recruit,name='news_detail'),
]