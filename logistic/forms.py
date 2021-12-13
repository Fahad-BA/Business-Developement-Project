from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from logistic.models import *
from django.forms import ModelForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60)
    Address_1 = forms.CharField(max_length=256)
    Address_2 = forms.CharField(max_length=256)

    class Meta:
        model = Account
        fields = ("email","username","Address_1","Address_2","password1","password2")

class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('email',)

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
            except Account.DoesNotExist:
                return email
            raise forms.ValidationError('email "%s" is already in use.' % account)

class OrderForm(ModelForm):
    class Meta:
        model = Orders
        fields = ['Link', 'Quantity', 'City', 'Package']
