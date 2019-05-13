from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('listagem/', views.listagem, name='listagem'),
    path('addLogin/', views.novo_Login, name='novo_Login'),
    path('atualizarLogin/<int:pk>/', views.atualizar_Login, name='atualizar_Login')
]
