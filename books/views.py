from django.shortcuts import render
from .models import Book,Category
# Create your views here.

# def book_list(request):
#     categories = Category.objects.all()
#     selected_category = request.GET.get('category', None)

#     if selected_category:
#         books = Book.objects.filter(categories__name=selected_category)
#     else:
#         books = Book.objects.all()

#     return render(request, 'books/books.html', {'books': books, 'categories': categories, 'selected_category': selected_category})

def book_list(request):
    categories = Category.objects.all()
    selected_categories = request.GET.getlist('category')

    if selected_categories:
        books = Book.objects.filter(categories__name__in=selected_categories).distinct()
    else:
        books = Book.objects.all()

    return render(request, 'books/books.html', {'books': books, 'categories': categories, 'selected_categories': selected_categories})