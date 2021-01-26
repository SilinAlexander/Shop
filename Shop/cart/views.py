from django.shortcuts import render

# Create your views here.
from django.views import View

from mainapp.models import LatestProducts


class ProductInCart(View):

    def get(self, request, *args, **kwargs):
        # # categories = Category.objects.get_categories_for_left_sidebar()
        # products = LatestProducts.objects.get_products_for_main_page(
        #     # 'prod1', 'prod2', with_respect_to='prod1'
        # )
        # context = {
        #     # 'categories': categories,
        #     'products': products,
        #     'cart': self.cart
        # }
        request.session['cart'] = 'fsrergrfg'
        request.session['cart1'] = 'fsrergrfg'
        print(request.session.items())
        return render(request, 'base.html', {})
