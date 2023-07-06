from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from . import models


class ListaProdutos(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 2


class DetalheProduto(View):
    ...


class Adicionaraocarrinho(View):
    ...


class Removerdocarrinho(View):
    ...


class Carrinho(View):
    ...


class Finalizar(View):
    ...
