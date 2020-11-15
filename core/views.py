from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, OrderItem, Order
from django.views.generic import ListView, DetailView
from django.utils import timezone


class homeView(ListView):
    model = Item
    template_name = 'home.html'


class itemDetailView(DetailView):
    model = Item
    template_name = 'product.html'


def checkout(request):
    # context = {'items': Item.objects.all(), }
    return render(request, 'checkout.html')


def products(request):
    context = {'items': Item.objects.all(), }
    return render(request, 'product.html', context)


def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    # we add "order_item" and "created" because it is returning a tuple to us
    order_item, created = OrderItem.objects.get_or_create(item=item,
                                                          user=request.user,
                                                          ordered=False)   # ordered = False, then we don't get an item that was already purchased
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(order_item)
    else:
        # if there's no order, then we have to create it
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
    return redirect("core:product", slug=slug)
