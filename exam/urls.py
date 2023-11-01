from django.urls import path
from exam import views

urlpatterns = [
    # Authentication
    path('normal_show/', views.ShowQuestionsView.as_view()),
    path('get-question/', views.get_question),  # 获取下一题按钮

    # path('register', views.RegisterView.as_view(), name='auth-register'),  # Auth-Register
    path('show_chapter/', views.ShowChapterView.as_view(),name='show_chapter'),  # 显示哪些章节，展示常规学习界面
    path('show_chapter/get_unit_content/', views.get_unit_content),  # 循环显示各个小节知识点
]
