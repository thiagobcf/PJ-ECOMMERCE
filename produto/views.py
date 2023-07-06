from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View


class ListaProdutos(ListView):
    ...


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
