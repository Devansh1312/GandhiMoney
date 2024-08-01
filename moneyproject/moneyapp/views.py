from django import views
from django.shortcuts import render, redirect
from .models import *
from .forms import *



class UserCreateView(views.View):
    form_class = UserForm
    
    def get(self, request):
        form = self.form_class()
        return render(request,'index.html', {'form':form})
    
    def post(self, request):
        form = self.form_class()
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('')
        


class PaymentTypeView(views.View):
    form_class = PaymentTypeForm
    
    def get(self, request):
        form = self.form_class()
        return render(request,'billing.html', {'form':form})
    
    def post(self, request):
        form = self.form_class()
        if form.is_valid():
            payment_type = form.save(commit=False)
            payment_type.user = request.user
            payment_type.save()
            return redirect('payment')
        else:
            return render(request,'billing.html', {'form': form} )
        
class BalanceCreateView(views.View):
    form_class = BalanceForm
    
    def get(self, request):
        form = self.form_class()
        return render(request,'index.html', {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('balance')
        else:
            return render(request,'index.html', {"form": form})
        
        
class ExpenseCreateView(views.View):
    form_class = ExpenseForm
    
    def get(self, request):
        form = self.form_class()
        return render(request, 'index.html',{"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('expense')
        else:
            return render(request,'index.html', {"form": form})

class CreditCreateView(views.View):
    form_class = CreditForm

    def get(self, request):
        form = self.form_class()
        return render(request,'index.html', {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            credit = form.save(commit=False)
            credit.user = request.user
            credit.save()
            return redirect('credit')
        else:
            return render(request,'index.html',{"form": form})


class CategoryView(views.View):
    form_class = CategoryForm
    
    def get(self, request):
        form = self.form_class()
        return render(request,'index.html', {'form': form})
    
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect('category')
        else:
            return render(request,'index.html', {'form': form})
        
        
        
        194761