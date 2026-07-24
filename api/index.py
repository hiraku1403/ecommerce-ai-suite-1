from fastapi import FastAPI, HTTPException
from core.schemas import ProdutoInput, PrevisaoOutput
from core.ml_model import ml_engine
from core.ai_agent import cro_agent

app = FastAPI(
    title="E-commerce AI Suite API",
    description="API de Previsão de Performance de Vendas com Machine Learning & Agentes de IA",
    version="2.0.0"
)

@app.get("/")
def home():
    return {
        "status": "online",
        "service": "E-commerce AI Suite - ML + AI Agent Pipeline",
        "docs": "/docs"
    }

@app.post("/api/v1/predict", response_model=PrevisaoOutput, summary="Prever Performance e Gerar Diagnóstico de IA")
def prever_e_analisar(dados: ProdutoInput):
    """
    1. Passa os dados do produto pelo modelo de Machine Learning (Random Forest)
    2. Envia a previsão e as métricas para o Agente de IA (Gemini) gerar um diagnóstico estratégico
    """
    try:
        # 1. Executa a predição de ML
        prob, classe = ml_engine.prever(
            preco=dados.preco,
            avaliacao_media=dados.avaliacao_media,
            num_avaliacoes=dados.num_avaliacoes,
            investimento_ads=dados.investimento_ads
        )

        # 2. Executa o Agente de IA para gerar a análise
        diagnostico_ia = cro_agent.analisar_performance(
            nome_produto=dados.nome_produto,
            preco=dados.preco,
            avaliacao_media=dados.avaliacao_media,
            num_avaliacoes=dados.num_avaliacoes,
            investimento_ads=dados.investimento_ads,
            probabilidade=prob,
            previsao=classe
        )

        return PrevisaoOutput(
            nome_produto=dados.nome_produto,
            probabilidade_conversao=round(prob, 4),
            previsao=classe,
            analise_agente_ia=diagnostico_ia
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno no pipeline de IA/ML: {str(e)}")