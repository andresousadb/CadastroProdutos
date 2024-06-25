from django import forms
from .models import Produtos


class CadastroProdutos(forms.ModelForm):

    class Meta:
        model = Produtos
        fields = ["nome", "descricao", "valor", "quantidade", "disponivel"]


class alterarproduto(forms.ModelForm):

    class Meta:
        model = Produtos
        fields = ["nome", "descricao", "valor", "quantidade", "disponivel"]
