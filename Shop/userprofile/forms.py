from django import forms
from .models import Address
from django_countries.widgets import CountrySelectWidget


class UserAddressForm(forms.ModelForm):

    city = forms.CharField(widget=forms.TextInput({
        'placeholder': 'city',
        'class': 'form-control'
    }))

    region = forms.CharField(widget=forms.TextInput({
        'placeholder': 'region',
        'class': 'form-control'
    }))

    street = forms.CharField(widget=forms.TextInput({
        'placeholder': 'street',
        'class': 'form-control'
    }))

    index = forms.CharField(widget=forms.TextInput({
        'placeholder': 'index',
        'class': 'form-control'
    }))

    class Meta:
        model = Address
        exclude = ('profile', )
        widgets = {'country': CountrySelectWidget()}

    def save(self, commit=True):
        # self.profile = self.instance
        print(self.instance)
        return super().save(commit=False)