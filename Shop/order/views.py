from django.shortcuts import render
from django.views import View
from .models import OrderItem


class CreateOrderView(View):

    def get(self, request):
        #session cart,
        #create Order
        #save in OrderItem
        #
        return render(request, 'order.html', {})
