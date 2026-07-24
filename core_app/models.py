from django.db import models

# Create your models here.


class RelatorioBatch(models.Model):
    nome_arquivo = models.CharField(max_length=255)
    arquivo_original = models.FileField(upload_to='planilhas/')
    criado_em = models.DateTimeField(auto_now_add=True)
    total_produtos = models.IntegerField(default=0)
    produtos_baixa_conversao = models.IntegerField(default=0)

    def __str__(self):
        return f"Relatório {self.nome_arquivo} - {self.criado_em.strftime('%d/%m/%Y %H:%M')}"

class ProdutoAnalisado(models.Model):
    relatorio = models.ForeignKey(RelatorioBatch, on_delete=models.CASCADE, related_name='produtos')
    nome_produto = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    avaliacao_media = models.FloatField()
    num_avaliacoes = models.IntegerField()
    investimento_ads = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Métricas calculadas pelo Machine Learning
    probabilidade_conversao = models.FloatField()
    previsao_classe = models.CharField(max_length=50) # 'Alta Conversao' ou 'Baixa Conversao'
    
    # Diagnóstico do Agente de IA
    diagnostico_causa = models.TextField(blank=True, null=True)
    plano_acao_cro = models.TextField(blank=True, null=True) # Salvo como texto em lista

    def __str__(self):
        return f"{self.nome_produto} ({self.previsao_classe})"