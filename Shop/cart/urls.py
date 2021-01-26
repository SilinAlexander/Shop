from django.urls import path

from .views import ProductInCart

app_name = 'cart'


urlpatterns = [
    path('carts/', ProductInCart.as_view())

]