from pydantic import BaseModel, Field
from typing import Optional

class ProdutoInput(BaseModel):
    nome_produto: str = Field(..., description="Nome do produto no e-commerce", example="Fone de Ouvido Bluetooth Pro")
    preco: float = Field(..., description="Preço do produto em Reais", example=149.90)
    avaliacao_media: float = Field(..., description="Nota média de 1.0 a 5.0", example=3.2)
    num_avaliacoes: int = Field(..., description="Quantidade total de avaliações", example=12)
    investimento_ads: float = Field(..., description="Investimento diário em tráfego pago (R$)", example=20.0)

    class Config:
        json_schema_extra = {
            "example": {
                "nome_produto": "Fone de Ouvido Bluetooth Pro",
                "preco": 149.90,
                "avaliacao_media": 3.2,
                "num_avaliacoes": 12,
                "investimento_ads": 20.0
            }
        }

class DiagnosticoAgenteIA(BaseModel):
    diagnostico_causa: str = Field(..., description="Análise do motivo pelo qual a conversão é alta/baixa")
    plano_acao_cro: list[str] = Field(..., description="Lista de ações recomendadas de otimização")

class PrevisaoOutput(BaseModel):
    nome_produto: str
    probabilidade_conversao: float = Field(..., description="Probabilidade calculada pelo Scikit-Learn (0 a 1)")
    previsao: str = Field(..., description="'Alta Conversao' ou 'Baixa Conversao'")
    analise_agente_ia: Optional[DiagnosticoAgenteIA] = Field(None, description="Análise gerada pelo Agente de IA")