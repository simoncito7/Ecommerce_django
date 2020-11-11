from django.shortcuts import render
from .models import Item


def item_list(request):
    # context = {'items': Item.objects.all(), }
    return render(request, 'home-page.html')


def checkout(request):
    # context = {'items': Item.objects.all(), }
    return render(request, 'checkout-page.html')


def product_page(request):
    # context = {'items': Item.objects.all(), }
    return render(request, 'product-page.html')
