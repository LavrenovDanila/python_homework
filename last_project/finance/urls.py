from django.urls import path
from .views import transaction_list, add_transaction, budget_view, add_budget, report_view

urlpatterns = [
    path('transactions/', transaction_list, name='transaction_list'),
    path('transactions/add/', add_transaction, name='add_transaction'),
    path('budget/', budget_view, name='budget'),
    path('budget/add/', add_budget, name='add_budget'),
    path('report/', report_view, name='report_view'),
]