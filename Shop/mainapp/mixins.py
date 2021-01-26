from django.views.generic.detail import SingleObjectMixin
from django.views.generic import View

from .models import Category, Customer, Product
from cart.models import Cart


class CategoryDetailMixin(SingleObjectMixin):

    CATEGORY_SLUG2PRODUCT_MODEL = {
        'prod1s': Product
    }

    def get_context_data(self, **kwargs):
        if isinstance(self.get_object(), Category):
            model = self.CATEGORY_SLUG2PRODUCT_MODEL[self.get_object().slug]
            context = super().get_context_data(**kwargs)
            context['category_products'] = model.objects.all()
            context['categories'] = Category.objects.get_categories_for_left_sidebar()
            return context
        context = super().get_context_data(**kwargs)
        return context


class CartMixin(View):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            cart = Cart.objects.get_or_create(owner=request.user)
        else:
            cart = Cart.objects.filter(for_anonymous_user=True).first()
            if not cart:
                cart = Cart.objects.create(for_anonymous_user=True)
        self.cart = cart
        return super().dispatch(request, *args, **kwargs)
