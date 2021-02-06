from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView
from .forms import UserAddressForm

User = get_user_model()


class UserProfileView(DetailView):
    template_name = 'userprofile/index.html'

    def get_queryset(self):
        return User.objects.all().select_related('profile_set').prefetch_related('profile_set__address_set')

    def get_context_data(self, **kwargs):
        context = {
            'profile': self.get_object(),
            'address_form': UserAddressForm()
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
            form.save(commit=False)
            form.profile = user.profile_set
            form.save()
        print(form.errors)
        return redirect('profile:profile', pk=kwargs.get('pk'))

    def get_form_kwargs(self):
        data = super().get_form_kwargs()
        data['request'] = self.request
        return data

    def get_queryset(self):
        return User.objects.all().select_related('profile_set').prefetch_related('profile_set__address_set')



