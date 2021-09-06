from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.first, name='base'),
    path('index/', views.second, name='index'),
    path("signup", views.SignUp.as_view(), name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"),name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout")
]
