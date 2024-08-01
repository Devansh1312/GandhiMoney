# forms.py
from django import forms
from .models import *



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
        fields = ['user','payment_mode', 'name', 'money']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control border'}),

            'payment_mode': forms.Select(attrs={'class': 'form-control border'}),
            'name': forms.TextInput(attrs={'class': 'form-control border', 'placeholder': ' Enter name'}),
            'money': forms.NumberInput(attrs={'class': 'form-control border', 'placeholder': ' Enter amount'}),
        }

class CreditForm(forms.ModelForm):
    class Meta:
        model = Credit
        fields = ['user','payment_mode', 'name', 'money']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control border'}),

            'payment_mode': forms.Select(attrs={'class': 'form-control border'}),
            'name': forms.TextInput(attrs={'class': 'form-control border', 'placeholder': ' Enter name'}),
            'money': forms.NumberInput(attrs={'class': 'form-control border', 'placeholder': ' Enter amount'}),
        }