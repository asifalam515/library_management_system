# views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Transaction
from .forms import DepositForm, BorrowForm, ReturnForm
from books.models import Book,BorrowedBook
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.template.loader import render_to_string

# views.py

# send email function
def send_transaction_email(user,amount,subject,template):
    
    message=render_to_string(template,{
        'user':user,
        'amount':amount
    })
    send_email =EmailMultiAlternatives(subject,'',to=[user.email])
    send_email.attach_alternative(message,"text/html")
    send_email.send()
    
    
def send_borrow_book_email(user, book_title,subject,template):
     message=render_to_string(template,{
        'user':user,
        
    })
     send_email =EmailMultiAlternatives(subject,'',to=[user.email])
     send_email.attach_alternative(message,"text/html")
     send_email.send()

    

@login_required
def deposit_money(request):
    user_account = request.user.account

    if request.method == 'POST':
        form = DepositForm(request.POST, account=user_account)
        if form.is_valid():
            deposited_amount = form.cleaned_data['amount']

            
            user_account.balance += deposited_amount
           
            user_account.save()

           
            form.instance.balance_before_transaction = user_account.balance - deposited_amount
            form.instance.balance_after_transaction = user_account.balance
            form.instance.transaction_type = 'deposit'
            form.save()

            messages.success(request, 'Deposit successful.')
            send_transaction_email(request.user,deposited_amount,"Deposit Message","deposit_email.html")
            return redirect('home')  # Change 'home' to the desired URL

    else:
        form = DepositForm(account=user_account)

    return render(request, 'deposit_money.html', {'form': form})


# @login_required
# def borrow_book(request, book_id):
#     book = Book.objects.get(pk=book_id)
#     user_account = request.user.account

#     if user_account.borrow_book(book.borrowing_price):
#         # If the user has enough balance, mark the book as borrowed
#         # You may need to create a separate BorrowedBook model to track borrowed books
#         # and relate it to the UserAccount model
#         messages.success(request, f"You have successfully borrowed {book.title}.")
#         return redirect('borrowed_books')  # Redirect to the list of borrowed books
#     else:
#         messages.error(request, "Insufficient balance to borrow the book.")
#         return redirect('home')  # Redirect to the home page or book list page
@login_required
def borrow_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    user_account = request.user.account

    if user_account.borrow_book(book.borrowing_price):
        # If the user has enough balance, create a BorrowedBook record
        BorrowedBook.objects.create(user_account=user_account, book=book)
        messages.success(request, f"You have successfully borrowed {book.title}.")
        send_borrow_book_email(request.user,book.title,"Book Borrowed","borrow_book_email.html")
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
def return_book(request, borrowed_book_id):
    borrowed_book = BorrowedBook.objects.get(pk=borrowed_book_id)

    if not borrowed_book.is_returned:
        # Add the borrowed amount back to the user's balance
        user_account = borrowed_book.user_account
        user_account.balance += borrowed_book.book.borrowing_price
        user_account.save()

        # Mark the book as returned
        borrowed_book.is_returned = True
        borrowed_book.save()

        messages.success(request, f"You have successfully returned {borrowed_book.book.title}.")
    else:
        messages.warning(request, f"{borrowed_book.book.title} has already been returned.")

    return redirect('borrowed_books')

