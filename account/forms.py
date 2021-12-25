from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-group input-text',
        'placeholder': 'Enter your first name'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-group input-text',
        'placeholder': 'Enter your last name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class' : 'form-group input-text',
        'placeholder': 'Enter your email'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-group input-text',
        'placeholder': 'Enter your username'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'form-group input-text',
        'placeholder': 'Enter your password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'form-group input-text',
        'placeholder': 'Confirm your password'
    }))



    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise ValidationError("passwords don't match")
