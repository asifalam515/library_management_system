

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Transaction
from .forms import DepositForm, BorrowForm, ReturnForm

@login_required
def deposit_money(request):
    user_account = request.user.account

    if request.method == 'POST':
        form = DepositForm(request.POST, account=user_account)
        if form.is_valid():
            form.save()
            messages.success(request, 'Deposit successful.')
            return redirect('home')  # Change 'home' to the desired URL
    else:
        form = DepositForm(account=user_account)

    return render(request, 'deposit_money.html', {'form': form})

@login_required
def borrow_book(request):
    user_account = request.user.account

    if request.method == 'POST':
        form = BorrowForm(request.POST, account=user_account)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book borrowed successfully.')
            return redirect('home')  # Change 'home' to the desired URL
    else:
        form = BorrowForm(account=user_account)

    return render(request, 'borrow_book.html', {'form': form})

@login_required
def return_book(request):
    user_account = request.user.account

    if request.method == 'POST':
        form = ReturnForm(request.POST, account=user_account)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book returned successfully.')
            return redirect('home')  # Change 'home' to the desired URL
    else:
        form = ReturnForm(account=user_account)

    return render(request, 'return_book.html', {'form': form})
