from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import DetailView

User = get_user_model()


class UserProfileView(DetailView):
    template_name = 'userprofile/index.html'

    def get_queryset(self):
        return User.objects.all().select_related('profile_set').prefetch_related('profile_set__address_set')

    def get_context_data(self, **kwargs):
        context = {
            'profile': self.get_object()
        }
        return context


