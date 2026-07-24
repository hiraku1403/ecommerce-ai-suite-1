from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_e_processar, name='upload_planilha'),
    path('historico/', views.lista_relatorios, name='lista_relatorios'),
    path('relatorio/<int:relatorio_id>/', views.detalhes_relatorio, name='detalhes_relatorio'),
]