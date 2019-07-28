from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Product
# Create your views here.

class product_list(ListView):
    model = Product

class ProductView(DetailView):
    model = Product


class ProductCreate(CreateView):
    model = Product
    fields = ['name', 'price']
    success_url = reverse_lazy('product_list')

class ProductUpdate(UpdateView):
    model = Product
    fields = ['name', 'price']
    success_url = reverse_lazy('product_list')

class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')

