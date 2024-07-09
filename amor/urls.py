from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.fazer_login, name='login'),
    path('pergunta/<int:pergunta_id>/', views.pergunta, name='pergunta'),
    path('erro/<int:pergunta_id>/', views.erro, name='erro'),
    path('resultado/', views.resultado, name='resultado'),
]
