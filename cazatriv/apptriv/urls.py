from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categorias/', views.categorias, name='categorias'),
    path('jugar/<str:categoria>/', views.jugar, name='jugar'),
    path('resultado/', views.resultado, name='resultado'),
]
