from .views import UserProfileView, UserAddressView, ChangePasswordView
from django.urls import path
app_name = 'profile'


urlpatterns = [
    path('profile/<pk>/', UserProfileView.as_view(), name='profile'),
    path('profile/<pk>/address/', UserAddressView.as_view(), name='user_address'),
    path('profile/<pk>/change_password/', ChangePasswordView.as_view(), name='change_password'),

]