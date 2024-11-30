from django import forms
from .models import Transaction, Budget

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'category', 'transaction_type', 'date']

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['amount', 'category', 'date']