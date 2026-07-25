# 🚀 E-commerce AI Suite: Machine Learning + Multiagentes + Dashboard Django

O **E-commerce AI Suite** é uma plataforma de inteligência preditiva para e-commerce que combina algoritmos de **Machine Learning (Scikit-Learn)** e **Agentes de IA Generativa (Google Gemini)** para analisar, em lote, a propensão de conversão de produtos e gerar diagnósticos acionáveis de CRO (*Conversion Rate Optimization*).

🔗 **Acesse o Projeto Online:** [https://ecommerce-ai-suite-1.vercel.app](https://ecommerce-ai-suite-1.vercel.app)

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.10+
- **Machine Learning:** Scikit-Learn (Random Forest Classifier), Pandas, NumPy
- **Inteligência Artificial:** SDK do Google Gemini (`google-genai`)
- **Web App & ORM:** Django, Django Templates, WhiteNoise
- **API Framework:** FastAPI, Pydantic, Uvicorn
- **Banco de Dados:** SQLite (Com suporte de auto-migration no ambiente Serverless / PostgreSQL em produção)
- **Frontend:** HTML5, Tailwind CSS (Design Responsivo e Dark Mode)
- **Deploy & Nuvem:** Vercel (Serverless Functions)

---

## 🌟 Principais Funcionalidades

1. **Predição com Machine Learning (Scikit-Learn):**
   - Treinamento sintético calibrado com regras de negócio e penalizações por falta de prova social e notas baixas.
   - Cálculo da probabilidade exata de conversão com base em preço, avaliação média, número de avaliações e investimento em anúncios.

2. **Diagnóstico Estratégico com Agente de IA (Gemini):**
   - Interceptação automática de produtos com previsão de *Baixa Conversão*.
   - Geração de diagnóstico de causa raiz e plano de ação estruturado para otimização de vendas.

3. **Processamento em Lote via Upload de Planilhas (`.xlsx`):**
   - Leitura sequencial e processamento em memória de arquivos Excel usando **Pandas**.
   - Gravação dos históricos e resultados em banco de dados relacional.

4. **Dashboard Interativo & Histórico:**
   - Visualização de métricas gerais (Taxa de Conversão, Total de Produtos, Alertas).
   - Consulta detalhada aos relatórios armazenados no banco de dados.

---

## 📁 Estrutura do Projeto

```text
ecommerce-ai-suite/
├── api_fastapi/            # Módulo desacoplado de API FastAPI
├── config/                 # Configurações do Projeto Django (settings, urls, wsgi)
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py             # Entrada do app e auto-migration para Vercel
├── core/                   # Core de ML e Agentes de IA
│   ├── ai_agent.py         # Integrador do Agente Gemini
│   ├── ml_model.py         # Treinamento e Predição com Scikit-Learn
│   └── schemas.py          # Schemas de validação Pydantic
├── core_app/               # Aplicação Django (Views, Models, Templates, Forms)
│   ├── models.py           # Modelos do ORM (RelatorioBatch, ProdutoAnalisado)
│   ├── views.py            # Regras de Negócio e Upload em memória
│   └── templates/          # Interfaces HTML com Tailwind CSS
├── .env                    # Variáveis de Ambiente (local)
├── .gitignore              # Proteção de arquivos sensíveis
├── manage.py               # Utilitário de comandos do Django
├── vercel.json             # Configuração de rotas para deploy Serverless
├── requirements.txt        # Dependências do Projeto
└── README.md