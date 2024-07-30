from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    
    path('test/',PaymentTypeView.as_view(),name="payment"),
    path('',BalanceCreateView.as_view(),name="balance"),
    path('',ExpenseCreateView.as_view(),name="expense"),
    path('',CreditCreateView.as_view(),name="credit"),
    path('',CategoryView.as_view(),name="category"),

]