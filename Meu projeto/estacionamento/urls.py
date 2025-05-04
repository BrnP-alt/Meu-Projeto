from django.urls import path
from vagas import views


urlpatterns = [
    path('', views.listar_vagas, name='listar_vagas'),
    path('ocupar/<int:vaga_id>/', views.ocupar_vaga, name='ocupar_vaga'),
    path('liberar/<int:vaga_id>/', views.liberar_vaga, name='liberar_vaga'),
]
