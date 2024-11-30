from django.shortcuts import render, redirect
from .models import Transaction, Category, Budget
from .forms import TransactionForm, BudgetForm
from django.contrib.auth.decorators import login_required

@login_required
def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'finance/transaction_list.html', {'transactions': transactions})

@login_required
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'finance/add_transaction.html', {'form': form})

@login_required
def budget_view(request):
    budgets = Budget.objects.filter(user=request.user)
    return render(request, 'finance/budget.html', {'budgets': budgets})

@login_required
def add_budget(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            return redirect('budget')
    else:
        form = BudgetForm()
    return render(request, 'finance/add_budget.html', {'form': form})

@login_required
def report_view(request):
    transactions = Transaction.objects.filter(user=request.user)
    total_income = sum(trans.amount for trans in transactions if trans.transaction_type == 'income')
    total_expense = sum(trans.amount for trans in transactions if trans.transaction_type == 'expense')
    return render(request, 'finance/report.html', {
        'total_income': total_income,
        'total_expense': total_expense
    })