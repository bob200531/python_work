from django.shortcuts import render
from .models import Recruit
from django.views import View
from django.views.generic import ListView,CreateView

def recruit_list(request):
    recruit_lst =Recruit.objects.all()
    context ={'recruit':recruit_lst}
    return render(request,'recruit-list.html',context)

def detail_recruit(request,pk):
    detail_info = Recruit.objects.get(pk=pk)
    context = {'recruit_detail':detail_info}
    return render(request,'recruit_detail.html',context)
# class RecruitView:
#     def my_method(request):
#         recruit_lst = Recruit.objects.all()
#         context = {'recruit': recruit_lst}
#         return render(request, 'recruit-list.html', context)

class RecruitView(View):
    def get(self,request):
        recruit_lst = Recruit.objects.all()
        context = {'recruit': recruit_lst}
        return render(request, 'recruit-list.html', context)

class RecruitListView(ListView):
    model = Recruit
    template_name = 'recruit_class.html'


class RecruitCreateView(CreateView):
    model = Recruit
    fields = '__all__'
    template_name = 'recruit_form.html'