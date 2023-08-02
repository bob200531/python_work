from django.shortcuts import render
from .models import ArticleNew
# Create your views here.
def list_news(request):
    news_lst = ArticleNew.objects.all()
    context = {'news_lst': news_lst}
    return render(request,'news.html',context)


def detail_recruit(request,pk):
    news_info = ArticleNew.objects.get(pk=pk)
    context = {'news_deatail':news_info}
    return render(request,'news_deatail.html',context)
