from django.urls import path
from authentication import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Authentication
    path('login/', views.LoginView.as_view(), name='auth-login'),  # Auth-Login
    # path('register', views.RegisterView.as_view(), name='auth-register'),  # Auth-Register
]
