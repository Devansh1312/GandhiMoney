from django import views
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.utils.timezone import now



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
        return render(request, 'payment.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            # payment_type = form.save(commit=False)
            # payment_type.user = request.user
            # payment_type.save()
            return redirect('payment')
        else:
            # Add debug statement to check form errors
            print(form.errors)
            return render(request, 'payment.html', {'form': form})
        
class BalanceCreateView(views.View):
    form_class = BalanceForm
    
    def get(self, request):
        form = self.form_class()
        return render(request,'balance.html', {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            # expense = form.save(commit=False)
            # expense.user = request.user
            # expense.save()
            return redirect('balance')
        else:
            return render(request,'balance.html', {"form": form})
        
        
class ExpenseCreateView(views.View):
    form_class = ExpenseForm
    
    def get(self, request):
        form = self.form_class()
        return render(request, 'expenses.html',{"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            # expense = form.save(commit=False)
            # expense.user = request.user
            # expense.save()
            return redirect('expense')
        else:
            return render(request,'expenses.html', {"form": form})

class CreditCreateView(views.View):
    form_class = CreditForm

    def get(self, request):
        form = self.form_class()
        return render(request,'credit.html', {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            # credit = form.save(commit=False)
            # credit.user = request.user
            # credit.save()
            return redirect('credit')
        else:
            return render(request,'credit.html',{"form": form})


class CategoryView(views.View):
    form_class = CategoryForm
    
    def get(self, request):
        form = self.form_class()
        return render(request,'category.html', {'form': form})
    
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            # category = form.save(commit=False)
            # category.user = request.user
            # category.save()
            return redirect('category')
        else:
            return render(request,'category.html', {'form': form})
        
        
        
      


class TableView(views.View):
    def get(self, request):
        current_date = now().date()
        selected_date = request.COOKIES.get('selected_date', current_date)
        expenses = Expense.objects.filter(date_created__date=selected_date)
        credits = Credit.objects.filter(date_created__date=selected_date)
        context = {
            'expenses': expenses,
            'credits': credits,
            'selected_date': selected_date,
        }
        return render(request, 'datalist/tables.html', context)