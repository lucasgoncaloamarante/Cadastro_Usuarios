from django.urls import path

from app_cadastro_usuarios import views

urlpatterns = [
    # rota, view responsável, nome de referência
    # usuarios.com
    path('', views.home,name='home'),
    #usuarios.com/usuarios
    path('usuario/', views.usuarios, name='listagem_usuarios')
]
