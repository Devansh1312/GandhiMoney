# forms.py
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError


class SignUpForm(UserCreationForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        label="Confirm Password",
        help_text="Enter the same password as above, for verification."
    )

    class Meta:
        model = CustomUser
        fields = ('user_name', 'email', 'mobile_number', 'password1', 'password2')

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 != password2:
            raise ValidationError("Passwords do not match")
        return cleaned_data

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username or Email')
    password = forms.CharField(widget=forms.PasswordInput)
class UserForm(forms.ModelForm):
    
    class Meta:
        model = CustomUser
        fields = '__all__'
        
class PaymentTypeForm(forms.ModelForm):
    class Meta:
        model = PaymentType
        fields = ['user','name']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control border'}),

            
            
            'name': forms.TextInput(attrs={'class': 'form-control border', 'placeholder': ' Enter name'}),
          
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['user','name']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control border'}),
            
            'name': forms.TextInput(attrs={'class': 'form-control border', 'placeholder': ' Enter name'}),
          
        }

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['user','category', 'payment_mode', 'title', 'date_created', 'money']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control border'}),
           
            'category': forms.Select(attrs={'class': 'form-control border'}),
            'payment_mode': forms.Select(attrs={'class': 'form-control border'}),
            'title': forms.TextInput(attrs={'class': 'form-control border', 'placeholder': ' Enter Title'}),
            'date_created': forms.DateInput(attrs={'class': 'form-control border', 'placeholder': 'Select date', 'type': 'text'}), 
            'money':forms.TextInput(attrs={'class': 'form-control border', 'placeholder': ' Enter Title'})
        }

class BalanceForm(forms.ModelForm):
    class Meta:
        model = Balance
        fields = ['user','payment_mode', 'money']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control border'}),

            'payment_mode': forms.Select(attrs={'class': 'form-control border'}),
            
            'money': forms.NumberInput(attrs={'class': 'form-control border', 'placeholder': ' Enter amount'}),
        }

class CreditForm(forms.ModelForm):
    class Meta:
        model = Credit
        fields = ['user','payment_mode', 'description', 'money','date_created']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control border'}),

            'payment_mode': forms.Select(attrs={'class': 'form-control border'}),
            'description': forms.TextInput(attrs={'class': 'form-control border', 'placeholder': ' Enter name'}),
            'money': forms.NumberInput(attrs={'class': 'form-control border', 'placeholder': ' Enter amount'}),
            'date_created': forms.DateInput(attrs={'class': 'form-control border', 'placeholder': 'Select date', 'type': 'text'}), 

        }