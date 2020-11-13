from django.shortcuts import render
from .models import Item
from django.views.generic import ListView, DetailView


class homeView(ListView):
    model = Item
    template_name = 'home.html'


class itemDetailView(DetailView):
    model = Item
    template_name = 'product.html'


def checkout(request):
    # context = {'items': Item.objects.all(), }
    return render(request, 'checkout.html')


# def products(request):
#     context = {'items': Item.objects.all(), }
#     return render(request, 'product.html', context)
