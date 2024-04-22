from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    class Meta:
        fields = ['email', 'username','password']
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control'})
        }

class RegisterForm(UserCreationForm):
    class Meta:
        fields = ['username','email']
        model = User
        widgets = {
            'email' : forms.EmailInput(attrs={'class':'form-control','required':'required'}),
            'username' : forms.TextInput(attrs={'class': 'form-control'}),
            'password1' : forms.PasswordInput(attrs={'class':'form-control'}),
            'password2' : forms.PasswordInput(attrs={'class':'form-control'})
        }

class UpdateForm(UserChangeForm):
    password = None
    class Meta:
        fields = ['username','email','first_name','last_name']
        model = User
        widgets = {
            'email' : forms.EmailInput(attrs={'class':'form-control','required':'required'}),
            'username' : forms.TextInput(attrs={'class': 'form-control'}),
            'first_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control'}),
        }

