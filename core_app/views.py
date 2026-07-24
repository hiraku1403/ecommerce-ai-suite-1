import pandas as pd
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UploadPlanilhaForm
from .models import RelatorioBatch, ProdutoAnalisado

# Importando o ML Engine e o Agente de IA que construímos
from core.ml_model import ml_engine
from core.ai_agent import cro_agent

def upload_e_processar(request):
    """View responsável pelo Upload da Planilha e Processamento em Lote (ML + IA)"""
    if request.method == 'POST':
        form = UploadPlanilhaForm(request.POST, request.FILES)
        if form.is_valid():
            arquivo_excel = request.FILES['arquivo']
            
            try:
                # 1. Leitura direta do arquivo em memória (io.BytesIO) para contornar o Read-Only da Vercel
                df = pd.read_excel(arquivo_excel)
                
                # Validação das colunas
                colunas_esperadas = ['nome_produto', 'preco', 'avaliacao_media', 'num_avaliacoes', 'investimento_ads']
                for col in colunas_esperadas:
                    if col not in df.columns:
                        messages.error(request, f"Coluna obrigatória ausente na planilha: '{col}'")
                        return render(request, 'core_app/upload.html', {'form': form})

                # 2. Criando o registro no banco sem salvar o arquivo físico no disco
                relatorio = RelatorioBatch.objects.create(
                    nome_arquivo=arquivo_excel.name,
                    total_produtos=len(df)
                )

                baixa_conversao_count = 0

                # 3. Processamento Linha por Linha
                for _, linha in df.iterrows():
                    prob, classe = ml_engine.prever(
                        preco=float(linha['preco']),
                        avaliacao_media=float(linha['avaliacao_media']),
                        num_avaliacoes=int(linha['num_avaliacoes']),
                        investimento_ads=float(linha['investimento_ads'])
                    )

                    diagnostico_texto = "Produto com alto potencial de ROI."
                    plano_acao_texto = "Manter estratégia atual e escalar anúncios."

                    if classe == "Baixa Conversao":
                        baixa_conversao_count += 1
                        analise = cro_agent.analisar_performance(
                            nome_produto=str(linha['nome_produto']),
                            preco=float(linha['preco']),
                            avaliacao_media=float(linha['avaliacao_media']),
                            num_avaliacoes=int(linha['num_avaliacoes']),
                            investimento_ads=float(linha['investimento_ads']),
                            probabilidade=prob,
                            previsao=classe
                        )
                        diagnostico_texto = analise.diagnostico_causa
                        plano_acao_texto = " | ".join(analise.plano_acao_cro)

                    # 4. Salva no banco de dados
                    ProdutoAnalisado.objects.create(
                        relatorio=relatorio,
                        nome_produto=str(linha['nome_produto']),
                        preco=float(linha['preco']),
                        avaliacao_media=float(linha['avaliacao_media']),
                        num_avaliacoes=int(linha['num_avaliacoes']),
                        investimento_ads=float(linha['investimento_ads']),
                        probabilidade_conversao=round(prob, 4),
                        previsao_classe=classe,
                        diagnostico_causa=diagnostico_texto,
                        plano_acao_cro=plano_acao_texto
                    )

                relatorio.produtos_baixa_conversao = baixa_conversao_count
                relatorio.save()

                messages.success(request, f"Planilha '{arquivo_excel.name}' processada com sucesso!")
                return redirect('detalhes_relatorio', relatorio_id=relatorio.id)

            except Exception as e:
                messages.error(request, f"Erro ao processar a planilha: {str(e)}")
    else:
        form = UploadPlanilhaForm()

    return render(request, 'core_app/upload.html', {'form': form})


def detalhes_relatorio(request, relatorio_id):
    """Exibe o Dashboard e Relatório Detalhado com as Análises de ML + IA"""
    relatorio = get_object_or_404(RelatorioBatch, id=relatorio_id)
    produtos = relatorio.produtos.all()

    # Cálculo de métricas gerais para os cards do dashboard
    taxa_conversao_alta = 0
    if relatorio.total_produtos > 0:
        taxa_conversao_alta = round(
            ((relatorio.total_produtos - relatorio.produtos_baixa_conversao) / relatorio.total_produtos) * 100, 1
        )

    context = {
        'relatorio': relatorio,
        'produtos': produtos,
        'taxa_conversao_alta': taxa_conversao_alta
    }
    return render(request, 'core_app/detalhes.html', context)


def lista_relatorios(request):
    """Lista o histórico de todas as planilhas já enviadas e salvas no banco"""
    relatorios = RelatorioBatch.objects.all().order_by('-criado_em')
    return render(request, 'core_app/lista_relatorios.html', {'relatorios': relatorios})