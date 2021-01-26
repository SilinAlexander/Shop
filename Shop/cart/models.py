from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

User = get_user_model()


class Cart(models.Model):

    owner = models.OneToOneField(User, null=True, verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField('CartProduct', blank=True, related_name='related_cart')
    # total_products = models.PositiveIntegerField(default=0)
    # final_price = models.DecimalField(max_digits=9, default=0, decimal_places=2, verbose_name='Общая цена')
    in_order = models.BooleanField(default=False)
    for_anonymous_user = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        # cart_data = self.products.aggregate(models.Sum('final_price'), models.Count('id'))
        # if cart_data.get('final_price__sum'):
        #     self.final_price = cart_data['final_price__sum']
        # else:
        #     self.final_price = 0
        # self.total_products = cart_data['id__count']
        super().save(*args, **kwargs)


class CartProduct(models.Model):

    user = models.ForeignKey(User, verbose_name='Покупатель', on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, verbose_name='Корзина', on_delete=models.CASCADE, related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')

    def __str__(self):
        return "Продукт: {} (для корзины)".format(self.content_object.title)

    def save(self, *args, **kwargs):
        self.final_price = self.qty * self.content_object.price
        super().save(*args, **kwargs)
