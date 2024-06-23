from django.urls import path
from ClasesUFC import views

urlpatterns = [
    path("", views.inicio, name='Inicio'),
    path('login/', views.login, name='Login'),
    path('logout/', views.logout, name='Logout'),
    path('clases/', views.clases, name='Clases'),
    path('register/', views.register, name='Register'),
]