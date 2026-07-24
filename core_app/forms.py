from django import forms

class UploadPlanilhaForm(forms.Form):
    arquivo = forms.FileField(
        label="Selecione a planilha de produtos (.xlsx)",
        help_text="Certifique-se de que a planilha contenha as colunas: nome_produto, preco, avaliacao_media, num_avaliacoes, investimento_ads"
    )