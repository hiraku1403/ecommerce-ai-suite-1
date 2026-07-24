import os
import json
from dotenv import load_dotenv  # <-- 1. Importar o load_dotenv
from google import genai
from core.schemas import DiagnosticoAgenteIA

load_dotenv()  # <-- 2. Carregar o arquivo .env no topo da página

class CROAnalystAgent:
    def __init__(self):
        # Agora ele sempre vai buscar a variável carregada pelo dotenv
        self.api_key = os.getenv("GEMINI_API_KEY")
        if self.api_key:
            self.client = genai.Client(api_key=self.api_key)
        else:
            self.client = None

    def analisar_performance(self, nome_produto: str, preco: float, avaliacao_media: float, num_avaliacoes: int, investimento_ads: float, probabilidade: float, previsao: str) -> DiagnosticoAgenteIA:
        """Agente especialista em e-commerce que analisa o output do ML e gera plano de ação"""
        
        # Se a chave não estiver configurada, retorna um diagnóstico padrão de fallback
        if not self.client:
            return DiagnosticoAgenteIA(
                diagnostico_causa="Variável de ambiente GEMINI_API_KEY não configurada.",
                plano_acao_cro=["Configure a chave para receber análises em tempo real da IA."]
            )

        prompt = f"""
        Você é um Diretor de E-commerce e Especialista em CRO (Conversion Rate Optimization).
        
        Nosso modelo de Machine Learning (Random Forest) analisou um produto e gerou a seguinte previsão:
        - Produto: {nome_produto}
        - Preço: R$ {preco:.2f}
        - Avaliação Média: {avaliacao_media} / 5.0
        - Número de Avaliações: {num_avaliacoes}
        - Investimento Diário em Ads: R$ {investimento_ads:.2f}
        - Previsão do ML: {previsao} (Probabilidade de Venda: {probabilidade * 100:.1f}%)

        Sua tarefa:
        1. Identifique a causa raiz de a conversão ser alta ou baixa com base nos números fornecidos.
        2. Dê de 2 a 3 recomendações acionáveis e diretas de CRO ou tráfego pago para melhorar as vendas.

        Responda estritamente no formato JSON abaixo, sem formatadores markdown extras:
        {{
            "diagnostico_causa": "Explicação concisa e analítica aqui",
            "plano_acao_cro": [
                "Recomendação 1",
                "Recomendação 2"
            ]
        }}
        """

        try:
            response = self.client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt
            )
            
            # Limpa possíveis marcadores de markdown caso o modelo inclua ```json ... ```
            raw_text = response.text.strip()
            if raw_text.startswith("```"):
                raw_text = raw_text.split("\n", 1)[1]
                if raw_text.endswith("```"):
                    raw_text = raw_text.rsplit("\n", 1)[0]
            
            dados = json.loads(raw_text)
            return DiagnosticoAgenteIA(
                diagnostico_causa=dados.get("diagnostico_causa", "Análise realizada."),
                plano_acao_cro=dados.get("plano_acao_cro", ["Otimizar a página do produto."])
            )
        except Exception as e:
            print(f"Erro no Agente de IA: {e}")
            return DiagnosticoAgenteIA(
                diagnostico_causa=f"Não foi possível gerar análise detalhada: {str(e)}",
                plano_acao_cro=["Revisar preço e investimento de anúncios."]
            )

cro_agent = CROAnalystAgent()