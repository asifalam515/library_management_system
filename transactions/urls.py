from django.urls import path,include
from .views import deposit_money, borrow_book, return_book,borrowed_books

urlpatterns = [
    path('deposit/', deposit_money, name='deposit_money'),
    # path('borrow/', borrow_book, name='borrow_book'),
    path('borrow/<int:book_id>/', borrow_book, name='borrow_book'),

    path('return/', return_book, name='return_book'),
    path('borrowed/', borrowed_books, name='borrowed_books'),
    path('return_book/<int:borrowed_book_id>/', return_book, name='return_book'),


    # Add other URL patterns as needed
]