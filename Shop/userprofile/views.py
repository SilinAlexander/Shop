from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from .forms import UserAddressForm, ChangePassword
from allauth.account.views import PasswordChangeView

User = get_user_model()


class UserProfileView(DetailView):
    template_name = 'userprofile/index.html'

    def get_queryset(self):
        return User.objects.all().select_related('profile_set').prefetch_related('profile_set__address_set')

    def get_context_data(self, **kwargs):
        context = {
            'profile': self.get_object(),
            'address_form': UserAddressForm(),
            'change_password_form': ChangePassword(user=self.get_object())
        }
        return context


class UserAddressView(CreateView):

    template_name = 'userprofile/index.html'

    def post(self, request, *args, **kwargs):
        user = self.get_object()
        print(user)
        print(kwargs)
        print(request.POST)
        form = UserAddressForm(data=request.POST, )
        if form.is_valid():
            form.save()
        print(form.errors)
        return redirect('profile:profile', pk=kwargs.get('pk'))

    def get_queryset(self):
        return User.objects.all().select_related('profile_set').prefetch_related('profile_set__address_set')

    def get_form_kwargs(self):
        data = super().get_form_kwargs()
        data['user'] = self.get_object()
        return data


class ChangePasswordView(PasswordChangeView):
    #template_name = "account/password_change." + app_settings.TEMPLATE_EXTENSION
    form_class = ChangePassword

    def get_success_url(self):
        return reverse_lazy('profile:profile', kwargs={'pk': self.kwargs.get('pk')})

