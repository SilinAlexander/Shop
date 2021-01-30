from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, View
from .models import Product, Category, LatestProducts, Customer
from .mixins import CategoryDetailMixin, CartMixin
from django.http import HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages
from allauth.account.views import SignupView, LoginView
from .forms import UserSignupForm, UserSignInForm
from django.core.mail import send_mail
from cart.models import Cart, CartProduct
from cart.cart import Cart as SessionCart


class BaseView(CartMixin, View):

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        context = {
            'products': products,
            'cart': self.cart
        }
        return render(request, 'index.html', context)


class ProductDetailView(CategoryDetailMixin, DetailView):

    CT_MODEL_MODEL_CLASS = {
        'prod1': Product
    }
    context_object_name = 'product'
    template_name = 'product_detail.html'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CategoryDetailView(DetailView):

    model = Category
    queryset = Category.objects.all()
    context_object_name = 'category'
    template_name = 'category_detail.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['category_products'] = Product.objects.filter(category=self.get_object())
        category = self.get_object()
        context['category_products'] = category.product_set.all()
        return context


class CartView(View):

    def get(self, request, *args, **kwargs):
        cart = SessionCart(request)
        context = {
            'cart': cart
        }
        return render(request, 'cart.html', context)


class AddToCartView(View):

    def post(self, request, *args, **kwargs):

        qty = request.POST.get('qty')
        product = self.get_object()
        print(qty)
        cart = SessionCart(request)
        cart.add(product_id=product.id, qty=qty)
        print(request.session.items())
        messages.add_message(request, messages.INFO, "Товар успешно добавлен")
        return HttpResponseRedirect('/cart/')

    def get_object(self):
        return get_object_or_404(Product, slug=self.kwargs.get('slug'))


class DeleteFromCartView(View):

    def get(self, request, slug, *args, **kwargs):
        # ct_model, product_slug = kwargs.get('ct_model'), kwargs.get('slug')
        # content_type = ContentType.objects.get(model=ct_model)
        # product = content_type.model_class().objects.get(slug=product_slug)
        # cart_product = CartProduct.objects.get(
        #     user=self.cart.owner, cart=self.cart, content_type=content_type, object_id=product.id
        # )
        # self.cart.products.remove(cart_product)
        # cart_product.delete()
        # self.cart.save()
        product = self.get_object()
        cart = SessionCart(request)
        cart.delete(product_id=product.id)
        messages.add_message(request, messages.INFO, "Товар успешно удален")
        return HttpResponseRedirect('/cart/')

    def get_object(self):
        return get_object_or_404(Product, slug=self.kwargs.get('slug'))


class ChangeQTYView(View):

    def post(self, request, *args, **kwargs):
        # cart_product = CartProduct.objects.get(
        #     user=self.cart.owner, cart=self.cart, content_type=content_type, object_id=product.id
        # )
        # qty = int(request.POST.get('qty'))
        # cart_product.qty = qty
        # cart_product.save()
        # self.cart.save()
        product = self.get_object()
        cart = SessionCart(request)
        cart.update(product_id=product.id, qty=request.POST.get('qty'))
        messages.add_message(request, messages.INFO, "Кол-во успешно изменено")
        return HttpResponseRedirect('/cart/')

    def get_object(self):
        return get_object_or_404(Product, slug=self.kwargs.get('slug'))


class UserSignUpView(SignupView):

   form_class = UserSignupForm
   template_name = 'account/signup.html'


class UserSignInView(LoginView):

   form_class = UserSignInForm
   template_name = 'account/login2.html'


class SendEmailView(View):

    def get(self, request, **kwargs):
        subject = 'Hello'
        message = 'Alexander'
        recipients = (
            'alexsilin1997@gmail.com',
            # 'bandirom@ukr.net'

        )
        email_from='alexsilin1997@gmail.com'
        send_mail(subject=subject, message=message, recipient_list=recipients, from_email=email_from)
        return render(request, template_name='base.html')

