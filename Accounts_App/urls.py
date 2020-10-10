from django.urls import path

from . import views

urlpatterns = [
    path('Register/', views.Accounts_Register_View, name='Register_Page'),
    path('Login/', views.Accounts_Login_View, name='Login_Page'),
    path('Logout/', views.Accounts_Logout_View, name='Logout_Page'),
]