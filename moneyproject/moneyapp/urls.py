from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    
    path('payment/',PaymentTypeView.as_view(),name="payment"),
    path('balance/',BalanceCreateView.as_view(),name="balance"),
    path('expense/',ExpenseCreateView.as_view(),name="expense"),
    path('credit/',CreditCreateView.as_view(),name="credit"),
    path('category/',CategoryView.as_view(),name="category"),

    path('table/',TableView.as_view(),name="table"),

    path('delete_credit/<int:pk>/', DeleteCreditView.as_view(), name='delete_credit'),
    path('delete_expense/<int:pk>/', DeleteExpenseView.as_view(), name='delete_expense'),
    # path('register/', signup, name='register'),
    # path('login/', login, name='login'),


]