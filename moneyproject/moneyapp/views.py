from django import views
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.utils.timezone import now
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages

from django.contrib.auth import authenticate, login as auth_login

# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)  # Automatically log the user in after signup
#             return redirect('login')  # Redirect to a home page or wherever you like
#     else:
#         form = SignUpForm()
#     return render(request, 'authentication/signup.html', {'form': form})

# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get("user_name")
#             password = form.cleaned_data.get("password")
#             user = authenticate(username=username, password=password)

#             if user is not None:
#                 if user.is_active:
#                     auth_login(request, user)  # Use auth_login here
#                     return redirect("table")  # Redirect to the appropriate view
#                 else:
#                     messages.warning(request, "User is not active.")
#             else:
#                 messages.error(request, "Invalid credentials")
#         else:
#             messages.error(request, "Invalid credentials")
#     else:
#         form = LoginForm()
#     return render(request, 'authentication/login.html', {'form': form})
 # Redirect to login page after logout
            
class UserCreateView(views.View):
    form_class = UserForm
    
    def get(self, request):
        form = self.form_class()
        return render(request,'authentication/register.html', {'form':form})
    
    def post(self, request):
        form = self.form_class()
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('login')
        return render(request,'authentication/register.html', {'form':form})
        


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
        
        
        
      
from django.utils.timezone import now

class TableView(views.View):
    def get(self, request):
        current_date = now().date()
        selected_date = request.COOKIES.get('selected_date', current_date)
        
        # Date-filtered transactions
        expenses = Expense.objects.filter(date_created__date=selected_date)
        credits = Credit.objects.filter(date_created__date=selected_date)
        balances=Balance.objects.filter(date_created__date=selected_date)
        
        # Total credits and expenses based on selected date
        total_credits_date = sum(credit.money for credit in credits)
        total_expenses_date = sum(expense.money for expense in expenses)
        total_balance =sum(balance.money for balance in balances)
        total_balance_date =  total_balance+(total_credits_date - total_expenses_date)

        # Overall balance calculation (for all dates)
        all_expenses = Expense.objects.all()
        all_credits = Credit.objects.all()
        all_balances = Balance.objects.all()
        
        total_credits_overall = sum(credit.money for credit in all_credits)
        total_expenses_overall = sum(expense.money for expense in all_expenses)
        total_balance_overall =sum(balance.money for balance in all_balances)

        total_balance_overall =total_balance_overall+(total_credits_overall - total_expenses_overall)

        # Calculate totals per payment mode (overall)
        payment_modes = set(credit.payment_mode.name for credit in all_credits) | set(expense.payment_mode.name for expense in all_expenses) | set(balance.payment_mode.name for balance in all_balances)
        totals_by_mode = {}
        for mode in payment_modes:
            total_credits_mode = sum(credit.money for credit in all_credits if credit.payment_mode.name == mode)
            total_expenses_mode = sum(expense.money for expense in all_expenses if expense.payment_mode.name == mode)
            total_balances_mode = sum(balance.money for balance in all_balances if balance.payment_mode.name == mode)

            totals_by_mode[mode] = total_balances_mode+(total_credits_mode - total_expenses_mode)

        # Context for date-filtered transactions
        context = {
            'expenses': expenses,
            'credits': credits,
            'selected_date': selected_date,
            'total_balance_date': total_balance_date,
            'total_balance_overall': total_balance_overall,
            'totals_by_mode': totals_by_mode,
        }
        return render(request, 'datalist/tables.html', context)