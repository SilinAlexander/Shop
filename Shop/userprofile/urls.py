from .views import UserProfileView, UserAddressView
from django.urls import path
app_name = 'profile'


urlpatterns = [
    path('profile/<pk>/', UserProfileView.as_view(), name='profile'),
    path('profile/<pk>/address/', UserAddressView.as_view(), name='user_address'),

]