from django.urls import path
from .views import homeView, checkout, itemDetailView

# here we need to specify the name of the app
app_name = 'core'

urlpatterns = [
    path('', homeView.as_view(), name='home'),
    path('checkout', checkout, name='checkout'),
    path('product/<slug>/', itemDetailView.as_view(), name='product'),
]
