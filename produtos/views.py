import requests
from django.http import HttpResponse
from .models import Produtos
from .form import CadastroProdutos,alterarproduto
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DeleteView


def CadastroProduto(requests):
    form = CadastroProdutos()

    if requests.method == "POST":

        form = CadastroProdutos(requests.POST)

        if form.is_valid():
            form.save()

            messages.success(requests, "Produto Cadastrado")

            return redirect("visualizar")

    context = {
        'form': form
    }

    return render(requests, 'CadastroProduto.html', context=context)


class ViewProduto(ListView):
    model = Produtos
    context = 'produto'
    template_name = 'VisualizarProdutos.html'


def DeleteProduto(requests, pk):
    produto = Produtos.objects.get(id=pk)

    produto.delete()

    messages.success(requests,"Produto apagado")

    return redirect("visualizar")

def AlterarProduto(requests,pk):
    produto = Produtos.objects.get(id=pk)

    form = alterarproduto(instance=produto)

    if requests.method == "POST":

        form = alterarproduto(requests.POST,instance=produto)

        if form.is_valid():
            form.save()

            messages.success(requests, "Alterado com sucesso")

            return redirect("visualizar")

    context = {
        'form': form
    }

    return render(requests, 'AlterarProdutos.html', context=context)






