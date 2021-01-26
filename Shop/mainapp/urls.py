from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.BaseView.as_view(), name='base'),
    path('products/<str:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('category/<str:slug>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('add-to-cart/<str:slug>/', views.AddToCartView.as_view(), name='add_to_cart'),
    path('delete-from-cart/<slug>/', views.DeleteFromCartView.as_view(), name='delete_from_cart'),
    path('change-qty/<str:slug>/',views.ChangeQTYView.as_view(), name='change_qty'),
    path('signup/', views.UserSignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('login/', views.UserSignInView.as_view(), name='login'),
    path('email/', views.SendEmailView.as_view(), name='login'),

]


