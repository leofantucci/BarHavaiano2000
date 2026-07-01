from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.usuariosView, name='home'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('usuarios/', views.usuariosView),
    path('register/<str:role>/', views.registerView, name='register')

]
