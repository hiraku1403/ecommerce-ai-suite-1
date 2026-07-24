import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

class EcommerceMLModel:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.is_trained = False
        self._treinar_modelo_inicial()

    def _gerar_dados_sinteticos(self, n_samples=1000):
        """Gera um dataset realista de e-commerce calibrado para regras de negócio de CRO"""
        np.random.seed(42)
        
        precos = np.random.uniform(20, 1500, n_samples)
        avaliacoes = np.random.uniform(1.0, 5.0, n_samples)
        num_avaliacoes = np.random.randint(0, 500, n_samples)
        investimento_ads = np.random.uniform(0, 1000, n_samples)

        # Regra 1: Avaliações ruins (< 3.2) destroem a conversão no e-commerce (fator de penalização)
        fator_penalizacao_nota = np.where(avaliacoes < 3.2, 0.2, 1.0)

        # Regra 2: Poucas avaliações (< 15) passam pouca confiança
        fator_confianca_num_av = np.where(num_avaliacoes < 15, 0.5, 1.0)

        score_base = (
            (avaliacoes / 5.0) * 0.45 +
            (np.log1p(num_avaliacoes) / 6.0) * 0.25 +
            (np.minimum(investimento_ads, 1000) / 1000.0) * 0.30
        )

        # O score final é multiplicado pelos fatores de penalização
        score_final = score_base * fator_penalizacao_nota * fator_confianca_num_av

        # 1 = Alta Conversão, 0 = Baixa Conversão
        targets = (score_final > 0.48).astype(int)

        df = pd.DataFrame({
            'preco': precos,
            'avaliacao_media': avaliacoes,
            'num_avaliacoes': num_avaliacoes,
            'investimento_ads': investimento_ads,
            'alta_conversao': targets
        })
        return df

    def _treinar_modelo_inicial(self):
        """Treina o modelo Scikit-Learn com os dados"""
        df = self._gerar_dados_sinteticos()
        X = df[['preco', 'avaliacao_media', 'num_avaliacoes', 'investimento_ads']]
        y = df['alta_conversao']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        self.is_trained = True
        print("✅ Modelo de Machine Learning (Random Forest) treinado com sucesso!")

    def prever(self, preco: float, avaliacao_media: float, num_avaliacoes: int, investimento_ads: float):
        """Recebe os dados do produto e devolve a probabilidade e a classe prevista"""
        if not self.is_trained:
            raise Exception("O modelo de ML ainda não foi treinado.")

        input_data = pd.DataFrame([{
            'preco': preco,
            'avaliacao_media': avaliacao_media,
            'num_avaliacoes': num_avaliacoes,
            'investimento_ads': investimento_ads
        }])

        probabilidade = float(self.model.predict_proba(input_data)[0][1])
        previsao_classe = "Alta Conversao" if probabilidade >= 0.5 else "Baixa Conversao"

        return probabilidade, previsao_classe

# Instância global do modelo para reutilização rápida na API
ml_engine = EcommerceMLModel()