from django.contrib import admin

# Register your models here.

from .models import RelatorioBatch, ProdutoAnalisado

@admin.register(RelatorioBatch)
class RelatorioBatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_arquivo', 'criado_em', 'total_produtos', 'produtos_baixa_conversao')

@admin.register(ProdutoAnalisado)
class ProdutoAnalisadoAdmin(admin.ModelAdmin):
    list_display = ('nome_produto', 'preco', 'probabilidade_conversao', 'previsao_classe')
    list_filter = ('previsao_classe',)