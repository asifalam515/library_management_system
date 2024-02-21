from django.shortcuts import render,redirect
from .models import Book,Category
from django.contrib.auth.decorators import login_required
from .models import BorrowedBook
from .forms import ReviewForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404



def book_list(request):
    categories = Category.objects.all()
    selected_categories = request.GET.getlist('category')

    if selected_categories:
        books = Book.objects.filter(categories__name__in=selected_categories).distinct()
    else:
        books = Book.objects.all()

    return render(request, 'books/books.html', {'books': books, 'categories': categories, 'selected_categories': selected_categories})



@login_required
def review_book(request, borrowed_book_id):
    borrowed_book = get_object_or_404(BorrowedBook, pk=borrowed_book_id)

    if borrowed_book.is_returned:
        messages.error(request, 'Cannot review a returned book.')
        return redirect('borrowed_books')

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user_account = borrowed_book.user_account
            review.borrowed_book = borrowed_book
            review.save()

            messages.success(request, 'Review submitted successfully.')
            return redirect('borrowed_books')
        else:
            messages.error(request, 'Form is not valid. Please check the data.')
    else:
        form = ReviewForm()

    return render(request, 'books/review_book.html', {'form': form, 'borrowed_book': borrowed_book})