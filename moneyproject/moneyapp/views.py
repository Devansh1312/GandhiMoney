from django.views import views
from django.shortcuts import render, redirect
from .models import *
from .forms import *

class PaymentType(views.view):
    form_class = PaymentTypeForm
    
    def get(self, request):
        form = self.form_class()
        return render(request, {'form':form})
    
    def post(self, request):
        form = self.form_class()
        if form.is_valid():
            payment_type = form.save(commit=False)
            payment_type.user = request.user
            payment_type.save()
            return redirect('')
        else:
            return render(request,{'form': form} )
        
class BalanceCreate(views.View):
    form_class = BalanceForm
    
    def get(self, request):
        form = self.form_class()
        return render(request, {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('')
        else:
            return render(request, self.template_name, {"form": form})
        
        
class ExpenseCreateView(views.View):
    form_class = ExpenseForm
    
    def get(self, request):
        form = self.form_class()
        return render(request, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('')
        else:
            return render(request, {"form": form})

class CreditCreateView(views.View):
    form_class = CreditForm

    def get(self, request):
        form = self.form_class()
        return render(request, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            credit = form.save(commit=False)
            credit.user = request.user
            credit.save()
            return redirect('credit-list')
        else:
            return render(request, {"form": form})
        