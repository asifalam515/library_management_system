# views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Transaction
from .forms import DepositForm, BorrowForm, ReturnForm
from books.models import Book,BorrowedBook

# views.py

@login_required
def deposit_money(request):
    user_account = request.user.account

    if request.method == 'POST':
        form = DepositForm(request.POST, account=user_account)
        if form.is_valid():
            deposited_amount = form.cleaned_data['amount']

            # Update the user's account balance after the deposit
            user_account.balance += deposited_amount
            user_account.save()

            # Save the deposit transaction
            form.instance.balance_before_transaction = user_account.balance - deposited_amount
            form.instance.balance_after_transaction = user_account.balance
            form.instance.transaction_type = 'deposit'
            form.save()

            messages.success(request, 'Deposit successful.')
            return redirect('home')  # Change 'home' to the desired URL

    else:
        form = DepositForm(account=user_account)

    return render(request, 'deposit_money.html', {'form': form})


@login_required
def borrow_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    user_account = request.user.account

    if user_account.borrow_book(book.borrowing_price):
        # If the user has enough balance, mark the book as borrowed
        # You may need to create a separate BorrowedBook model to track borrowed books
        # and relate it to the UserAccount model
        messages.success(request, f"You have successfully borrowed {book.title}.")
        return redirect('borrowed_books')  # Redirect to the list of borrowed books
    else:
        messages.error(request, "Insufficient balance to borrow the book.")
        return redirect('home')  # Redirect to the home page or book list page

@login_required
def borrowed_books(request):
    user_account = request.user.account
    borrowed_books = BorrowedBook.objects.filter(user_account=user_account)
    return render(request, 'borrowed_books.html', {'borrowed_books': borrowed_books})

@login_required
def return_book(request):
    user_account = request.user.account

    if request.method == 'POST':
        form = ReturnForm(request.POST, account=user_account)
        if form.is_valid():
            # Get the borrowed amount from the form
            returned_amount = form.cleaned_data['amount']

            # Check if the user borrowed the book
            if returned_amount > user_account.balance:
                messages.error(request, 'You cannot return more money than you borrowed.')
            else:
                # Update the account balance after the return
                user_account.balance += returned_amount
                user_account.save()

                # Save the return transaction
                form.save()

                messages.success(request, 'Book returned successfully.')
                return redirect('home')  # Change 'home' to the desired URL
    else:
        form = ReturnForm(account=user_account)

    return render(request, 'return_book.html', {'form': form})

