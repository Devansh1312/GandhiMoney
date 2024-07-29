# forms.py
from django import forms
from .models import *

class PaymentTypeForm(forms.ModelForm):
    class Meta:
        model = PaymentType
        fields = ['name']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'paymenttype', 'title', 'date_created', 'money']

class BalanceForm(forms.ModelForm):
    class Meta:
        model = Balance
        fields = ['payment_mode', 'name', 'money']

class CreditForm(forms.ModelForm):
    class Meta:
        model = Credit
        fields = ['payment_mode', 'name', 'money']
