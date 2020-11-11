from django.urls import path
from core.views import item_list, checkout, product_page

# here we need to specify the name of the app
app_name = 'core'

urlpatterns = [
    path('', item_list, name='item_list'),
    path('checkout', checkout, name='checkout'),
    path('product-page', product_page, name='product_page'),
]
