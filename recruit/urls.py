from django.urls import path
from .views import recruit_list,detail_recruit,RecruitView,RecruitListView,RecruitCreateView



urlpatterns = [
    path('list/',recruit_list,name='recruit'),
    # path('list-class/',RecruitView.my_method,name='recruit-list-class'),
    path('list-class/',RecruitView.as_view(),name='recruit-list-class'),
    path('list-class-generic/',RecruitListView.as_view(),name='recruit-list-class-generic'),
    path('detail/<int:pk>/',detail_recruit,name='recruit_detail'),
    path('create/',RecruitCreateView.as_view(),name='create-recruit'),

]