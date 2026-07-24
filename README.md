# 🚀 E-commerce AI Suite: Machine Learning + Multiagentes + Dashboard Django

O **E-commerce AI Suite** é uma plataforma de inteligência preditiva para e-commerce que combina algoritmos de **Machine Learning (Scikit-Learn)** e **Agentes de IA (Google Gemini)** para analisar, em lote, a propensão de conversão de produtos e gerar diagnósticos acionáveis de CRO (*Conversion Rate Optimization*).

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.10+
- **Machine Learning:** Scikit-Learn (Random Forest Classifier), Pandas, NumPy
- **Inteligência Artificial:** SDK do Google Gemini (`google-genai`)
- **Web App & ORM:** Django, Django Templates
- **API Framework:** FastAPI, Pydantic, Uvicorn
- **Banco de Dados:** SQLite (Desenvolvimento) / PostgreSQL (Suporte para Produção)
- **Frontend:** HTML5, Tailwind CSS (Design Responsivo e Dark Mode)

---

## 🌟 Principais Funcionalidades

1. **Predição com Machine Learning (Scikit-Learn):**
   - Treinamento sintético calibrado com regras de negócio e penalizações por falta de prova social e notas baixas.
   - Cálculo da probabilidade exata de conversão com base em preço, avaliação média, número de avaliações e investimento em anúncios.

2. **Diagnóstico Estratégico com Agente de IA (Gemini):**
   - Interceptação automática de produtos com previsão de *Baixa Conversão*.
   - Geração de diagnóstico de causa raiz e plano de ação estruturado para otimização de vendas.

3. **Processamento em Lote via Upload de Planilhas (`.xlsx`):**
   - Leitura sequencial de arquivos Excel usando **Pandas**.
   - Gravação dos históricos e resultados em banco de dados relacional.

4. **Dashboard Interativo & Histórico:**
   - Visualização de métricas gerais (Taxa de Conversão, Total de Produtos, Alertas).
   - Consulta detalhada aos relatórios armazenados no banco de dados.

---

## 📁 Estrutura do Projeto

```text
ecommerce-ai-suite/
├── api/                    # Entrada para Serverless / FastAPI
│   └── index.py
├── config/                 # Configurações do Projeto Django
│   ├── settings.py
│   └── urls.py
├── core/                   # Core de ML e Agentes de IA
│   ├── ai_agent.py         # Integrador do Agente Gemini
│   ├── ml_model.py         # Treinamento e Predição com Scikit-Learn
│   └── schemas.py          # Schemas de validação Pydantic
├── core_app/               # Aplicação Django (Views, Models, Templates)
│   ├── models.py           # Modelos de Banco de Dados (ORM)
│   ├── views.py            # Regras de Negócio e Upload
│   └── templates/          # Interfaces HTML com Tailwind CSS
├── .env                    # Variáveis de Ambiente (não commitado)
├── .gitignore              # Proteção de arquivos sensíveis
├── manage.py               # Utilitário de comandos do Django
├── requirements.txt        # Dependências do Projeto
└── README.md