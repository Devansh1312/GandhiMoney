from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    
    path('test/',PaymentTypeView.as_view(),name="payment"),
    path('a',BalanceCreateView.as_view(),name="balance"),
    path('s',ExpenseCreateView.as_view(),name="expense"),
    path('e',CreditCreateView.as_view(),name="credit"),
    path('dh',CategoryView.as_view(),name="category"),

]