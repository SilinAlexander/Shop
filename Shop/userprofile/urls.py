from .views import UserProfileView
from django.urls import path
app_name = 'profile'


urlpatterns = [
    path('profile/<pk>/', UserProfileView.as_view(), name='profile')

]